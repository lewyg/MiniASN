from miniasn.exceptions.ParserExceptions import ParametersLoadException, NotDeclaredTypeException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class DeclaredType(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, type_name, parameters, declaration):
        super().__init__()
        self.type_name = type_name
        self.parameters = parameters
        self.declaration = declaration

    @staticmethod
    def parse(parser, *args, **kwargs):
        type_name = parser.parse_node(NodeType.IDENTIFIER)

        declaration = parser.check_if_name_exists(parser.declared_types, type_name)

        if not declaration:
            raise NotDeclaredTypeException(type_name.identifier.line,
                                           type_name.identifier.column,
                                           type_name.value)

        required_parameters = declaration.declaration.required_arguments()

        parameters = parser.parse_node(NodeType.PARAMETERS) if parser.can_parse(NodeType.PARAMETERS) else None

        loaded_parameters = len(parameters.parameters) if parameters is not None else 0

        if loaded_parameters != required_parameters:
            raise ParametersLoadException(type_name.identifier.line,
                                          type_name.identifier.column,
                                          loaded_parameters,
                                          required_parameters,
                                          type_name.value)

        return DeclaredType(type_name, parameters, declaration)

    def __str__(self):
        return '{}{}'.format(self.type_name, self.parameters or '')
