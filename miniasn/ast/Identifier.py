from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class Identifier(Node):
    first = TokenType.IDENTIFIER

    def __init__(self, identifier):
        super().__init__()
        self.identifier = identifier

    @staticmethod
    def parse(parser, *args, **kwargs):
        identifier = parser.parse_node(TokenType.IDENTIFIER)

        return Identifier(identifier)

    def value(self):
        return self.identifier.token_value

    def __str__(self):
        return self.value()
