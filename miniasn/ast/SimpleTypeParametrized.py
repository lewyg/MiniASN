from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class SimpleTypeParametrized(Node):
    first = [TokenType.UINT,
             TokenType.BITSTRING]

    def __init__(self, type, parameter):
        super().__init__()
        self.type = type
        self.parameter = parameter

    @staticmethod
    def parse(parser, *args, **kwargs):
        type = parser.parse_or_node_list([TokenType.UINT,
                                          TokenType.BITSTRING])

        parameter = None
        if parser.can_parse(TokenType.PARAMETERIZER):
            parser.parse_node(TokenType.PARAMETERIZER)
            parameter = parser.parse_node(NodeType.NUMBER)

        return SimpleTypeParametrized(type, parameter)

    def __str__(self):
        return '{}'.format(self.type) + ('_{}'.format(self.parameter) if self.parameter else '')
