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

        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)
        argument = parser.parse_node(NodeType.IDENTIFIER)
        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        attributes = [parser.parse_node(NodeType.CHOICE_ATTRIBUTE)]

        while parser.can_parse(NodeType.CHOICE_ATTRIBUTE):
            attribute = parser.parse_node(NodeType.CHOICE_ATTRIBUTE)
            attributes.append(attribute)
            if attribute.is_default():
                break

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return ChoiceDeclaration(attributes, [argument])

    def required_arguments(self):
        return 1

    def __str__(self):
        return 'CHOICE[{}]\n\t{}'.format(self.arguments[0],
                                         '\n\t'.join([str(attribute) for attribute in self.attributes]))
