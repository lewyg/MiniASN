BITS_IN_BYTE = 8
UTF_8 = 'utf-8'


class FileReader:
    def __init__(self, filename):
        self.__file = self.__open_file(filename)
        self.__last_byte = []
        self.__bits_counter = 0
        self.__current_line = 1
        self.__current_column = 1

    def __del__(self):
        try:
            self.__file.close()
        except AttributeError:
            pass

    @property
    def current_line(self):
        return self.__current_line

    @property
    def current_column(self):
        return self.__current_column

    def __open_file(self, filename):
        return open(filename, 'rb')

    def read_char(self):
        byte = self.__file.read(1)
        char = self.__byte_to_char(byte)
        self.__update_current_position(char)

        return char

    def __update_current_position(self, char):
        self.__current_column += 1

        if char == '\n':
            self.__current_line += 1
            self.__current_column = 1

    def preview_next_char(self):
        position = self.__file.tell()
        byte = self.__file.read(1)
        self.__file.seek(position)

        return self.__byte_to_char(byte)

    def __byte_to_char(self, byte):
        return str(byte, UTF_8)

    def read_bit(self):
        if not self.__last_byte or self.__bits_counter == BITS_IN_BYTE:
            byte = self.__file.read(1)
            if not byte:
                return None
            self.__last_byte = self.__get_bits_from_byte(byte)
            self.__bits_counter = 0

        bit = self.__last_byte[self.__bits_counter]
        self.__bits_counter += 1

        return bit

    def __get_bits_from_byte(self, byte):
        byte = ord(byte)

        return [(byte >> i) & 1 for i in range(BITS_IN_BYTE)][::-1]
