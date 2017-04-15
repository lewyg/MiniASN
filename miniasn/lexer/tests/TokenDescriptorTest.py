from unittest import TestCase
from mock import patch

from miniasn.lexer.TokenDescriptor import TokenDescriptor
from miniasn.token.TokenType import TokenType


def test_qualifier(*args):
    pass


def test_acceptor(*args):
    pass


class TokenDescriptorTest(TestCase):
    def test_instance(self):
        token_descriptor = TokenDescriptor(TokenType.IDENTIFIER)

        self.assertIsInstance(token_descriptor, TokenDescriptor)
        self.assertEqual(token_descriptor.token_type, TokenType.IDENTIFIER)
        self.assertTrue(token_descriptor.required_space)

    def test_constructor_with_arguments(self):
        token_descriptor = TokenDescriptor(token_type=TokenType.IDENTIFIER,
                                           qualifier=test_qualifier,
                                           required_space=False,
                                           acceptor=test_acceptor)

        self.assertIsInstance(token_descriptor, TokenDescriptor)
        self.assertEqual(token_descriptor.token_type, TokenType.IDENTIFIER)
        self.assertFalse(token_descriptor.required_space)
        self.assertEqual(token_descriptor.qualifier, test_qualifier)
        self.assertEqual(token_descriptor.acceptor, test_acceptor)

    @patch('.'.join([__name__, test_qualifier.__name__]))
    def test_qualifier(self, mock):
        token_descriptor = TokenDescriptor(TokenType.IDENTIFIER, qualifier=test_qualifier)
        token_descriptor.qualifier()

        self.assertTrue(mock.called)

    @patch('.'.join([__name__, test_acceptor.__name__]))
    def test_acceptor(self, mock):
        token_descriptor = TokenDescriptor(TokenType.IDENTIFIER, acceptor=test_acceptor)
        token_descriptor.acceptor()

        self.assertTrue(mock.called)
