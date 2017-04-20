from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class ChoiceDeclaration(Node):
    first = TokenType.CHOICE

    def __init__(self, choice_attributes, arguments):
        super().__init__()
        self.choice_attributes = choice_attributes
        self.arguments = arguments

    @staticmethod
    def parse(parser, *args, **kwargs):
        parser.parse_node(TokenType.CHOICE)

        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)
        arguments = parser.parse_node(NodeType.IDENTIFIER)
        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        choice_attributes = [parser.parse_node(NodeType.CHOICE_ATTRIBUTE)]

        while parser.can_parse(NodeType.CHOICE_ATTRIBUTE):
            choice_attribute = parser.parse_node(NodeType.CHOICE_ATTRIBUTE)
            choice_attributes.append(choice_attribute)
            if choice_attribute.is_default():
                break

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return ChoiceDeclaration(choice_attributes, arguments)

    def __str__(self):
        return 'CHOICE[{}]\n\t{}'.format(self.arguments,
                                         '\n\t'.join([str(attribute) for attribute in self.choice_attributes]))
