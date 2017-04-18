from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class Value(Node):
    first = [TokenType.NUMBER_LITERAL,
             NodeType.BOOLEAN]

    def __init__(self, value):
        super().__init__()
        self.value = value

    @staticmethod
    def parse(parser):
        value = parser.parse_or_node_list([TokenType.NUMBER_LITERAL,
                                           NodeType.BOOLEAN])

        return Value(value)

    def __str__(self):
        return str(self.value)
