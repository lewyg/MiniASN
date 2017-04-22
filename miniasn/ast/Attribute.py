from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class Attribute(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, identifier, type):
        super().__init__()
        self.identifier = identifier
        self.type = type
        self.value = None

    @staticmethod
    def parse(parser, *args, **kwargs):
        identifier = parser.parse_node(NodeType.IDENTIFIER)

        type = parser.parse_node(NodeType.TYPE)

        return Attribute(identifier, type)

    @staticmethod
    def __name_in_use(declared_types, name):
        return any(declared_type.identifier.value == name for declared_type in declared_types)

    def __str__(self):
        return '{} {}'.format(self.identifier, self.type)
