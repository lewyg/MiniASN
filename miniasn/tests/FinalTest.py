import io

from unittest import TestCase

from miniasn.lexer.Lexer import Lexer
from miniasn.parser.Parser import Parser
from miniasn.reader.ByteReader import ByteReader
from miniasn.reader.FileReader import FileReader


class FinalTest(TestCase):
    def test_simple_type_declaration_bool(self):
        file = io.StringIO(
            """bool ::= BOOL"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('00')))

        self.assertEqual(tree.read_value(reader, "bool", []),
                         """bool = False"""
                         )

    def test_simple_type_declaration_bitstring(self):
        file = io.StringIO(
            """bit ::= BITSTRING"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('f0f0')))

        self.assertEqual(tree.read_value(reader, "bit", []),
                         """bit = 11110000"""
                         )

    def test_simple_type_declaration_bitstring_11(self):
        file = io.StringIO(
            """bit11 ::= BITSTRING_11"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('f0f0')))

        self.assertEqual(tree.read_value(reader, "bit11", []),
                         """bit11 = 11110000111"""
                         )

    def test_simple_type_declaration_uint(self):
        file = io.StringIO(
            """uint ::= UINT"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('1f')))

        self.assertEqual(tree.read_value(reader, "uint", []),
                         """uint = 31"""
                         )

    def test_simple_type_declaration_uint_7(self):
        file = io.StringIO(
            """uint7 ::= UINT_7"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff')))

        self.assertEqual(tree.read_value(reader, "uint7", []),
                         """uint7 = 127"""
                         )

    def test_simple_type_declaration_uint_3(self):
        file = io.StringIO(
            """uint3 ::= UINT_3"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('7f')))

        self.assertEqual(tree.read_value(reader, "uint3", []),
                         """uint3 = 3"""
                         )

    def test_array_declaration(self):
        file = io.StringIO(
            """array ::= ARRAY[a]{num UINT}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff00f00f')))

        self.assertEqual(''.join(tree.read_value(reader, "array", [4]).split()),
                         """array[4]=[{num=255,},{num=0,},{num=240,},{num=15,},]"""
                         )

    def test_choice_declaration_default(self):
        file = io.StringIO(
            """choice ::= CHOICE[a]{UINT(a == 5)BOOL(DEFAULT)}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff00f00f')))

        self.assertEqual(''.join(tree.read_value(reader, "choice", [4]).split()),
                         """choice[4]=(BOOL)True"""
                         )

    def test_choice_declaration_expression(self):
        file = io.StringIO(
            """choice ::= CHOICE[a]{UINT(a == 5)BOOL(DEFAULT)}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff00f00f')))

        self.assertEqual(''.join(tree.read_value(reader, "choice", [5]).split()),
                         """choice[5]=(UINT)255"""
                         )

    def test_choice_declaration_expression_with_two_variables(self):
        file = io.StringIO(
            """choice ::= CHOICE[a b]{UINT(a == b)BOOL(DEFAULT)}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff00f00f')))

        self.assertEqual(''.join(tree.read_value(reader, "choice", [5, 5]).split()),
                         """choice[5,5]=(UINT)255"""
                         )

    def test_sequence_declaration(self):
        file = io.StringIO(
            """seq ::= SEQUENCE{num UINT}"""
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff00f00f')))

        self.assertEqual(''.join(tree.read_value(reader, "seq", []).split()),
                         """seq={num=255,}"""
                         )

    def test_sequence_declaration_with_parametrized_array(self):
        file = io.StringIO(
            """arr ::= ARRAY[a]{num UINT}
                seq ::= SEQUENCE{param UINT nums arr[param]}
            """
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('020102')))

        self.assertEqual(''.join(tree.read_value(reader, "seq", []).split()),
                         """seq={param=2,nums=[{num=1,},{num=2,},],}"""
                         )

    def test_sequence_declaration_with_parametrized_array_seq_param(self):
        file = io.StringIO(
            """arr ::= ARRAY[a]{num UINT}
                seq ::= SEQUENCE[a]{nums arr[a]}
            """
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('0201')))

        self.assertEqual(''.join(tree.read_value(reader, "seq", [2]).split()),
                         """seq[2]={nums=[{num=2,},{num=1,},],}"""
                         )

    def test_sequence_declaration_with_choice_parametrized_seq_param(self):
        file = io.StringIO(
            """cho ::= CHOICE[a]{UINT(a == 1) BOOL(DEFAULT)}
                seq ::= SEQUENCE[a]{choice cho[a]}
            """
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('02')))

        self.assertEqual(''.join(tree.read_value(reader, "seq", [1]).split()),
                         """seq[1]={choice=(UINT)2,}"""
                         )

    def test_sequence_declaration_with_choice_parametrized_seq_param_bool(self):
        file = io.StringIO(
            """cho ::= CHOICE[a]{UINT(a == TRUE) BOOL(DEFAULT)}
                seq ::= SEQUENCE[a]{choice cho[a]}
            """
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('02')))

        self.assertEqual(''.join(tree.read_value(reader, "seq", [True]).split()),
                         """seq[True]={choice=(UINT)2,}"""
                         )

    def test_sequence_declaration_with_choice_default(self):
        file = io.StringIO(
            """cho ::= CHOICE[a]{UINT(a == 5) BOOL(DEFAULT)}
                seq ::= SEQUENCE[a]{choice cho[a]}
            """
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff')))

        self.assertEqual(''.join(tree.read_value(reader, "seq", [2]).split()),
                         """seq[2]={choice=(BOOL)True,}"""
                         )

    def test_sequence_declaration_with_choice_default_multitypes(self):
        file = io.StringIO(
            """cho ::= CHOICE[a]{UINT(a == TRUE) BITSTRING(a > 5) BOOL(DEFAULT)}
                seq ::= SEQUENCE[a]{choice cho[a]}
            """
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff')))

        self.assertEqual(''.join(tree.read_value(reader, "seq", [2]).split()),
                         """seq[2]={choice=(BOOL)True,}"""
                         )

    def test_sequence_declaration_with_choice_default_multitypes_bool_param(self):
        file = io.StringIO(
            """cho ::= CHOICE[a]{UINT(a == TRUE) BITSTRING(a > 5) BOOL(DEFAULT)}
                seq ::= SEQUENCE[a]{choice cho[a]}
            """
        )
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()

        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff')))

        self.assertEqual(''.join(tree.read_value(reader, "seq", [True]).split()),
                         """seq[True]={choice=(UINT)255,}"""
                         )
