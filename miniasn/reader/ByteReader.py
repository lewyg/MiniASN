from miniasn.exceptions.ReaderException import EndOfBytesException

BITS_IN_BYTE = 8


class ByteReader:
    def __init__(self, file):
        self.__file = file
        self.__last_byte = []
        self.__bits_counter = 0

    def __del__(self):
        try:
            self.__file.close()
        except AttributeError:
            pass

    def read_byte(self):
        byte = self.__file.read(1)

        if byte is b'':
            raise EndOfBytesException()

        return byte

    def read_bit(self):
        if not self.__last_byte or self.__bits_counter == BITS_IN_BYTE:
            byte = self.read_byte()
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
