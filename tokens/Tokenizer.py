from tokens.TokenDescriptor import TokenDescriptor
from tokens.TokenType import TokenType


class Tokenizer:
    # (token_type, qualifier, required_space, acceptor)
    __token_descriptors = [
        TokenDescriptor(TokenType.EQUAL,
                        required_space=False),
        TokenDescriptor(TokenType.NOT_EQUAL,
                        required_space=False),
        TokenDescriptor(TokenType.GREATER,
                        required_space=False),
        TokenDescriptor(TokenType.LESS,
                        required_space=False),
        TokenDescriptor(TokenType.GREATER_OR_EQUAL,
                        required_space=False),
        TokenDescriptor(TokenType.LESS_OR_EQUAL,
                        required_space=False),
        TokenDescriptor(TokenType.ASSIGN,
                        required_space=False),
        TokenDescriptor(TokenType.PARAMETRIZE,
                        required_space=False),

        TokenDescriptor(TokenType.LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(TokenType.RIGHT_BRACKET,
                        required_space=False),
        TokenDescriptor(TokenType.SQUARE_LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(TokenType.SQUARE_RIGHT_BRACKET,
                        required_space=False),
        TokenDescriptor(TokenType.CLIP_LEFT_BRACKET,
                        required_space=False),
        TokenDescriptor(TokenType.CLIP_RIGHT_BRACKET,
                        required_space=False),

        TokenDescriptor(TokenType.UNIT),
        TokenDescriptor(TokenType.BITSTRING),
        TokenDescriptor(TokenType.BOOL),
        TokenDescriptor(TokenType.ARRAY),
        TokenDescriptor(TokenType.CHOICE),
        TokenDescriptor(TokenType.SEQUENCE),

        TokenDescriptor(TokenType.AND),
        TokenDescriptor(TokenType.OR),
        TokenDescriptor(TokenType.DEFAULT),

        TokenDescriptor(TokenType.TRUE),
        TokenDescriptor(TokenType.FALSE),

        # non-standard TokenDescriptions always at end!
        TokenDescriptor(TokenType.NUMBER_LITERAL,
                        qualifier=lambda char, *args: char.isdigit(),
                        acceptor=lambda word, *args: word.isdigit()),
        TokenDescriptor(TokenType.IDENTIFIER,
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
