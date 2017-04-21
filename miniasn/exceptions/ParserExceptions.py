class ParserException(Exception):
    def __init__(self, line, column, reason):
        super(ParserException, self).__init__(line, column, reason)
        self.line = line
        self.column = column
        self.reason = reason

    def __str__(self):
        return 'Parser exception occurred at line {}, column {}: \n\t{}'.format(self.line, self.column, self.reason)


class UnexpectedTokenException(ParserException):
    def __init__(self, line, column, token, expected_token):
        reason = 'Unexpected token {}, expected {}'.format(token, expected_token)
        super(UnexpectedTokenException, self).__init__(line, column, reason)


class NotDeclaredTypeException(ParserException):
    def __init__(self, line, column, name):
        reason = 'Type {} is not declared'.format(name)
        super(NotDeclaredTypeException, self).__init__(line, column, reason)


class NameInUseException(ParserException):
    def __init__(self, line, column, name):
        reason = 'Name {} is already in use'.format(name)
        super(NameInUseException, self).__init__(line, column, reason)


class UnknownNameException(ParserException):
    def __init__(self, line, column, name):
        reason = 'Name {} is not defined'.format(name)
        super(UnknownNameException, self).__init__(line, column, reason)


class ParametersLoadException(ParserException):
    def __init__(self, line, column, loaded_parameters, required_parameters, declared_type_name):
        reason = '{} parameters loaded, but {} expected for type {}'.format(loaded_parameters,
                                                                            required_parameters,
                                                                            declared_type_name)
        super(ParametersLoadException, self).__init__(line, column, reason)


class ArgumentsLoadException(ParserException):
    def __init__(self, line, column, loaded_arguments, required_arguments, declared_type_name):
        reason = '{} arguments loaded, but {} expected for type {}'.format(loaded_arguments,
                                                                           required_arguments,
                                                                           declared_type_name)
        super(ArgumentsLoadException, self).__init__(line, column, reason)
