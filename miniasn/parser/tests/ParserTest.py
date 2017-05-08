import unittest
import mock

from miniasn.parser.Parser import Parser
from miniasn.lexer.Lexer import Lexer


class ParserTest(unittest.TestCase):
    __next_token = None
    __current_token = None
    __parser = None

    def setUp(self):
        with mock.patch.object(Lexer, Lexer.read_next_token.__name__) as read_token:
            with mock.patch.object(Lexer, Lexer.get_token.__name__) as current_token:
                read_token.return_value = self.__next_token
                current_token.return_value = self.__current_token
                self.__parser = Parser(Lexer(None))

    def test_instance(self):
        self.assertIsInstance(self.__parser, Parser)
