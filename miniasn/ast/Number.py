from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class Number(Node):
    first = TokenType.NUMBER_LITERAL

    def __init__(self, value):
        super().__init__()
        self.__value = value

    @staticmethod
    def parse(parser):
        number_token = parser.parse_node(TokenType.NUMBER_LITERAL)

        return Number(number_token)

    def value(self):
        return int(self.__value.token_value)
