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
        token_list = self.__tokenizer.descriptors

        next_char = self.__file_reader.next_byte()
        if not next_char:
            return None

        word = ''
        possible_tokens = [token for token in token_list
                           if token.qualifier(next_char, len(word), token.token_type.value)]

        while possible_tokens:
            token_list = possible_tokens
            word += self.__file_reader.read_byte()
            next_char = self.__file_reader.next_byte()
            possible_tokens = [token for token in token_list
                               if token.qualifier(next_char, len(word), token.token_type.value)]

        token_list = [token for token in token_list if token.acceptor(word, token.token_type.value)]

        if not token_list:
            raise Exception("zly znak")

        tokena = token_list[0]

        if not next_char.isspace() and tokena.required_space and tokena not in self.__tokenizer.tokens_required_space:
            raise Exception("spacja")

        return Token(tokena.token_type, word, 0, 0)
