from miniasn.exceptions.ParserExceptions import ParametersLoadException, NotDeclaredTypeException
from miniasn.node.Node import Node
from miniasn.node.NodeType import NodeType


class DeclaredType(Node):
    first = NodeType.IDENTIFIER

    def __init__(self, identifier, parameters, declaration):
        super().__init__()
        self.identifier = identifier
        self.parameters = parameters
        self.declaration = declaration

    @staticmethod
    def parse(parser, *args, **kwargs):
        identifier = parser.parse_node(NodeType.IDENTIFIER)

        declaration = parser.get_declared_type(identifier)

        if not declaration:
            raise NotDeclaredTypeException(identifier.identifier.line,
                                           identifier.identifier.column,
                                           identifier.value())

        required_parameters = declaration.declaration.required_arguments()

        parameters = parser.parse_node(NodeType.PARAMETERS) if parser.can_parse(NodeType.PARAMETERS) else None

        loaded_parameters = len(parameters.parameters) if parameters is not None else 0

        if loaded_parameters != required_parameters:
            raise ParametersLoadException(identifier.identifier.line,
                                          identifier.identifier.column,
                                          loaded_parameters,
                                          required_parameters,
                                          identifier.value())

        return DeclaredType(identifier, parameters, declaration)

    def __str__(self):
        return '{}{}'.format(self.identifier, self.parameters or '')
