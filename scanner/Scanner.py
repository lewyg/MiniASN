from token.Token import Token
from token.TokenType import TokenType


class Scanner:
    current_word = 0

    def __init__(self, file_name):
        self.words = self.__open_file_and_read_words(file_name)

    def __open_file_and_read_words(self, file_name):
        file = open(file_name).read()

        for splitter in TokenType.OPERATOR.keys():
            file = file.replace(splitter, ' ' + splitter + ' ')
        for splitter in TokenType.PARENTHESIS.keys():
            file = file.replace(splitter, ' ' + splitter + ' ')

        return file.split()

    def get_token(self):
        token = None

        if self.current_word < len(self.words):
            word = self.__next_word()
            token_type = self.__tokenize_word(word)
            token = Token(token_type, word)

        return token

    def __next_word(self):
        word = self.words[self.current_word]
        self.current_word += 1

        return word

    def __tokenize_word(self, word):
        if word in TokenType.PARENTHESIS.keys():
            return TokenType.PARENTHESIS[word]
        elif word in TokenType.OPERATOR.keys():
            return TokenType.OPERATOR[word]
        elif word in TokenType.DATA_TYPE.keys():
            return TokenType.DATA_TYPE[word]
        elif word in TokenType.EXPRESSION_CONTROLLER.keys():
            return TokenType.EXPRESSION_CONTROLLER[word]
        elif word.isdigit() and not (len(word) > 1 and word[0] == '0'):
            return TokenType.NUMBER['NAME']
        elif word.isalnum() and word[0].isalpha():
            return TokenType.IDENTIFIER['NAME']
