from unittest import TestCase

from miniasn.token.Token import Token
from miniasn.token.TokenType import TokenType


class TokenTest(TestCase):
    def test_instance(self):
        token = Token(TokenType.IDENTIFIER, 'id', 1, 2)

        self.assertIsInstance(token, Token)
        self.assertEqual(token.token_type, TokenType.IDENTIFIER)
        self.assertEqual(token.token_value, 'id')
        self.assertEqual(token.line, 1)
        self.assertEqual(token.column, 2)

    def test_repr(self):
        token = Token(TokenType.IDENTIFIER, 'id', 0, 0)

        self.assertEqual(str(token), 'id')
