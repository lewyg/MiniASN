from miniasn.exceptions.ParserExceptions import ParserException
from miniasn.exceptions.ReaderException import ArgumentsNumberException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class ChoiceDeclaration(Node):
    first = TokenType.CHOICE

    def __init__(self, attributes, arguments):
        super().__init__()
        self.attributes = attributes
        self.arguments = arguments

    @staticmethod
    def parse(parser, *args, **kwargs):
        parser.parse_node(TokenType.CHOICE)

        arguments = parser.parse_node(NodeType.ARGUMENTS, type_name='CHOICE')

        bracket = parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        attributes = []
        while True:
            attribute = parser.parse_node(NodeType.CHOICE_ATTRIBUTE)
            attributes.append(attribute)
            if attribute.is_default() or not parser.can_parse(NodeType.CHOICE_ATTRIBUTE):
                break

        if not attribute.is_default():
            raise ParserException(bracket.line, bracket.column, "Last choice attribute must be DEFAULT")

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return ChoiceDeclaration(attributes, arguments.arguments)

    def required_arguments(self):
        return len(self.arguments) if self.arguments else 0

    def get_correct_attribute(self):
        for attribute in self.attributes:
            if attribute.check_if_true():
                return attribute

    def read_value(self, reader, arguments=None, *args, **kwargs):
        if len(arguments) != len(self.arguments):
            raise ArgumentsNumberException("CHOICE", self.required_arguments(), len(arguments))

        arguments = arguments

        result = ''
        i = 0
        for argument in arguments:
            self.arguments[i].value = argument
            i += 1

        attribute = self.get_correct_attribute()
        result += attribute.read_value(reader, *args, **kwargs).replace('\n', '\n    ')

        return result

    def __str__(self):
        arguments = '{}'.format(' '.join([str(argument) for argument in self.arguments]))

        return 'CHOICE[{}]\n\t{}'.format(arguments, '\n\t'.join([str(attribute) for attribute in self.attributes]))
