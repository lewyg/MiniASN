class Token:
    def __init__(self, token_type, token_value, line, column):
        self.__token_type = token_type
        self.__token_value = token_value
        self.__line = line
        self.__column = column

    @property
    def token_type(self):
        return self.__token_type

    @property
    def token_value(self):
        return self.__token_value

    @property
    def line(self):
        return self.__line

    @property
    def column(self):
        return self.__column

    def __repr__(self):
        return "{}({})".format(self.token_value, self.token_type.name)

    def __str__(self):
        return self.token_value
