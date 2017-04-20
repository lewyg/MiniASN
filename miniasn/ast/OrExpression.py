from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class OrExpression(Node):
    first = NodeType.AND_EXPRESSION

    def __init__(self, and_expressions):
        super().__init__()
        self.and_expressions = and_expressions

    @staticmethod
    def parse(parser, *args, **kwargs):
        and_expressions = []

        and_expression = parser.parse_node(NodeType.AND_EXPRESSION)
        and_expressions.append(and_expression)

        while parser.can_parse(TokenType.OR):
            parser.parse_node(TokenType.OR)
            and_expression = parser.parse_node(NodeType.AND_EXPRESSION)
            and_expressions.append(and_expression)

        return OrExpression(and_expressions)

    def __str__(self):
        result = str(self.and_expressions[0])
        for and_expression in self.and_expressions[1:]:
            result += ' or {}'.format(and_expression)

        return result
