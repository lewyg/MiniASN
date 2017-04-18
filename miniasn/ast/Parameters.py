from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class Parameters(Node):
    first = TokenType.SQUARE_LEFT_BRACKET

    def __init__(self, parameters):
        super().__init__()
        self.parameters = parameters

    @staticmethod
    def parse(parser):
        parameters = []
        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)

        parameter = parser.parse_node(NodeType.PARAMETER)
        parameters.append(parameter)

        while parser.can_parse(NodeType.PARAMETER):
            parameter = parser.parse_node(NodeType.PARAMETER)
            parameters.append(parameter)

        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        return Parameters(parameters)
