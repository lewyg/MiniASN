from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class ChoiceDeclaration(Node):
    first = TokenType.CHOICE

    def __init__(self, children, parameter):
        super().__init__()
        self.children = children
        self.parameter = parameter

    @staticmethod
    def parse(parser):
        parser.parse_node(TokenType.CHOICE)

        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)
        parameter = parser.parse_node(NodeType.PARAMETER)
        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        children = []
        choice_attribute = parser.parse_node(NodeType.CHOICE_ATTRIBUTE)
        children.append(choice_attribute)

        while parser.can_parse(NodeType.CHOICE_ATTRIBUTE):
            choice_attribute = parser.parse_node(NodeType.CHOICE_ATTRIBUTE)
            children.append(choice_attribute)
            if choice_attribute.is_default():
                break

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return ChoiceDeclaration(children, parameter)

    def __str__(self):
        result = 'CHOICE[{}]'.format(self.parameter)
        for attribute in self.children:
            result += '\n\t{}'.format(attribute)

        return result
