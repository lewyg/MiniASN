from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class Identifier(Node):
    first = TokenType.IDENTIFIER

    def __init__(self, identifier):
        super().__init__()
        self.identifier = identifier
        self.value = self.identifier.token_value

    def get_value(self):
        return self.value

    @staticmethod
    def parse(parser, *args, **kwargs):
        identifier = parser.parse_node(TokenType.IDENTIFIER)

        return Identifier(identifier)

    def __str__(self):
        return self.value
