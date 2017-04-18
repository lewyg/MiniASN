from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class Parameters(Node):
    first = TokenType.SQUARE_LEFT_BRACKET

    def __init__(self, parameters):
        super().__init__()
        self.children = parameters

    @staticmethod
    def parse(parser):
        children = []
        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)

        parameter = parser.parse_node(NodeType.PARAMETER)
        children.append(parameter)

        while parser.can_parse(NodeType.PARAMETER):
            parameter = parser.parse_node(NodeType.PARAMETER)
            children.append(parameter)

        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        return Parameters(children)

    def __str__(self):
        if not self.children:
            return ''

        result = '[{}'.format(self.children[0])
        for parameter in self.children[1:]:
            result += ' {}'.format(parameter)
        result += ']'

        return result
