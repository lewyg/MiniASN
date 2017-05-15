import unittest

import io

from miniasn.exceptions.ParserExceptions import UnexpectedTokenException, ArgumentsLoadException, NameInUseException, \
    NotDeclaredTypeException, ParserException
from miniasn.parser.Parser import Parser
from miniasn.lexer.Lexer import Lexer
from miniasn.reader.FileReader import FileReader


class ParserTest(unittest.TestCase):
    def test_instance(self):
        lexer = Lexer(FileReader(io.StringIO('')))
        parser = Parser(lexer)

        self.assertIsInstance(parser, Parser)

    def test_simple_type_declaration_bitstring(self):
        file = io.StringIO(
"""bit16 ::= BITSTRING_16"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        tree = parser.parse()

        self.assertEqual(str(tree),
"""bit16 ::= BITSTRING_16"""
                         )

    def test_simple_type_declaration_int(self):
        file = io.StringIO(
"""int16 ::= UINT_16"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        tree = parser.parse()

        self.assertEqual(str(tree),
"""int16 ::= UINT_16"""
                         )

    def test_simple_type_declaration_bool(self):
        file = io.StringIO(
"""boole ::= BOOL"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        tree = parser.parse()

        self.assertEqual(str(tree),
"""boole ::= BOOL"""
                         )

    def test_simple_type_declaration_bool_parametrized(self):
        file = io.StringIO(
"""bool16 ::= BOOL_16"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(UnexpectedTokenException, parser.parse)

    def test_array_declaration(self):
        file = io.StringIO(
"""arr::=ARRAY[g]
{
    a UINT
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        tree = parser.parse()

        self.assertEqual(str(tree),
"""arr ::= ARRAY[g]
	a UINT"""
                         )

    def test_array_declaration_no_argument(self):
        file = io.StringIO(
"""arr::=ARRAY[]
{
    a UINT
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(UnexpectedTokenException, parser.parse)

    def test_array_declaration_too_many_arguments(self):
        file = io.StringIO(
            """arr::=ARRAY[c d e]
            {
                a UINT
            }"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(ArgumentsLoadException, parser.parse)

    def test_array_declaration_name_in_use(self):
        file = io.StringIO(
            """arr::=ARRAY[a]
            {
                a UINT
            }"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(NameInUseException, parser.parse)

    def test_array_declaration_not_declared_type(self):
        file = io.StringIO(
            """arr::=ARRAY[x]
            {
                a type
            }"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(NotDeclaredTypeException, parser.parse)

    def test_choice_declaration(self):
        file = io.StringIO(
"""choi::=CHOICE[a]
{
    UINT(a>0 AND a < 100)
    BOOL(a == 0)
    BITSTRING(DEFAULT)
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        tree = parser.parse()

        self.assertEqual(str(tree),
"""choi ::= CHOICE[a]
	UINT(a > 0 and a < 100)
	BOOL(a == 0)
	BITSTRING(DEFAULT)"""
                         )

    def test_choice_declaration_no_argument(self):
        file = io.StringIO(
"""choi::=CHOICE[]
{
    UINT(DEFAULT)
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(UnexpectedTokenException, parser.parse)

    def test_choice_declaration_no_default(self):
        file = io.StringIO(
"""choi ::= CHOICE[a]
{
    UINT(a == 0)
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(ParserException, parser.parse)

    def test_choice_declaration_not_declared_type(self):
        file = io.StringIO(
"""choi ::= CHOICE[a]
{
    a type
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(NotDeclaredTypeException, parser.parse)

    def test_sequence_declaration(self):
        file = io.StringIO(
"""seq::= SEQUENCE[a b c] {
    d UINT_9
    e BOOL
}"""
            )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        tree = parser.parse()

        self.assertEqual(str(tree),
"""seq ::= SEQUENCE[a b c]
	d UINT_9
	e BOOL"""
                         )

    def test_sequence_declaration_no_argument(self):
        file = io.StringIO(
"""seq::= SEQUENCE {
    d UINT_9
    e BOOL
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        tree = parser.parse()

        self.assertEqual(str(tree),
"""seq ::= SEQUENCE
	d UINT_9
	e BOOL"""
                         )

    def test_sequence_declaration_no_argument_with_bracket(self):
        file = io.StringIO(
"""seq::= SEQUENCE[] {
    d UINT_9
    e BOOL
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(UnexpectedTokenException, parser.parse)

    def test_sequence_declaration_name_in_use(self):
        file = io.StringIO(
"""seq::= SEQUENCE[a] {
    a UINT_9
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(NameInUseException, parser.parse)

    def test_sequence_declaration_not_declared_type(self):
        file = io.StringIO(
"""seq::= SEQUENCE[a] {
    a type
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(NotDeclaredTypeException, parser.parse)

    def test_example_file(self):
        file = io.StringIO(
"""bit16 ::= BITSTRING_16
uint8 ::= UINT_8

b::=CHOICE[a]
{
    UINT(a>0 AND a < 100)
    BOOL(a == 0)
    bit16(a == 100 OR a == 110)
    BITSTRING(DEFAULT)
}

arr::=ARRAY[g]
{
    arr b[g]
    c b[3]
}

sss::= SEQUENCE[x f e] {
    a UINT_9
    g b[a]
}

MojaSekwencjaSeq::= SEQUENCE {
    a uint8
    b sss[a 1 1]
}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        tree = parser.parse()

        self.assertEqual(str(tree),
"""bit16 ::= BITSTRING_16

uint8 ::= UINT_8

b ::= CHOICE[a]
	UINT(a > 0 and a < 100)
	BOOL(a == 0)
	bit16(a == 100 or a == 110)
	BITSTRING(DEFAULT)

arr ::= ARRAY[g]
	arr b[g]
	c b[3]

sss ::= SEQUENCE[x f e]
	a UINT_9
	g b[a]

MojaSekwencjaSeq ::= SEQUENCE
	a uint8
	b sss[a 1 1]"""
                         )
