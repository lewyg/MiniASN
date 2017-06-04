from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class OrExpression(Node):
    first = NodeType.AND_EXPRESSION

    def __init__(self, and_expressions):
        super().__init__()
        self.and_expressions = and_expressions
        self.value = None

    def get_value(self):
        self.value = False

        for expression in self.and_expressions:
            if expression.get_value():
                self.value = True
                break

        return self.value

    @staticmethod
    def parse(parser, *args, **kwargs):
        and_expressions = [parser.parse_node(NodeType.AND_EXPRESSION)]

        while parser.can_parse(TokenType.OR):
            parser.parse_node(TokenType.OR)
            and_expressions.append(parser.parse_node(NodeType.AND_EXPRESSION))

        return OrExpression(and_expressions)

    def __str__(self):
        return ' or '.join([str(expression) for expression in self.and_expressions])
