class ReaderException(Exception):
    def __init__(self, reason):
        super(ReaderException, self).__init__(reason)
        self.reason = reason

    def __str__(self):
        return 'Reader exception occurred: \n\t{}'.format(self.reason)


class ArgumentsNumberException(ReaderException):
    def __init__(self, name, n_agrs, expected):
        reason = 'Name {} expected {} arguments, but {} given'.format(name, n_agrs, expected)
        super(ArgumentsNumberException, self).__init__(reason)


class ArgumentTypeException(ReaderException):
    def __init__(self, type, expected):
        reason = 'Argument type {} expected, given {}'.format(type, expected)
        super(ArgumentTypeException, self).__init__(reason)


class EndOfBytesException(ReaderException):
    def __init__(self):
        reason = 'End of bytes in file!'
        super(EndOfBytesException, self).__init__(reason)
