class LexerException(Exception):
    def __init__(self, line, column, reason):
        super(LexerException, self).__init__(line, column, reason)
        self.__line = line
        self.__column = column
        self.__reason = reason

    def __str__(self):
        return 'Lexer exception occurred at line {}, column {}: \n\t{}'.format(self.__line,
                                                                               self.__column,
                                                                               self.__reason)


class RequiredSpaceException(LexerException):
    def __init__(self, line, column, token):
        reason = 'Space is required between {} and next token'.format(token)
        super(RequiredSpaceException, self).__init__(line, column, reason)


class UndefinedSymbolException(LexerException):
    def __init__(self, line, column, char):
        reason = 'Undefined symbol {}'.format(char)
        super(UndefinedSymbolException, self).__init__(line, column, reason)
