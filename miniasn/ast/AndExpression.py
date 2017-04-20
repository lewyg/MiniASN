from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class AndExpression(Node):
    first = NodeType.SIMPLE_EXPRESSION

    def __init__(self, simple_expressions):
        super().__init__()
        self.simple_expressions = simple_expressions

    @staticmethod
    def parse(parser, *args, **kwargs):
        simple_expressions = [parser.parse_node(NodeType.SIMPLE_EXPRESSION)]

        while parser.can_parse(TokenType.AND):
            parser.parse_node(TokenType.AND)
            simple_expressions.append(parser.parse_node(NodeType.SIMPLE_EXPRESSION))

        return AndExpression(simple_expressions)

    def __str__(self):
        return ' and '.join([str(expression) for expression in self.simple_expressions])
