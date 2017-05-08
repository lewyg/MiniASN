import os
from unittest import TestCase

from miniasn.reader.FileReader import FileReader

resource_path = os.path.dirname(os.path.abspath(__file__)) + '/res/'


class FileReaderTest(TestCase):
    def test_instance(self):
        file_reader = FileReader(resource_path + 'empty_file')

        self.assertIsInstance(file_reader, FileReader)

    def test_when_file_does_not_exists(self):
        self.assertRaises(IOError, FileReader, 'not_existing_file')

    def test_read_byte(self):
        file_reader = FileReader(resource_path + 'one_char_file')
        char = file_reader.read_char()

        self.assertEqual(char, 'a')

    def test_read_byte_when_end_of_file(self):
        file_reader = FileReader(resource_path + 'empty_file')
        char = file_reader.read_char()

        self.assertEqual(char, '')

    def test_update_position_without_newline(self):
        file_reader = FileReader(resource_path + 'one_char_file')
        file_reader.read_char()

        self.assertEqual(file_reader.current_line, 1)
        self.assertEqual(file_reader.current_column, 2)

    def test_update_position_with_newline(self):
        file_reader = FileReader(resource_path + 'multi_line_file')
        file_reader.read_char()  # CR
        file_reader.read_char()  # LF

        self.assertEqual(file_reader.current_line, 2)
        self.assertEqual(file_reader.current_column, 1)

    def test_preview_next_byte(self):
        file_reader = FileReader(resource_path + 'one_char_file')
        preview_char = file_reader.preview_next_char()
        char = file_reader.read_char()

        self.assertEqual(char, preview_char)

    def test_preview_next_byte_when_end_of_file(self):
        file_reader = FileReader(resource_path + 'empty_file')
        preview_char = file_reader.preview_next_char()

        self.assertEqual(preview_char, '')
