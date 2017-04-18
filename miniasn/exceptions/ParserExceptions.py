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
        reason = 'Unexpected token {}, expected {}'.format(token, expected_token)
        super(UnexpectedTokenException, self).__init__(line, column, reason)


class EndOfFileException(ParserException):
    def __init__(self, expected_token):
        reason = 'End of file, expected {}'.format(expected_token)
        super(EndOfFileException, self).__init__('-', '-', reason)
