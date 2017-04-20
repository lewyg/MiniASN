from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.Token import Token
from miniasn.token.TokenType import TokenType


class ChoiceAttribute(Node):
    first = NodeType.TYPE

    def __init__(self, type, expression):
        super().__init__()
        self.type = type
        self.expression = expression

    @staticmethod
    def parse(parser, *args, **kwargs):
        type = parser.parse_node(NodeType.TYPE)

        parser.parse_node(TokenType.LEFT_BRACKET)
        expression = parser.parse_or_node_list([NodeType.OR_EXPRESSION,
                                                TokenType.DEFAULT])
        parser.parse_node(TokenType.RIGHT_BRACKET)

        return ChoiceAttribute(type, expression)

    def is_default(self):
        return type(self.expression) is Token and self.expression.token_type == TokenType.DEFAULT

    def __str__(self):
        return '{}({})'.format(self.type, self.expression)
