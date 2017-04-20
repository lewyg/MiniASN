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

        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)
        arguments = parser.parse_node(NodeType.IDENTIFIER)
        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        attributes = []

        attribute = parser.parse_node(NodeType.ATTRIBUTE)
        attributes.append(attribute)

        while parser.can_parse(NodeType.ATTRIBUTE):
            attribute = parser.parse_node(NodeType.ATTRIBUTE)
            attributes.append(attribute)

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return ArrayDeclaration(attributes, arguments)

    def __str__(self):
        result = 'ARRAY[{}]'.format(self.arguments)
        for attribute in self.attributes:
            result += '\n\t{}'.format(attribute)

        return result
