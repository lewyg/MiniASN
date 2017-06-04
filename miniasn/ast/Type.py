from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class Type(Node):
    first = [NodeType.SIMPLE_TYPE,
             NodeType.DECLARED_TYPE]

    def __init__(self, type):
        super().__init__()
        self.type = type

    @staticmethod
    def parse(parser, *args, **kwargs):
        type = parser.parse_or_node_list([NodeType.SIMPLE_TYPE,
                                          NodeType.DECLARED_TYPE])

        return Type(type)

    def read_value(self, reader, *args, **kwargs):
        return self.type.read_value(reader, *args, **kwargs)

    def __str__(self):
        return str(self.type)
