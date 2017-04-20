from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class DeclaredType(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, identifier, parameters):
        super().__init__()
        self.identifier = identifier
        self.parameters = parameters

    @staticmethod
    def parse(parser, *args, **kwargs):
        identifier = parser.parse_node(NodeType.IDENTIFIER)

        parameters = parser.parse_node(NodeType.PARAMETERS) if parser.can_parse(NodeType.PARAMETERS) else None

        return DeclaredType(identifier, parameters)

    def __str__(self):
        return '{}{}'.format(self.identifier, self.parameters)

