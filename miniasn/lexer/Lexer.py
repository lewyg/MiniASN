from miniasn.lexer.TokenDescriptor import TokenDescriptor
from miniasn.token.Token import Token
from miniasn.token.TokenType import TokenType
from miniasn.exceptions.LexerExceptions import UndefinedSymbolException, RequiredSpaceException


class Lexer:
    __descriptors = [
        TokenDescriptor(token_type=TokenType.EQUAL,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.NOT_EQUAL,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.GREATER,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.LESS,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.GREATER_OR_EQUAL,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.LESS_OR_EQUAL,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.ASSIGN,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.PARAMETRIZE,
                        required_space=False),

        TokenDescriptor(token_type=TokenType.LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.RIGHT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.SQUARE_LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.SQUARE_RIGHT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.CLIP_LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.CLIP_RIGHT_BRACKET,
                        required_space=False),

        TokenDescriptor(token_type=TokenType.UNIT),
        TokenDescriptor(token_type=TokenType.BITSTRING),
        TokenDescriptor(token_type=TokenType.BOOL),
        TokenDescriptor(token_type=TokenType.ARRAY),
        TokenDescriptor(token_type=TokenType.CHOICE),
        TokenDescriptor(token_type=TokenType.SEQUENCE),

        TokenDescriptor(token_type=TokenType.AND),
        TokenDescriptor(token_type=TokenType.OR),
        TokenDescriptor(token_type=TokenType.DEFAULT),

        TokenDescriptor(token_type=TokenType.TRUE),
        TokenDescriptor(token_type=TokenType.FALSE),

        # non-standard TokenDescriptions always at end!
        TokenDescriptor(token_type=TokenType.NUMBER_LITERAL,
                        qualifier=lambda char, *args: char.isdigit(),
                        acceptor=lambda word, *args: word.isdigit()),
        TokenDescriptor(token_type=TokenType.IDENTIFIER,
                        qualifier=lambda char, char_position, *args:
                        char.isalnum() if char_position else char.isalpha(),
                        acceptor=lambda word, *args: word.isalnum()),
    ]

    def __init__(self, file_reader):
        self.__file_reader = file_reader
        self.__descriptors_required_space = [token_descriptor for token_descriptor in self.__descriptors
                                             if token_descriptor.required_space]
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
            return None

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

        if token_descriptor.required_space and self.__next_token_required_space(next_char):
            raise RequiredSpaceException(self.__file_reader.current_line, self.__file_reader.current_column,
                                         '{}({})'.format(word, token_descriptor.token_name))

    def __next_token_required_space(self, next_char):
        return bool([token_desc for token_desc in self.__descriptors_required_space
                     if token_desc.qualifier(next_char, 0, token_desc.token_value)])
