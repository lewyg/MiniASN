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

    @staticmethod
    def __name_in_use(declared_types, name):
        return any(declared_type.identifier.value() == name for declared_type in declared_types)

    def __str__(self):
        return '{}{}'.format(self.identifier, self.parameters or '')

