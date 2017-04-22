from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class SimpleType(Node):
    first = [NodeType.SIMPLE_TYPE_PARAMETRIZED,
             TokenType.BOOL]

    def __init__(self, type):
        super().__init__()
        self.type = type

    @staticmethod
    def parse(parser, *args, **kwargs):
        type = parser.parse_or_node_list([NodeType.SIMPLE_TYPE_PARAMETRIZED,
                                          TokenType.BOOL])

        return SimpleType(type)

    def required_arguments(self):
        return 0

    def __str__(self):
        return str(self.type)
