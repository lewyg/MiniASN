from miniasn.node.Node import Node
from miniasn.token.TokenType import TokenType


class RelationalOperator(Node):
    first = [TokenType.EQUAL,
             TokenType.NOT_EQUAL,
             TokenType.GREATER,
             TokenType.GREATER_OR_EQUAL,
             TokenType.LESS,
             TokenType.LESS_OR_EQUAL]

    def __init__(self, operator):
        super().__init__()
        self.operator = operator

    @staticmethod
    def parse(parser, *args, **kwargs):
        operator = parser.parse_or_node_list([TokenType.EQUAL,
                                              TokenType.NOT_EQUAL,
                                              TokenType.GREATER,
                                              TokenType.GREATER_OR_EQUAL,
                                              TokenType.LESS,
                                              TokenType.LESS_OR_EQUAL])
        return RelationalOperator(operator)

    def __str__(self):
        return str(self.operator)
