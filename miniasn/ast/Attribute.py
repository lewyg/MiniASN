from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class Attribute(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, identifier, type):
        super().__init__()
        self.identifier = identifier
        self.type = type

    @staticmethod
    def parse(parser):
        identifier = parser.parse_node(NodeType.IDENTIFIER)

        type = parser.parse_node(NodeType.TYPE)

        return Attribute(identifier, type)

    def __str__(self):
        return '{} {}'.format(self.identifier, self.type)
