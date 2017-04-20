from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class Arguments(Node):
    first = TokenType.SQUARE_LEFT_BRACKET

    def __init__(self, arguments):
        super().__init__()
        self.arguments = arguments

    @staticmethod
    def parse(parser, *args, **kwargs):
        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)

        arguments = [parser.parse_node(NodeType.IDENTIFIER)]

        while parser.can_parse(NodeType.IDENTIFIER):
            arguments.append(parser.parse_node(NodeType.IDENTIFIER))

        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        return Arguments(arguments)

    def __str__(self):
        if not self.arguments:
            return ''

        return '[{}]'.format(' '.join([str(argument) for argument in self.arguments]))
