class Token:
    def __init__(self, token_type, value):
        self.__token_type = token_type
        self.__value = value

    def __repr__(self):
        return "{:12} -\t {}".format(self.__token_type, self.__value)
