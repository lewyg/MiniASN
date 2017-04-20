class ParserException(Exception):
    def __init__(self, line, column, reason):
        super(ParserException, self).__init__(line, column, reason)
        self.__line = line
        self.__column = column
        self.__reason = reason

    def __str__(self):
        return 'Parser exception occurred at line {}, column {}: \n\t{}'.format(self.__line,
                                                                                self.__column,
                                                                                self.__reason)


class UnexpectedTokenException(ParserException):
    def __init__(self, line, column, token, expected_token):
        reason = 'Unexpected token {}, expected {}'.format(token.name, expected_token.name)
        super(UnexpectedTokenException, self).__init__(line, column, reason)


class NameInUseException(ParserException):
    def __init__(self, line, column, name):
        reason = 'Name {} is already in use'.format(name)
        super(NameInUseException, self).__init__(line, column, reason)
