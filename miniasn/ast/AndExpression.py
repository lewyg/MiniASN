from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class AndExpression(Node):
    first = NodeType.SIMPLE_EXPRESSION

    def __init__(self, children):
        super().__init__()
        self.children = children

    @staticmethod
    def parse(parser):
        children = []

        simple_expression = parser.parse_node(NodeType.SIMPLE_EXPRESSION)
        children.append(simple_expression)

        while parser.can_parse(TokenType.AND):
            parser.parse_node(TokenType.AND)
            simple_expression = parser.parse_node(NodeType.SIMPLE_EXPRESSION)
            children.append(simple_expression)

        return AndExpression(children)

    def __str__(self):
        result = str(self.children[0])
        for simple_expression in self.children[1:]:
            result += ' and {}'.format(simple_expression)

        return result
