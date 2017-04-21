from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class Number(Node):
    first = TokenType.NUMBER_LITERAL

    def __init__(self, number):
        super().__init__()
        self.number = number
        self.value = int(self.number.token_value)

    @staticmethod
    def parse(parser, *args, **kwargs):
        number = parser.parse_node(TokenType.NUMBER_LITERAL)

        return Number(number)

    def __str__(self):
        return str(self.value)
