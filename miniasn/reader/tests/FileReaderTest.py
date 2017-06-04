import io

from unittest import TestCase

from miniasn.reader.FileReader import FileReader


class FileReaderTest(TestCase):
    def test_instance(self):
        file_reader = FileReader(io.StringIO(''))

        self.assertIsInstance(file_reader, FileReader)

    def test_when_file_does_not_exists(self):
        file_reader = FileReader(None)

        self.assertRaises(AttributeError, file_reader.read_char)

    def test_read_byte(self):
        file_reader = FileReader(io.StringIO('a'))
        char = file_reader.read_char()

        self.assertEqual(char, 'a')

    def test_read_byte_when_end_of_file(self):
        file_reader = FileReader(io.StringIO(''))
        char = file_reader.read_char()

        self.assertEqual(char, '')

    def test_update_position_without_newline(self):
        file_reader = FileReader(io.StringIO('a'))
        file_reader.read_char()

        self.assertEqual(file_reader.current_line, 1)
        self.assertEqual(file_reader.current_column, 2)

    def test_update_position_with_newline(self):
        file_reader = FileReader(io.StringIO("\n"))
        file_reader.read_char()

        self.assertEqual(file_reader.current_line, 2)
        self.assertEqual(file_reader.current_column, 1)

    def test_preview_next_byte(self):
        file_reader = FileReader(io.StringIO('a'))
        preview_char = file_reader.preview_next_char()
        char = file_reader.read_char()

        self.assertEqual(char, preview_char)

    def test_preview_next_byte_when_end_of_file(self):
        file_reader = FileReader(io.StringIO(''))
        preview_char = file_reader.preview_next_char()

        self.assertEqual(preview_char, '')
