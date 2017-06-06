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
            parser.local_names = []
            declaration = parser.parse_node(NodeType.DECLARATION)
            declarations.append(declaration)
            parser.declared_types.append(declaration)

        return DataStructure(declarations)

    def read_value(self, reader, name, arguments, *args, **kwargs):
        for declaration in self.declarations:
            if declaration.identifier.value == name:
                return "{}{} = {}".format(name, arguments or '',
                                          declaration.read_value(reader, arguments=arguments, *args, **kwargs))

        return 'Structure {} not found!'.format(name)

    def __str__(self):
        return '\n\n'.join([str(declaration) for declaration in self.declarations])
