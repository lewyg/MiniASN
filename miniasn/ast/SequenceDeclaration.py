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

        attribute = parser.parse_node(NodeType.ATTRIBUTE)
        attributes.append(attribute)

        while parser.can_parse(NodeType.ATTRIBUTE):
            attribute = parser.parse_node(NodeType.ATTRIBUTE)
            attributes.append(attribute)

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return SequenceDeclaration(attributes, arguments)

    def __str__(self):
        result = 'SEQUENCE{}'.format(self.arguments)
        for attribute in self.attributes:
            result += '\n\t{}'.format(attribute)

        return result
