from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class Declaration(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, identifier, declaration):
        super().__init__()
        self.identifier = identifier
        self.declaration = declaration

    @staticmethod
    def parse(parser, *args, **kwargs):
        identifier = parser.parse_node(NodeType.IDENTIFIER)

        parser.parse_node(TokenType.DECLARER)

        declaration = parser.parse_or_node_list([NodeType.SIMPLE_TYPE_DECLARATION,
                                                 NodeType.SEQUENCE_DECLARATION,
                                                 NodeType.CHOICE_DECLARATION,
                                                 NodeType.ARRAY_DECLARATION])

        return Declaration(identifier, declaration)

    @staticmethod
    def __name_in_use(declared_types, name):
        return any(declared_type.identifier.value() == name for declared_type in declared_types)

    def __str__(self):
        return '{} ::= {}'.format(self.identifier, self.declaration)
