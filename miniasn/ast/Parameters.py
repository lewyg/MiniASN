from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class Parameters(Node):
    first = TokenType.SQUARE_LEFT_BRACKET

    def __init__(self, parameters):
        super().__init__()
        self.parameters = parameters

    @staticmethod
    def parse(parser, *args, **kwargs):
        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)

        parameters = []

        parameter = parser.parse_node(NodeType.PARAMETER)
        parameters.append(parameter)

        while parser.can_parse(NodeType.PARAMETER):
            parameter = parser.parse_node(NodeType.PARAMETER)
            parameters.append(parameter)

        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        return Parameters(parameters)

    def __str__(self):
        if not self.parameters:
            return ''

        result = '[{}'.format(self.parameters[0])
        for parameter in self.parameters[1:]:
            result += ' {}'.format(parameter)
        result += ']'

        return result
