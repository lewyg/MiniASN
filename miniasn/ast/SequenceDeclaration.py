from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class SequenceDeclaration(Node):
    first = TokenType.SEQUENCE

    def __init__(self, attributes, parameters):
        super().__init__()
        self.attributes = attributes
        self.parameters = parameters

    @staticmethod
    def parse(parser, *args, **kwargs):
        parser.parse_node(TokenType.SEQUENCE)

        parameters = parser.parse_node(NodeType.PARAMETERS) if parser.can_parse(NodeType.PARAMETERS) else None

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        attributes = []

        attribute = parser.parse_node(NodeType.ATTRIBUTE)
        attributes.append(attribute)

        while parser.can_parse(NodeType.ATTRIBUTE):
            attribute = parser.parse_node(NodeType.ATTRIBUTE)
            attributes.append(attribute)

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return SequenceDeclaration(attributes, parameters)

    def __str__(self):
        result = 'SEQUENCE{}'.format(self.parameters)
        for attribute in self.attributes:
            result += '\n\t{}'.format(attribute)

        return result
