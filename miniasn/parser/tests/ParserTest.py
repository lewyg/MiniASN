import io
import unittest

from miniasn.exceptions.ParserExceptions import UnexpectedTokenException, ArgumentsLoadException, NameInUseException, \
    NotDeclaredTypeException, ParserException, ParametersLoadException
from miniasn.lexer.Lexer import Lexer
from miniasn.parser.Parser import Parser
from miniasn.reader.FileReader import FileReader


class ParserTest(unittest.TestCase):
    def assertParserTest(self, data_structure, result):
        file = io.StringIO(data_structure)
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        self.assertEqual(''.join(str(tree).split()), ''.join(result.split()))

    def assertParserRaiseTest(self, data_structure, exception):
        file = io.StringIO(data_structure)
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)

        self.assertRaises(exception, parser.parse)

    def test_instance(self):
        lexer = Lexer(FileReader(io.StringIO('')))
        parser = Parser(lexer)

        self.assertIsInstance(parser, Parser)

    def test_simple_type_declaration_bitstring(self):
        data_structure = """bit16 ::= BITSTRING_16"""
        result = """bit16::=BITSTRING_16"""

        self.assertParserTest(data_structure, result)

    def test_simple_type_declaration_int(self):
        data_structure = """int16 ::= UINT_16"""
        result = """int16::=UINT_16"""

        self.assertParserTest(data_structure, result)

    def test_simple_type_declaration_bool(self):
        data_structure = """boole ::= BOOL"""
        result = """boole::=BOOL"""

        self.assertParserTest(data_structure, result)

    def test_simple_type_declaration_bool_parametrized(self):
        data_structure = """bool16 ::= BOOL_16"""
        exception = UnexpectedTokenException

        self.assertParserRaiseTest(data_structure, exception)

    def test_array_declaration(self):
        data_structure = """arr::=ARRAY[g]
                            {
                                a UINT
                            }"""
        result = """arr::=ARRAY[g]aUINT"""

        self.assertParserTest(data_structure, result)

    def test_array_declaration_no_argument(self):
        data_structure = """arr::=ARRAY[]
                            {
                                a UINT
                            }"""
        exception = UnexpectedTokenException

        self.assertParserRaiseTest(data_structure, exception)

    def test_array_declaration_too_many_arguments(self):
        data_structure = """arr::=ARRAY[c d e]
                            {
                                a UINT
                            }"""
        exception = ArgumentsLoadException

        self.assertParserRaiseTest(data_structure, exception)

    def test_array_declaration_name_in_use(self):
        data_structure = """arr::=ARRAY[a]
                            {
                                a UINT
                            }"""
        exception = NameInUseException

        self.assertParserRaiseTest(data_structure, exception)

    def test_array_declaration_not_declared_type(self):
        data_structure = """arr::=ARRAY[x]
                            {
                                a type
                            }"""
        exception = NotDeclaredTypeException

        self.assertParserRaiseTest(data_structure, exception)

    def test_choice_declaration(self):
        data_structure = """choi::=CHOICE[a]
                            {
                                UINT(a>0 AND a < 100)
                                BOOL(a == 0)
                                BITSTRING(DEFAULT)
                            }"""
        result = """choi::=CHOICE[a]UINT(a>0anda<100)BOOL(a==0)BITSTRING(DEFAULT)"""

        self.assertParserTest(data_structure, result)

    def test_choice_declaration_no_argument(self):
        data_structure = """choi::=CHOICE[]
                            {
                                UINT(DEFAULT)
                            }"""
        exception = UnexpectedTokenException

        self.assertParserRaiseTest(data_structure, exception)

    def test_choice_declaration_many_argument(self):
        data_structure = """choi::=CHOICE[a b]
                            {
                                UINT(DEFAULT)
                            }"""
        result = """choi::=CHOICE[ab]UINT(DEFAULT)"""

        self.assertParserTest(data_structure, result)

    def test_choice_declaration_no_default(self):
        data_structure = """choi ::= CHOICE[a]
                            {
                                UINT(a == 0)
                            }"""
        exception = ParserException

        self.assertParserRaiseTest(data_structure, exception)

    def test_choice_declaration_not_declared_type(self):
        data_structure = """choi ::= CHOICE[a]
                            {
                                type
                            }"""
        exception = NotDeclaredTypeException

        self.assertParserRaiseTest(data_structure, exception)

    def test_sequence_declaration(self):
        data_structure = """seq::= SEQUENCE[a b c] {
                                d UINT_9
                                e BOOL
                            }"""
        result = """seq::=SEQUENCE[abc]dUINT_9eBOOL"""

        self.assertParserTest(data_structure, result)

    def test_sequence_declaration_no_argument(self):
        data_structure = """seq::= SEQUENCE {
                                d UINT_9
                                e BOOL
                            }"""
        result = """seq::=SEQUENCEdUINT_9eBOOL"""

        self.assertParserTest(data_structure, result)

    def test_sequence_declaration_no_argument_with_bracket(self):
        data_structure = """seq::= SEQUENCE[] {
                                d UINT_9
                                e BOOL
                            }"""
        exception = UnexpectedTokenException

        self.assertParserRaiseTest(data_structure, exception)

    def test_sequence_declaration_name_in_use(self):
        data_structure = """seq::= SEQUENCE[a] {
                                a UINT_9
                            }"""
        exception = NameInUseException

        self.assertParserRaiseTest(data_structure, exception)

    def test_sequence_declaration_not_declared_type(self):
        data_structure = """seq::= SEQUENCE[a] {
                                a type
                            }"""
        exception = NotDeclaredTypeException

        self.assertParserRaiseTest(data_structure, exception)

    def test_sequence_declaration_with_choice_in(self):
        data_structure = """choi ::= CHOICE[a]
                            {
                                UINT(DEFAULT)
                            }
                            seq::= SEQUENCE[a] {
                                b choi[a]
                            }"""
        result = """choi::=CHOICE[a]UINT(DEFAULT)seq::=SEQUENCE[a]bchoi[a]"""

        self.assertParserTest(data_structure, result)

    def test_sequence_declaration_with_choice_many_args_in(self):
        data_structure = """choi ::= CHOICE[a b]
                            {
                                UINT(DEFAULT)
                            }
                            seq::= SEQUENCE[a] {
                                b choi[a 2]
                            }"""
        result = """choi::=CHOICE[ab]UINT(DEFAULT)seq::=SEQUENCE[a]bchoi[a2]"""

        self.assertParserTest(data_structure, result)

    def test_sequence_declaration_with_choice_many_args_in_missing_args(self):
        data_structure = """choi ::= CHOICE[a b]
                            {
                                UINT(DEFAULT)
                            }
                            seq::= SEQUENCE[a] {
                                b choi[a]
                            }"""
        exception = ParametersLoadException

        self.assertParserRaiseTest(data_structure, exception)

    def test_example_file(self):
        data_structure = """bit16 ::= BITSTRING_16
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
        result = """bit16::=BITSTRING_16
                    uint8::=UINT_8
                    b::=CHOICE[a]UINT(a>0anda<100)BOOL(a==0)bit16(a==100ora==110)BITSTRING(DEFAULT)
                    arr::=ARRAY[g]arrb[g]cb[3]
                    sss::=SEQUENCE[xfe]aUINT_9gb[a]
                    MojaSekwencjaSeq::=SEQUENCEauint8bsss[a11]"""

        self.assertParserTest(data_structure, result)
