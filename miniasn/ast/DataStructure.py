from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class DataStructure(Node):
    first = NodeType.DECLARATION

    def __init__(self, children):
        super().__init__()
        self.children = children

    @staticmethod
    def parse(parser):
        children = []
        while not parser.end_of_file():
            node = parser.parse_node(NodeType.DECLARATION)
            children.append(node)

        return DataStructure(children)

    def __str__(self):
        result = ''
        for declaration in self.children:
            result += '{}\n\n'.format(declaration)

        return result[:-2]
