BITS_IN_BYTE = 8


class FileReaderMocked:
    def __init__(self, data):
        self.__data = data

    @property
    def current_line(self):
        return None

    @property
    def current_column(self):
        return None

    def read_char(self):
        if not self.__data:
            return ''

        char = self.__data[0]
        self.__data = self.__data[1:]

        return char

    def preview_next_char(self):
        return self.__data[0] if self.__data else ''
