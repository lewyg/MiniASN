class TokenType:
    OPERATOR = {
        '==': 'EQUAL',
        '!=': 'NOT_EQUAL',
        '>': 'GREATER',
        '<': 'LESS',
        '<=': 'NOT_GREATER',
        '>=': 'NOT_LESS',
        '::=': 'ASSIGN',
        '_': 'PARAMETRIZE'
    }

    PARENTHESIS = {
        '[': 'SQUARE_LEFT',
        ']': 'SQUARE_RIGHT',
        '{': 'CLIP_LEFT',
        '}': 'CLIP_RIGHT',
        '(': 'NORMAL_LEFT',
        ')': 'NORMAL_RIGHT'
    }

    DATA_TYPE = {
        'UINT': 'UINT',
        'BITSTRING': 'BITSTRING',
        'BOOL': 'BOOL',
        'ARRAY': 'ARRAY',
        'CHOICE': 'CHOICE',
        'SEQUENCE': 'SEQUENCE'
    }

    EXPRESSION_CONTROLLER = {
        'AND': 'AND',
        'OR': 'OR',
        'DEFAULT': 'DEFAULT'
    }

    IDENTIFIER = {
        'NAME': 'IDENTIFIER'
    }

    NUMBER = {
        'NAME': 'NUMBER'
    }
