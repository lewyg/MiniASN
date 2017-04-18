from miniasn.ast.AndExpression import AndExpression
from miniasn.ast.ArrayDeclaration import ArrayDeclaration
from miniasn.ast.Attribute import Attribute
from miniasn.ast.Boolean import Boolean
from miniasn.ast.ChoiceAttribute import ChoiceAttribute
from miniasn.ast.ChoiceDeclaration import ChoiceDeclaration
from miniasn.ast.DataStructure import DataStructure
from miniasn.ast.Declaration import Declaration
from miniasn.ast.DeclaredType import DeclaredType
from miniasn.ast.Identifier import Identifier
from miniasn.ast.Number import Number
from miniasn.ast.OrExpression import OrExpression
from miniasn.ast.Parameter import Parameter
from miniasn.ast.Parameters import Parameters
from miniasn.ast.RelationalOperator import RelationalOperator
from miniasn.ast.SequenceDeclaration import SequenceDeclaration
from miniasn.ast.SimpleExpression import SimpleExpression
from miniasn.ast.SimpleType import SimpleType
from miniasn.ast.SimpleTypeDeclaration import SimpleTypeDeclaration
from miniasn.ast.Type import Type
from miniasn.ast.Value import Value
from miniasn.node.NodeType import NodeType
from miniasn.token.TokenType import TokenType


class Parser:
    __nodes = {
        NodeType.DATA_STRUCTURE: DataStructure,
        NodeType.DECLARATION: Declaration,
        NodeType.SEQUENCE_DECLARATION: SequenceDeclaration,
        NodeType.CHOICE_DECLARATION: ChoiceDeclaration,
        NodeType.CHOICE_ATTRIBUTE: ChoiceAttribute,
        NodeType.ARRAY_DECLARATION: ArrayDeclaration,
        NodeType.SIMPLE_TYPE_DECLARATION: SimpleTypeDeclaration,
        NodeType.PARAMETERS: Parameters,
        NodeType.PARAMETER: Parameter,
        NodeType.ATTRIBUTE: Attribute,
        NodeType.TYPE: Type,
        NodeType.SIMPLE_TYPE: SimpleType,
        NodeType.DECLARED_TYPE: DeclaredType,
        NodeType.OR_EXPRESSION: OrExpression,
        NodeType.AND_EXPRESSION: AndExpression,
        NodeType.SIMPLE_EXPRESSION: SimpleExpression,
        NodeType.RELATIONAL_OPERATOR: RelationalOperator,
        NodeType.VALUE: Value,
        NodeType.BOOLEAN: Boolean,
        NodeType.IDENTIFIER: Identifier,
        NodeType.NUMBER: Number,
    }

    def __init__(self, lexer):
        self.__lexer = lexer

    def parse(self):
        self.__advance()
        root = self.parse_node(NodeType.DATA_STRUCTURE)

        return root

    def parse_or_node_list(self, or_list):
        for node_type in or_list:
            if self.can_parse(node_type):
                return self.parse_node(node_type)

        raise Exception('Node not loaded from or list {}'.format(or_list))

    def can_parse(self, first):
        if first in TokenType:
            return self.__check_token_type(first)

        if first in NodeType:
            type = self.__nodes[first]
            return self.can_parse(type.first)

        for node_type in first:
            if self.can_parse(node_type):
                return True

        return False

    def parse_node(self, node_type):
        if node_type in NodeType:
            type = self.__nodes[node_type]
            node = type.parse(self)
        else:
            node = self.__parse_token(node_type)

        return node

    def __parse_token(self, token_type):
        token = self.__lexer.get_token()
        if self.__check_token_type(token_type):
            self.__advance()
        else:
            raise Exception('Unexpected token, expected: {}, {}\n line {} col {}'.format(token_type,
                                                                                         token.token_type, token.line,
                                                                                         token.column))
        return token

    def __advance(self):
        return self.__lexer.read_next_token()

    def __check_token_type(self, expected_type):
        token = self.__lexer.get_token()
        return token.token_type is expected_type if token else False
