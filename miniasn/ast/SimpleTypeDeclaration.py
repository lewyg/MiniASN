from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class SimpleTypeDeclaration(Node):
    first = NodeType.SIMPLE_TYPE

    def __init__(self, type, parameter):
        super().__init__()
        self.type = type
        self.parameter = parameter

    @staticmethod
    def parse(parser):
        type = parser.parse_node(NodeType.SIMPLE_TYPE)
        parser.parse_node(TokenType.PARAMETERIZER)
        parameter = parser.parse_node(NodeType.NUMBER)

        return SimpleTypeDeclaration(type, parameter)

    def __str__(self):
        return '{}_{}'.format(self.type, self.parameter)
