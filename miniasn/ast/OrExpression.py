from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class OrExpression(Node):
    first = NodeType.AND_EXPRESSION

    def __init__(self, children):
        super().__init__()
        self.children = children

    @staticmethod
    def parse(parser):
        children = []
        and_expression = parser.parse_node(NodeType.AND_EXPRESSION)
        children.append(and_expression)

        while parser.can_parse(TokenType.OR):
            parser.parse_node(TokenType.OR)
            and_expression = parser.parse_node(NodeType.AND_EXPRESSION)
            children.append(and_expression)

        return OrExpression(children)

    def __str__(self):
        result = str(self.children[0])
        for and_expression in self.children[1:]:
            result += ' or {}'.format(and_expression)

        return result
