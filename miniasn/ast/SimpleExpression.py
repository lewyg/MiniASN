from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class SimpleExpression(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, left_operand, operator, right_operand):
        super().__init__()
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

    @staticmethod
    def parse(parser, *args, **kwargs):
        left_operand = parser.parse_node(NodeType.IDENTIFIER)
        operator = parser.parse_node(NodeType.RELATIONAL_OPERATOR)
        right_operand = parser.parse_node(NodeType.VALUE)

        return SimpleExpression(left_operand, operator, right_operand)

    def __str__(self):
        return '{} {} {}'.format(self.left_operand, self.operator, self.right_operand)
