BITS_IN_BYTE = 8


class FileReaderMocked:
    def __init__(self, file):
        self.__file = file
        self.__last_byte = []
        self.__bits_counter = 0
        self.__current_line = 1
        self.__current_column = 1

    @property
    def current_line(self):
        return self.__current_line

    @property
    def current_column(self):
        return self.__current_column

    def read_char(self):
        if not self.__file:
            return ''

        byte = self.__file[0]
        self.__file = self.__file[1:]
        self.__update_current_position(byte)

        return byte

    def __update_current_position(self, char):
        self.__current_column += 1

        if char == '\n':
            self.__current_line += 1
            self.__current_column = 1

    def preview_next_char(self):
        return self.__file[0] if self.__file else ''

    def read_bit(self):
        if not self.__last_byte or self.__bits_counter == BITS_IN_BYTE:
            byte = self.read_char()
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