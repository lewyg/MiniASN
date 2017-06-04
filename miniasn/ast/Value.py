from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class Value(Node):
    first = [NodeType.NUMBER,
             NodeType.BOOLEAN]

    def __init__(self, value):
        super().__init__()
        self.value = value.value

    def get_value(self):
        return self.value

    @staticmethod
    def parse(parser, *args, **kwargs):
        value = parser.parse_or_node_list([NodeType.NUMBER,
                                           NodeType.BOOLEAN])

        return Value(value)

    def __str__(self):
        return str(self.value)
