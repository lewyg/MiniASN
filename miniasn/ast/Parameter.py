from miniasn.exceptions.ParserExceptions import UnknownNameException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class Parameter(Node):
    first = [NodeType.IDENTIFIER,
             NodeType.NUMBER]

    def __init__(self, parameter, value):
        super().__init__()
        self.parameter = parameter
        self.value = value

    @staticmethod
    def parse(parser, *args, **kwargs):
        parameter = parser.parse_or_node_list([NodeType.IDENTIFIER,
                                               NodeType.NUMBER])
        if type(parameter.value) == int:
            return Parameter(parameter, parameter.value)

        parameter_definition = parser.check_if_name_exists(parser.local_names, parameter)
        if not parameter_definition:
            raise UnknownNameException(parameter.identifier.line,
                                       parameter.identifier.column,
                                       parameter.value)
        return Parameter(parameter, parameter_definition.value)

    def __str__(self):
        return str(self.parameter.value)
