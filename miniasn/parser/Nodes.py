from miniasn.ast.Arguments import Arguments
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
from miniasn.ast.SimpleTypeParametrized import SimpleTypeParametrized
from miniasn.ast.Type import Type
from miniasn.ast.Value import Value
from miniasn.node.NodeType import NodeType

nodes = {
    NodeType.DATA_STRUCTURE: DataStructure,
    NodeType.DECLARATION: Declaration,
    NodeType.SEQUENCE_DECLARATION: SequenceDeclaration,
    NodeType.CHOICE_DECLARATION: ChoiceDeclaration,
    NodeType.CHOICE_ATTRIBUTE: ChoiceAttribute,
    NodeType.ARRAY_DECLARATION: ArrayDeclaration,
    NodeType.ARGUMENTS: Arguments,
    NodeType.ATTRIBUTE: Attribute,
    NodeType.TYPE: Type,
    NodeType.SIMPLE_TYPE: SimpleType,
    NodeType.SIMPLE_TYPE_PARAMETRIZED: SimpleTypeParametrized,
    NodeType.DECLARED_TYPE: DeclaredType,
    NodeType.PARAMETERS: Parameters,
    NodeType.PARAMETER: Parameter,
    NodeType.OR_EXPRESSION: OrExpression,
    NodeType.AND_EXPRESSION: AndExpression,
    NodeType.SIMPLE_EXPRESSION: SimpleExpression,
    NodeType.RELATIONAL_OPERATOR: RelationalOperator,
    NodeType.VALUE: Value,
    NodeType.BOOLEAN: Boolean,
    NodeType.IDENTIFIER: Identifier,
    NodeType.NUMBER: Number,
}