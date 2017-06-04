from miniasn.exceptions.ParserExceptions import NameInUseException
from miniasn.exceptions.ReaderException import ArgumentsNumberException, ArgumentTypeException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class ArrayDeclaration(Node):
    first = TokenType.ARRAY

    def __init__(self, attributes, arguments):
        super().__init__()
        self.attributes = attributes
        self.arguments = arguments

    @staticmethod
    def parse(parser, *args, **kwargs):
        parser.parse_node(TokenType.ARRAY)

        arguments = parser.parse_node(NodeType.ARGUMENTS, required_arguments=1, type_name='ARRAY')

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        attributes = []
        while True:
            attribute = parser.parse_node(NodeType.ATTRIBUTE)
            attributes.append(attribute)

            if parser.check_if_name_exists(parser.local_names, attribute.identifier):
                raise NameInUseException(attribute.identifier.identifier.line,
                                         attribute.identifier.identifier.column,
                                         attribute.identifier.value)

            parser.local_names.append(attribute)

            if not parser.can_parse(NodeType.ATTRIBUTE):
                break

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return ArrayDeclaration(attributes, arguments.arguments)

    def required_arguments(self):
        return 1

    def read_value(self, reader, arguments, *args, **kwargs):
        if len(arguments) != 1:
            raise ArgumentsNumberException("ARRAY", self.required_arguments(), len(arguments))

        argument = arguments[0]

        try:
            if type(argument) is not int:
                argument = int(argument)
        except:
            raise ArgumentTypeException(int, type(argument))

        self.arguments[0].value = argument

        result = "["
        for i in range(argument):
            result += "\n {"
            for attribute in self.attributes:
                result += "\n  "
                result += attribute.read_value(reader, *args, **kwargs).replace('\n', '\n    ')
                result += ","
            result += "\n },"
        result += "\n]"

        return result

    def __str__(self):
        return 'ARRAY[{}]\n\t{}'.format(self.arguments[0],
                                        '\n\t'.join([str(attribute) for attribute in self.attributes]))
