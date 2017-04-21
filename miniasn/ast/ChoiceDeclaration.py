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

        arguments = parser.parse_node(NodeType.ARGUMENTS, required_arguments=1)

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        attributes = []
        while True:
            attribute = parser.parse_node(NodeType.CHOICE_ATTRIBUTE)
            attributes.append(attribute)
            if attribute.is_default() or not parser.can_parse(NodeType.CHOICE_ATTRIBUTE):
                break

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return ChoiceDeclaration(attributes, arguments.arguments)

    def required_arguments(self):
        return 1

    def __str__(self):
        return 'CHOICE[{}]\n\t{}'.format(self.arguments[0],
                                         '\n\t'.join([str(attribute) for attribute in self.attributes]))
