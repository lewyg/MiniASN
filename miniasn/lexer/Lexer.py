from miniasn.lexer import Descriptors
from miniasn.token.Token import Token
from miniasn.exceptions.LexerExceptions import UndefinedSymbolException, RequiredSpaceException
from miniasn.token.TokenType import TokenType


class Lexer:
    __descriptors = Descriptors.descriptors

    def __init__(self, file_reader, descriptors=__descriptors):
        self.__file_reader = file_reader
        self.__descriptors_required_space = [token_descriptor for token_descriptor in self.__descriptors
                                             if token_descriptor.required_space]
        self.__descriptors = descriptors
        self.__token = None

    def get_token(self):
        return self.__token

    def read_next_token(self):
        self.__ignore_whitespaces()
        self.__token = self.__read_token()

        return self.get_token()

    def __ignore_whitespaces(self):
        next_char = self.__file_reader.preview_next_char()

        while next_char and next_char.isspace():
            self.__file_reader.read_char()
            next_char = self.__file_reader.preview_next_char()

    def __read_token(self):
        word = ''
        line, column = self.__file_reader.current_line, self.__file_reader.current_column
        descriptors = self.__descriptors
        next_char = self.__file_reader.preview_next_char()

        if not next_char:
            return Token(TokenType.END_OF_FILE, word, line, column)

        possible_descriptors = self.__update_possible_descriptors(descriptors, next_char, 0)

        while possible_descriptors:
            descriptors = possible_descriptors
            word += self.__file_reader.read_char()
            next_char = self.__file_reader.preview_next_char()
            possible_descriptors = self.__update_possible_descriptors(descriptors, next_char, len(word))

        descriptors = self.__accepted_descriptors(descriptors, word)

        if not descriptors:
            raise UndefinedSymbolException(line, column, word + next_char)

        token_descriptor = descriptors[0]

        self.__check_if_space_is_reqiured(token_descriptor, word, next_char)

        return Token(token_descriptor.token_type, word, line, column)

    def __update_possible_descriptors(self, descriptors, next_char, char_position):
        return [token_descriptor for token_descriptor in descriptors
                if token_descriptor.qualifier(next_char, char_position, token_descriptor.token_value)]

    def __accepted_descriptors(self, descriptors, word):
        return [token_descriptor for token_descriptor in descriptors
                if token_descriptor.acceptor(word, token_descriptor.token_value)]

    def __check_if_space_is_reqiured(self, token_descriptor, word, next_char):
        if next_char.isspace():
            return

        if token_descriptor.required_space and self.__does_next_token_require_space(next_char):
            raise RequiredSpaceException(self.__file_reader.current_line, self.__file_reader.current_column,
                                         '{}({})'.format(word, token_descriptor.token_name))

    def __does_next_token_require_space(self, next_char):
        return bool([token_desc for token_desc in self.__descriptors_required_space
                     if token_desc.qualifier(next_char, 0, token_desc.token_value)])
