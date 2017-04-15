from miniasn.token.TokenType import TokenType

from miniasn.token.TokenDescriptor import TokenDescriptor


class Tokenizer:
    __token_descriptors = [
        TokenDescriptor(token_type=TokenType.EQUAL,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.NOT_EQUAL,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.GREATER,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.LESS,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.GREATER_OR_EQUAL,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.LESS_OR_EQUAL,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.ASSIGN,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.PARAMETRIZE,
                        required_space=False),

        TokenDescriptor(token_type=TokenType.LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.RIGHT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.SQUARE_LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.SQUARE_RIGHT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.CLIP_LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(token_type=TokenType.CLIP_RIGHT_BRACKET,
                        required_space=False),

        TokenDescriptor(token_type=TokenType.UNIT),
        TokenDescriptor(token_type=TokenType.BITSTRING),
        TokenDescriptor(token_type=TokenType.BOOL),
        TokenDescriptor(token_type=TokenType.ARRAY),
        TokenDescriptor(token_type=TokenType.CHOICE),
        TokenDescriptor(token_type=TokenType.SEQUENCE),

        TokenDescriptor(token_type=TokenType.AND),
        TokenDescriptor(token_type=TokenType.OR),
        TokenDescriptor(token_type=TokenType.DEFAULT),

        TokenDescriptor(token_type=TokenType.TRUE),
        TokenDescriptor(token_type=TokenType.FALSE),

        # non-standard TokenDescriptions always at end!
        TokenDescriptor(token_type=TokenType.NUMBER_LITERAL,
                        qualifier=lambda char, *args: char.isdigit(),
                        acceptor=lambda word, *args: word.isdigit()),
        TokenDescriptor(token_type=TokenType.IDENTIFIER,
                        qualifier=lambda char, char_position, *args: char.isalnum() if char_position else char.isalpha(),
                        acceptor=lambda word, *args: word.isalnum()),
    ]

    def __init__(self):
        self.__tokens_required_space = [token_descriptor for token_descriptor in self.__token_descriptors
                                        if token_descriptor.required_space]

    @property
    def descriptors(self):
        return self.__token_descriptors

    @property
    def tokens_required_space(self):
        return self.__tokens_required_space
