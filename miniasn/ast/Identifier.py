from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class Identifier(Node):
    first = TokenType.IDENTIFIER

    def __init__(self, value):
        super().__init__()
        self.__value = value

    @staticmethod
    def parse(parser):
        identifier_token = parser.parse_node(TokenType.IDENTIFIER)

        return Identifier(identifier_token)

    def value(self):
        return self.__value.token_value
