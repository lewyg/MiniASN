from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class Boolean(Node):
    first = [TokenType.TRUE,
             TokenType.FALSE]

    def __init__(self, value):
        super().__init__()
        self.value = value

    @staticmethod
    def parse(parser):
        bool_token = parser.parse_or_node_list([TokenType.TRUE,
                                                TokenType.FALSE])

        return Boolean(bool_token)

    def value(self):
        return self.value.token_type == TokenType.TRUE

    def __str__(self):
        return str(self.value())
