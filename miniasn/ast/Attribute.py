from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class Attribute(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, identifier, type):
        super().__init__()
        self.identifier = identifier
        self.type = type
        self.value = None

    def get_value(self):
        return self.value

    @staticmethod
    def parse(parser, *args, **kwargs):
        identifier = parser.parse_node(NodeType.IDENTIFIER)

        type = parser.parse_node(NodeType.TYPE)

        return Attribute(identifier, type)

    def read_value(self, reader, *args, **kwargs):
        self.value = self.type.read_value(reader, *args, **kwargs)
        return "{} = {}".format(self.identifier, self.value)

    def __str__(self):
        return '{} {}'.format(self.identifier, self.type)
