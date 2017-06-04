from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class Argument(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, identifier):
        super().__init__()
        self.identifier = identifier
        self.value = None

    def get_value(self):
        return self.value

    @staticmethod
    def parse(parser, *args, **kwargs):
        identifier = parser.parse_node(NodeType.IDENTIFIER)

        return Argument(identifier)

    def __str__(self):
        return str(self.identifier)
