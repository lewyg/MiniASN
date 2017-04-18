from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class Parameter(Node):
    first = [NodeType.IDENTIFIER,
             NodeType.NUMBER]

    def __init__(self, parameter):
        super().__init__()
        self.parameter = parameter

    @staticmethod
    def parse(parser):
        parameter = parser.parse_or_node_list([NodeType.IDENTIFIER,
                                               NodeType.NUMBER])

        return Parameter(parameter)

    def __str__(self):
        return str(self.parameter)
