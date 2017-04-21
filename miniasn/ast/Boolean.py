from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class Boolean(Node):
    first = [TokenType.TRUE,
             TokenType.FALSE]

    def __init__(self, bool):
        super().__init__()
        self.bool = bool
        self.value = self.bool.token_type == TokenType.TRUE

    @staticmethod
    def parse(parser, *args, **kwargs):
        boolean = parser.parse_or_node_list([TokenType.TRUE,
                                             TokenType.FALSE])

        return Boolean(boolean)

    def __str__(self):
        return str(self.value)
