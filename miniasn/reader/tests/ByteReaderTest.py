import io

import os
from unittest import TestCase

from miniasn.exceptions.ReaderException import EndOfBytesException
from miniasn.reader.ByteReader import ByteReader

resource_path = os.path.dirname(os.path.abspath(__file__)) + '/res/'


class ByteReaderTest(TestCase):
    def test_instance(self):
        file_reader = ByteReader(io.BytesIO(b''))

        self.assertIsInstance(file_reader, ByteReader)

    def test_when_file_does_not_exists(self):
        file_reader = ByteReader(None)

        self.assertRaises(AttributeError, file_reader.read_byte)

    def test_read_byte(self):
        file_reader = ByteReader(io.BytesIO(b'a'))
        byte = file_reader.read_byte()

        self.assertEqual(byte, b'a')

    def test_read_byte_when_end_of_file(self):
        file_reader = ByteReader(io.BytesIO(b''))

        self.assertRaises(EndOfBytesException, file_reader.read_byte)

    def test_read_bit(self):
        file_reader = ByteReader(io.BytesIO(b'a'))
        bit = file_reader.read_bit()

        self.assertEqual(bit, 0)

    def test_read_bit_when_end_of_file(self):
        file_reader = ByteReader(io.BytesIO(b''))

        self.assertRaises(EndOfBytesException, file_reader.read_bit)

    def test_read_bits_whole_byte(self):
        file_reader = ByteReader(io.BytesIO(b'ab'))
        bit = file_reader.read_bit()
        byte = []
        while bit is not None and len(byte) < 8:
            byte.append(bit)
            bit = file_reader.read_bit()

        # 01100001 = 97(a)
        self.assertEqual(byte, [0, 1, 1, 0, 0, 0, 0, 1])
