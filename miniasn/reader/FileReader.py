# coding=utf-8
BITS_IN_BYTE = 8


class FileReader:
    def __init__(self, filename):
        self.__file = self.__open_file(filename)
        self.__last_byte = []
        self.__bits_counter = 0
        self.__current_line = 1
        self.__current_column = 1

    def __del__(self):
        self.__file.close()

    @property
    def current_line(self):
        return self.__current_line

    @property
    def current_column(self):
        return self.__current_column

    def __open_file(self, filename):
        return open(filename, 'rb')

    def read_byte(self):
        byte = self.__file.read(1)
        self.__update_current_position(byte)

        return byte

    def __update_current_position(self, char):
        self.__current_column += 1

        if char == '\n':
            self.__current_line += 1
            self.__current_column = 1

    def next_byte(self):
        position = self.__file.tell()
        byte = self.__file.read(1)
        self.__file.seek(position)

        return byte

    def read_bit(self):
        if not self.__last_byte or self.__bits_counter == BITS_IN_BYTE:
            self.__last_byte = self.__get_bits_from_byte(self.read_byte())
            self.__bits_counter = 0

        bit = self.__last_byte[self.__bits_counter]
        self.__bits_counter += 1

        return bit

    def __get_bits_from_byte(self, byte):
        byte = ord(byte)

        return [(byte >> i) & 1 for i in range(BITS_IN_BYTE)][::-1]
