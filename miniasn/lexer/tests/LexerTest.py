from unittest import TestCase

from miniasn.exceptions.LexerExceptions import RequiredSpaceException, UndefinedSymbolException
from miniasn.lexer.Lexer import Lexer
from miniasn.lexer.tests.FileReaderMocked import FileReaderMocked
from miniasn.token.Token import Token
from miniasn.token.TokenType import TokenType


class LexerTest(TestCase):
    def test_instance(self):
        lexer = Lexer(FileReaderMocked(''))

        self.assertIsInstance(lexer, Lexer)

    def test_get_token(self):
        lexer = Lexer(FileReaderMocked('id'))
        token = lexer.get_token()

        self.assertIsInstance(token, Token)
        self.assertEqual(token.token_type, TokenType.IDENTIFIER)
        self.assertEqual(token.token_value, 'id')

    def test_get_token_with_white_space_at_beginning(self):
        lexer = Lexer(FileReaderMocked('        \t\n id'))
        token = lexer.get_token()

        self.assertIsInstance(token, Token)
        self.assertEqual(token.token_type, TokenType.IDENTIFIER)
        self.assertEqual(token.token_value, 'id')

    def test_get_token_when_no_token(self):
        lexer = Lexer(FileReaderMocked(''))
        token = lexer.get_token()

        self.assertIsNone(token)

    def test_get_token_all_tokens(self):
        for token_type in TokenType:
            with self.subTest(token=token_type):
                lexer = Lexer(FileReaderMocked(token_type.value))
                token = lexer.get_token()

                self.assertEqual(token.token_type, token_type)
                self.assertEqual(token.token_value, token_type.value)

    def test_token_identifier(self):
        lexer = Lexer(FileReaderMocked('id'))
        token = lexer.get_token()

        self.assertEqual(token.token_type, TokenType.IDENTIFIER)

    def test_token_identifier_with_digits_at_end(self):
        lexer = Lexer(FileReaderMocked('id123'))
        token = lexer.get_token()

        self.assertEqual(token.token_type, TokenType.IDENTIFIER)

    def test_token_identifier_with_digits_at_beginning(self):
        lexer = Lexer(FileReaderMocked('123ar'))

        self.assertRaises(RequiredSpaceException, lexer.get_token)

    def test_token_identifier_with_non_alphanum_chars(self):
        lexer = Lexer(FileReaderMocked('id@as'))
        token = lexer.get_token()

        self.assertEqual(token.token_type, TokenType.IDENTIFIER)
        self.assertEqual(token.token_value, 'id')
        self.assertRaises(UndefinedSymbolException, lexer.get_token)

    def test_token_number(self):
        lexer = Lexer(FileReaderMocked('123'))
        token = lexer.get_token()

        self.assertEqual(token.token_type, TokenType.NUMBER_LITERAL)

    def test_two_token_with_required_space_without_space(self):
        lexer = Lexer(FileReaderMocked('123asd'))

        self.assertRaises(RequiredSpaceException, lexer.get_token)

    def test_two_token_with_required_space(self):
        lexer = Lexer(FileReaderMocked('123 asd'))
        token_1 = lexer.get_token()
        token_2 = lexer.get_token()

        self.assertEqual(token_1.token_type, TokenType.NUMBER_LITERAL)
        self.assertEqual(token_1.token_value, '123')
        self.assertEqual(token_2.token_type, TokenType.IDENTIFIER)
        self.assertEqual(token_2.token_value, 'asd')

    def test_two_token_without_required_space_without_space(self):
        lexer = Lexer(FileReaderMocked('[]'))
        token_1 = lexer.get_token()
        token_2 = lexer.get_token()

        self.assertEqual(token_1.token_type, TokenType.SQUARE_LEFT_BRACKET)
        self.assertEqual(token_1.token_value, TokenType.SQUARE_LEFT_BRACKET.value)
        self.assertEqual(token_2.token_type, TokenType.SQUARE_RIGHT_BRACKET)
        self.assertEqual(token_2.token_value, TokenType.SQUARE_RIGHT_BRACKET.value)

    def test_two_token_without_required_space_with_space(self):
        lexer = Lexer(FileReaderMocked(' [ ] '))
        token_1 = lexer.get_token()
        token_2 = lexer.get_token()

        self.assertEqual(token_1.token_type, TokenType.SQUARE_LEFT_BRACKET)
        self.assertEqual(token_1.token_value, TokenType.SQUARE_LEFT_BRACKET.value)
        self.assertEqual(token_2.token_type, TokenType.SQUARE_RIGHT_BRACKET)
        self.assertEqual(token_2.token_value, TokenType.SQUARE_RIGHT_BRACKET.value)

    def test_undefined_symbol_after_token(self):
        lexer = Lexer(FileReaderMocked('123@'))
        token = lexer.get_token()

        self.assertEqual(token.token_type, TokenType.NUMBER_LITERAL)
        self.assertRaises(UndefinedSymbolException, lexer.get_token)

    def test_undefined_symbol_after_end_of_token_which_may_be_sub_token(self):
        lexer = Lexer(FileReaderMocked('<@'))
        token = lexer.get_token()

        self.assertEqual(token.token_type, TokenType.LESS)
        self.assertRaises(UndefinedSymbolException, lexer.get_token)