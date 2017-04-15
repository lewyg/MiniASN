def standard_qualifier(char, char_position, token_value, *args):
    return token_value[char_position] == char if char_position < len(token_value) else False


def standard_acceptor(word, token_value, *args):
    return word == token_value


class TokenDescriptor:
    def __init__(self,
                 token_type,
                 qualifier=standard_qualifier,
                 required_space=True,
                 acceptor=standard_acceptor):
        self.__token_type = token_type
        self.__qualifier = qualifier
        self.__required_space = required_space
        self.__acceptor = acceptor

    @property
    def token_type(self):
        return self.__token_type

    @property
    def required_space(self):
        return self.__required_space

    @property
    def qualifier(self):
        return self.__qualifier

    @property
    def acceptor(self):
        return self.__acceptor
