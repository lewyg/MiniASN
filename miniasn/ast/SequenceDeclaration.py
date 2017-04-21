from miniasn.exceptions.ParserExceptions import NameInUseException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class SequenceDeclaration(Node):
    first = TokenType.SEQUENCE

    def __init__(self, attributes, arguments):
        super().__init__()
        self.attributes = attributes
        self.arguments = arguments

    @staticmethod
    def parse(parser, *args, **kwargs):
        parser.parse_node(TokenType.SEQUENCE)

        arguments = parser.parse_node(NodeType.ARGUMENTS) if parser.can_parse(NodeType.ARGUMENTS) else None

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        attributes = []
        while True:
            attribute = parser.parse_node(NodeType.ATTRIBUTE)
            attributes.append(attribute)

            if parser.get_local_name(attribute.identifier):
                raise NameInUseException(attribute.identifier.identifier.line,
                                         attribute.identifier.identifier.column,
                                         attribute.identifier.value)

            parser.local_names.append(attribute)

            if not parser.can_parse(NodeType.ATTRIBUTE):
                break

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return SequenceDeclaration(attributes, arguments.arguments if arguments else [])

    def required_arguments(self):
        return len(self.arguments) if self.arguments else 0

    def __str__(self):
        arguments = '[{}]'.format(' '.join([str(argument) for argument in self.arguments]))

        return 'SEQUENCE{}\n\t{}'.format(arguments if self.arguments else '',
                                         '\n\t'.join([str(attribute) for attribute in self.attributes]))
