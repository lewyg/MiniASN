from tokens.Token import Token
from tokens.Tokenizer import Tokenizer


class Lexer:
    def __init__(self, file_reader):
        self.__file_reader = file_reader
        self.__tokenizer = Tokenizer()

    def get_token(self):
        self.__ignore_whitespaces()
        token = self.__read_token()

        return token

    def __ignore_whitespaces(self):
        next_char = self.__file_reader.next_byte()

        while next_char and next_char.isspace():
            self.__file_reader.read_byte()
            next_char = self.__file_reader.next_byte()

    def __read_token(self):
        word = ''
        descriptors = self.__tokenizer.descriptors
        next_char = self.__file_reader.next_byte()

        if not next_char:
            return None

        possible_descriptors = self.__update_possible_descriptors(descriptors, next_char, len(word))

        while possible_descriptors:
            descriptors = possible_descriptors
            word += self.__file_reader.read_byte()
            next_char = self.__file_reader.next_byte()
            possible_descriptors = self.__update_possible_descriptors(descriptors, next_char, len(word))

        descriptors = self.__get_accepted_descriptors(descriptors, word)

        if not descriptors:
            raise Exception('Unexpected symbol! {}'.format(next_char))

        token_descriptor = descriptors[0]

        self.__check_space(token_descriptor, next_char)

        return Token(token_descriptor.token_type, word, 0, 0)

    def __update_possible_descriptors(self, descriptors, next_char, char_position):
        return [token_descriptor for token_descriptor in descriptors
                if token_descriptor.qualifier(next_char,
                                              char_position,
                                              token_descriptor.token_type.value)]

    def __get_accepted_descriptors(self, descriptors, word):
        return [token_descriptor for token_descriptor in descriptors
                if token_descriptor.acceptor(word,
                                             token_descriptor.token_type.value)]

    def __check_space(self, descriptor, next_char):
        if next_char.isspace():
            return

        if descriptor.required_space and \
                [token_descriptor for token_descriptor in self.__tokenizer.tokens_required_space
                 if token_descriptor.token_type.value[0] == next_char]:
            raise Exception("Space is required for {}".format(descriptor.token_type.name))
