from miniasn.token.Tokenizer import Tokenizer

from miniasn.token.Token import Token


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

        descriptors = self.__accepted_descriptors(descriptors, word)

        if not descriptors:
            raise Exception('Unexpected symbol! {}'.format(next_char))

        token_descriptor = descriptors[0]

        self.__check_if_space_is_reqiured(token_descriptor, next_char)

        return Token(token_descriptor.token_type, word, 0, 0)

    def __update_possible_descriptors(self, descriptors, next_char, char_position):
        return [token_descriptor for token_descriptor in descriptors
                if token_descriptor.qualifier(next_char,
                                              char_position,
                                              token_descriptor.token_type.value)]

    def __accepted_descriptors(self, descriptors, word):
        return [token_descriptor for token_descriptor in descriptors
                if token_descriptor.acceptor(word,
                                             token_descriptor.token_type.value)]

    def __check_if_space_is_reqiured(self, token_descriptor, next_char):
        if next_char.isspace():
            return

        if token_descriptor.required_space and \
                [token_required_space for token_required_space in self.__tokenizer.tokens_required_space
                 if token_required_space.token_type.value[0] == next_char]:
            raise Exception("Space is required for {}".format(token_descriptor.token_type.name))
