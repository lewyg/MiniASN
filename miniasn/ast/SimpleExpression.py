from miniasn.exceptions.ParserExceptions import UnknownNameException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class SimpleExpression(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, left_operand, operator, right_operand):
        super().__init__()
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand
        self.value = None

    def get_value(self):
        left_value = str(self.left_operand.get_value()).upper()
        operator_type = self.operator.operator.token_type
        right_value = str(self.right_operand.get_value()).upper()

        if operator_type == TokenType.EQUAL:
            self.value = left_value == right_value
        elif operator_type == TokenType.NOT_EQUAL:
            self.value = left_value != right_value
        elif left_value.isdigit() and right_value.isdigit():
            if operator_type == TokenType.GREATER:
                self.value = int(left_value) > int(right_value)
            elif operator_type == TokenType.LESS:
                self.value = int(left_value) < int(right_value)
            elif operator_type == TokenType.GREATER_OR_EQUAL:
                self.value = int(left_value) >= int(right_value)
            elif operator_type == TokenType.LESS_OR_EQUAL:
                self.value = int(left_value) <= int(right_value)
        else:
            self.value = False

        return self.value

    @staticmethod
    def parse(parser, *args, **kwargs):
        left_operand = parser.parse_node(NodeType.IDENTIFIER)
        left_operand_definition = parser.check_if_name_exists(parser.local_names, left_operand)
        if not left_operand_definition:
            raise UnknownNameException(left_operand.identifier.line,
                                       left_operand.identifier.column,
                                       left_operand.value)

        operator = parser.parse_node(NodeType.RELATIONAL_OPERATOR)

        right_operand = parser.parse_or_node_list([NodeType.IDENTIFIER,
                                                   NodeType.VALUE])
        if right_operand.first == TokenType.IDENTIFIER:
            right_operand_definition = parser.check_if_name_exists(parser.local_names, right_operand)
            if not right_operand_definition:
                raise UnknownNameException(right_operand.identifier.line,
                                           right_operand.identifier.column,
                                           right_operand.value)
            right_operand = right_operand_definition

        return SimpleExpression(left_operand_definition, operator, right_operand)

    def __str__(self):
        return '{} {} {}'.format(self.left_operand, self.operator, self.right_operand)
