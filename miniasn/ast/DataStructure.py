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
            declarations.append(parser.parse_node(NodeType.DECLARATION))

        return DataStructure(declarations)

    def __str__(self):
        return '\n\n'.join([str(declaration) for declaration in self.declarations])
