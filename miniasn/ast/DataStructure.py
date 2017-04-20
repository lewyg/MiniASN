from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class DataStructure(Node):
    first = NodeType.DECLARATION

    def __init__(self, declarations):
        super().__init__()
        self.declarations = declarations

    @staticmethod
    def parse(parser, *args, **kwargs):
        declarations = []
        while not parser.end_of_file():
            declaration = parser.parse_node(NodeType.DECLARATION)
            declarations.append(declaration)

        return DataStructure(declarations)

    def __str__(self):
        result = ''
        for declaration in self.declarations:
            result += '{}\n\n'.format(declaration)

        return result[:-2]
