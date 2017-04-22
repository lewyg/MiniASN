from miniasn.exceptions.ParserExceptions import NameInUseException
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

        if parser.check_if_name_exists(parser.declared_types, identifier):
            raise NameInUseException(identifier.identifier.line,
                                     identifier.identifier.column,
                                     identifier.value)

        parser.parse_node(TokenType.DECLARER)

        declaration = parser.parse_or_node_list([NodeType.SEQUENCE_DECLARATION,
                                                 NodeType.CHOICE_DECLARATION,
                                                 NodeType.ARRAY_DECLARATION,
                                                 NodeType.SIMPLE_TYPE])

        return Declaration(identifier, declaration)

    def __str__(self):
        return '{} ::= {}'.format(self.identifier, self.declaration)
