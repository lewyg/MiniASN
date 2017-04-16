class Parser:
    def __init__(self, lexer):
        self.__lexer = lexer

    def parse(self):
        pass

    def __advance(self):
        return self.__lexer.read_next_token()

    def __check_token_type(self, expected_type):
        token = self.__lexer.get_token()
        return token.token_type is expected_type if token else False
