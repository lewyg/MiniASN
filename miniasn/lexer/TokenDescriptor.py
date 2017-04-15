class TokenDescriptor:
    def __init__(self,
                 token_type,
                 qualifier=None,
                 required_space=True,
                 acceptor=None):
        self.__token_type = token_type
        self.__qualifier = qualifier
        self.__required_space = required_space
        self.__acceptor = acceptor

    @property
    def token_type(self):
        return self.__token_type

    @property
    def token_name(self):
        return self.__token_type.name

    @property
    def token_value(self):
        return self.__token_type.value

    @property
    def required_space(self):
        return self.__required_space

    @property
    def qualifier(self):
        return self.__qualifier or self.__standard_qualifier

    @property
    def acceptor(self):
        return self.__acceptor or self.__standard_acceptor

    def __standard_qualifier(self, char, char_position, token_value, *args):
        return token_value[char_position] == char if char_position < len(token_value) else False

    def __standard_acceptor(self, word, token_value, *args):
        return word == token_value
