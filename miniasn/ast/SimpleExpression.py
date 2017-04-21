from miniasn.exceptions.ParserExceptions import UnknownNameException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class SimpleExpression(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, left_operand, operator, right_operand):
        super().__init__()
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand
        self.value = None

    @staticmethod
    def parse(parser, *args, **kwargs):
        left_operand = parser.parse_node(NodeType.IDENTIFIER)
        left_operand_definition = parser.get_local_name(left_operand)
        if not left_operand_definition:
            raise UnknownNameException(left_operand.identifier.line,
                                       left_operand.identifier.column,
                                       left_operand.value)

        operator = parser.parse_node(NodeType.RELATIONAL_OPERATOR)
        right_operand = parser.parse_node(NodeType.VALUE)

        return SimpleExpression(left_operand_definition, operator, right_operand)

    def __str__(self):
        return '{} {} {}'.format(self.left_operand, self.operator, self.right_operand)
