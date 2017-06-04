import io

from unittest import TestCase

from miniasn.encoder import Encoder
from miniasn.reader.ByteReader import ByteReader


class EncoderTest(TestCase):
    def test_bool_false(self):
        reader = ByteReader(io.BytesIO(bytearray.fromhex('00')))
        value = Encoder.encode_bool(reader)

        self.assertFalse(value)

    def test_bool_true(self):
        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff')))
        value = Encoder.encode_bool(reader)

        self.assertTrue(value)

    def test_bitstring(self):
        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff')))
        value = Encoder.encode_bitstring(reader, 8)

        self.assertEqual(value, "11111111")

    def test_uint(self):
        reader = ByteReader(io.BytesIO(bytearray.fromhex('ff')))
        value = Encoder.encode_uint(reader, 8)

        self.assertEqual(value, 255)
