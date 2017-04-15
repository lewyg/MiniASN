from enum import Enum


class TokenType(Enum):
    EQUAL = '=='
    NOT_EQUAL = '!='
    GREATER = '>'
    LESS = '<'
    GREATER_OR_EQUAL = '>='
    LESS_OR_EQUAL = '<='
    ASSIGN = '::='
    PARAMETRIZE = '_'

    LEFT_BRACKET = '('
    RIGHT_BRACKET = ')'
    SQUARE_LEFT_BRACKET = '['
    SQUARE_RIGHT_BRACKET = ']'
    CLIP_LEFT_BRACKET = '{'
    CLIP_RIGHT_BRACKET = '}'

    UNIT = 'UINT'
    BITSTRING = 'BITSTRING'
    BOOL = 'BOOL'
    ARRAY = 'ARRAY'
    CHOICE = 'CHOICE'
    SEQUENCE = 'SEQUENCE'

    AND = 'AND'
    OR = 'OR'
    DEFAULT = 'DEFAULT'

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    NUMBER_LITERAL = '123'
    IDENTIFIER = 'ID'
