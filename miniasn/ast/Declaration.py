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
    def parse(parser):
        identifier = parser.parse_node(NodeType.IDENTIFIER)
        parser.parse_node(TokenType.DECLARER)

        declaration = parser.parse_or_node_list([NodeType.SIMPLE_TYPE_DECLARATION,
                                                 NodeType.SEQUENCE_DECLARATION,
                                                 NodeType.CHOICE_DECLARATION,
                                                 NodeType.ARRAY_DECLARATION])

        return Declaration(identifier, declaration)
