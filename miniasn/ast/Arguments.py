from miniasn.exceptions.ParserExceptions import NameInUseException, ArgumentsLoadException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class Arguments(Node):
    first = TokenType.SQUARE_LEFT_BRACKET

    def __init__(self, arguments):
        super().__init__()
        self.arguments = arguments

    @staticmethod
    def parse(parser, required_arguments=None, *args, **kwargs):
        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)

        arguments = []
        while True:
            argument = parser.parse_node(NodeType.ARGUMENT)

            if parser.get_local_name(argument):
                raise NameInUseException(argument.identifier.identifier.line,
                                         argument.identifier.identifier.column,
                                         argument.identifier.value)
            parser.local_names.append(argument)
            arguments.append(argument)

            if not parser.can_parse(NodeType.IDENTIFIER):
                break

        if required_arguments and len(arguments) != required_arguments:
            raise ArgumentsLoadException(arguments[0].identifier.identifier.line,
                                         arguments[0].identifier.identifier.column,
                                         len(arguments),
                                         required_arguments,
                                         arguments[0].identifier.value)

        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        return Arguments(arguments)

    def __str__(self):
        if not self.arguments:
            return ''

        return '[{}]'.format(' '.join([str(argument) for argument in self.arguments]))
