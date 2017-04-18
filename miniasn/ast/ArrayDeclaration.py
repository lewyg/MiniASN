from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class ArrayDeclaration(Node):
    first = TokenType.ARRAY

    def __init__(self, children, parameter):
        super().__init__()
        self.children = children
        self.parameter = parameter

    @staticmethod
    def parse(parser):
        parser.parse_node(TokenType.ARRAY)

        parser.parse_node(TokenType.SQUARE_LEFT_BRACKET)
        parameter = parser.parse_node(NodeType.PARAMETER)
        parser.parse_node(TokenType.SQUARE_RIGHT_BRACKET)

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        children = []

        attribute = parser.parse_node(NodeType.ATTRIBUTE)
        children.append(attribute)

        while parser.can_parse(NodeType.ATTRIBUTE):
            attribute = parser.parse_node(NodeType.ATTRIBUTE)
            children.append(attribute)

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return ArrayDeclaration(children, parameter)

    def __str__(self):
        result = 'ARRAY[{}]'.format(self.parameter)
        for attribute in self.children:
            result += '\n\t{}'.format(attribute)

        return result
