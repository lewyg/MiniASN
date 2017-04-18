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
