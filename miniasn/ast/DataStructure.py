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
        while parser.can_parse(NodeType.DECLARATION):
            node = parser.parse_node(NodeType.DECLARATION)
            children.append(node)

        return DataStructure(children)
