from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class SequenceDeclaration(Node):
    first = TokenType.SEQUENCE

    def __init__(self, children, parameters):
        super().__init__()
        self.children = children
        self.parameters = parameters

    @staticmethod
    def parse(parser):
        parser.parse_node(TokenType.SEQUENCE)

        parameters = parser.parse_node(NodeType.PARAMETERS) if parser.can_parse(NodeType.PARAMETERS) else None

        parser.parse_node(TokenType.CLIP_LEFT_BRACKET)

        children = []
        attribute = parser.parse_node(NodeType.ATTRIBUTE)
        children.append(attribute)

        while parser.can_parse(NodeType.ATTRIBUTE):
            attribute = parser.parse_node(NodeType.ATTRIBUTE)
            children.append(attribute)

        parser.parse_node(TokenType.CLIP_RIGHT_BRACKET)

        return SequenceDeclaration(children, parameters)
