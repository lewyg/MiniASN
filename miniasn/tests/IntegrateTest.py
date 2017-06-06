import io

from unittest import TestCase

from miniasn.lexer.Lexer import Lexer
from miniasn.parser.Parser import Parser
from miniasn.reader.ByteReader import ByteReader
from miniasn.reader.FileReader import FileReader


class IntegrateTest(TestCase):
    def assertMiniASNTest(self, data_structure, hex_data, result, name, params=None):
        if params is None:
            params = []

        file = io.StringIO(data_structure)
        lexer = Lexer(FileReader(file))
        parser = Parser(lexer)
        tree = parser.parse()
        reader = ByteReader(io.BytesIO(bytearray.fromhex(hex_data)))

        self.assertEqual(''.join(tree.read_value(reader, name, params).split()), ''.join(result.split()))

    def test_structure_not_found(self):
        data_structure = """uint ::= UINT"""
        result = """Structure aaa not found!"""

        self.assertMiniASNTest(data_structure, '1f', result, 'aaa')

    def test_simple_type_declaration_bool(self):
        data_structure = """bool ::= BOOL"""
        result = """bool=False"""

        self.assertMiniASNTest(data_structure, '00', result, 'bool')

    def test_simple_type_declaration_bitstring(self):
        data_structure = """bit ::= BITSTRING"""
        result = """bit=11110000"""

        self.assertMiniASNTest(data_structure, 'f0f0', result, 'bit')

    def test_simple_type_declaration_bitstring_11(self):
        data_structure = """bit11 ::= BITSTRING_11"""
        result = """bit11=11110000111"""

        self.assertMiniASNTest(data_structure, 'f0f0', result, 'bit11')

    def test_simple_type_declaration_uint(self):
        data_structure = """uint ::= UINT"""
        result = """uint=31"""

        self.assertMiniASNTest(data_structure, '1f', result, 'uint')

    def test_simple_type_declaration_uint_7(self):
        data_structure = """uint7 ::= UINT_7"""
        result = """uint7=127"""

        self.assertMiniASNTest(data_structure, 'ff', result, 'uint7')

    def test_simple_type_declaration_uint_3(self):
        data_structure = """uint3 ::= UINT_3"""
        result = """uint3=3"""

        self.assertMiniASNTest(data_structure, '7f', result, 'uint3')

    def test_array_declaration(self):
        data_structure = """array ::= ARRAY[a]{num UINT}"""
        result = """array[4]=[{num=255,},{num=0,},{num=240,},{num=15,},]"""

        self.assertMiniASNTest(data_structure, 'ff00f00f', result, 'array', [4])

    def test_choice_declaration_default(self):
        data_structure = """choice ::= CHOICE[a]{UINT(a == 5)BOOL(DEFAULT)}"""
        result = """choice[4]=(BOOL)True"""

        self.assertMiniASNTest(data_structure, 'ff00f00f', result, 'choice', [4])

    def test_choice_declaration_expression(self):
        data_structure = """choice ::= CHOICE[a]{UINT(a == 5)BOOL(DEFAULT)}"""
        result = """choice[5]=(UINT)255"""

        self.assertMiniASNTest(data_structure, 'ff00f00f', result, 'choice', [5])

    def test_choice_declaration_expression_with_two_variables(self):
        data_structure = """choice ::= CHOICE[a b]{UINT(a == b)BOOL(DEFAULT)}"""
        result = """choice[5,5]=(UINT)255"""

        self.assertMiniASNTest(data_structure, 'ff00f00f', result, 'choice', [5, 5])

    def test_sequence_declaration(self):
        data_structure = """seq ::= SEQUENCE{num UINT}"""
        result = """seq={num=255,}"""

        self.assertMiniASNTest(data_structure, 'ff00f00f', result, 'seq')

    def test_sequence_declaration_with_parametrized_array(self):
        data_structure = """arr ::= ARRAY[a]{num UINT}
                            seq ::= SEQUENCE{param UINT nums arr[param]}
                            """
        result = """seq={param=2,nums=[{num=1,},{num=2,},],}"""

        self.assertMiniASNTest(data_structure, '020102', result, 'seq')

    def test_sequence_declaration_with_parametrized_array_seq_param(self):
        data_structure = """arr ::= ARRAY[a]{num UINT}
                            seq ::= SEQUENCE[a]{nums arr[a]}
                            """
        result = """seq[2]={nums=[{num=2,},{num=1,},],}"""

        self.assertMiniASNTest(data_structure, '0201', result, 'seq', [2])

    def test_sequence_declaration_with_choice_parametrized_seq_param(self):
        data_structure = """cho ::= CHOICE[a]{UINT(a == 1) BOOL(DEFAULT)}
                            seq ::= SEQUENCE[a]{choice cho[a]}
                        """
        result = """seq[1]={choice=(UINT)2,}"""

        self.assertMiniASNTest(data_structure, '02', result, 'seq', [1])

    def test_sequence_declaration_with_choice_parametrized_seq_param_bool(self):
        data_structure = """cho ::= CHOICE[a]{UINT(a == TRUE) BOOL(DEFAULT)}
                            seq ::= SEQUENCE[a]{choice cho[a]}
                        """
        result = """seq[True]={choice=(UINT)2,}"""

        self.assertMiniASNTest(data_structure, '02', result, 'seq', [True])

    def test_sequence_declaration_with_choice_default(self):
        data_structure = """cho ::= CHOICE[a]{UINT(a == 5) BOOL(DEFAULT)}
                            seq ::= SEQUENCE[a]{choice cho[a]}
                            """
        result = """seq[2]={choice=(BOOL)True,}"""

        self.assertMiniASNTest(data_structure, 'ff', result, 'seq', [2])

    def test_sequence_declaration_with_choice_default_multitypes(self):
        data_structure = """cho ::= CHOICE[a]{UINT(a == TRUE) BITSTRING(a > 5) BOOL(DEFAULT)}
                            seq ::= SEQUENCE[a]{choice cho[a]}
                            """
        result = """seq[2]={choice=(BOOL)True,}"""

        self.assertMiniASNTest(data_structure, 'ff', result, 'seq', [2])

    def test_sequence_declaration_with_choice_default_multitypes_bool_param(self):
        data_structure = """cho ::= CHOICE[a]{UINT(a == TRUE) BITSTRING(a > 5) BOOL(DEFAULT)}
                            seq ::= SEQUENCE[a]{choice cho[a]}
                            """
        result = """seq[True]={choice=(UINT)255,}"""

        self.assertMiniASNTest(data_structure, 'ff', result, 'seq', [True])
