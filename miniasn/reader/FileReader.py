UTF_8 = 'utf-8'


class FileReader:
    def __init__(self, file):
        self.__file = file
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

    def read_char(self):
        char = self.__file.read(1)
        self.__update_current_position(char)

        return char

    def __update_current_position(self, char):
        self.__current_column += 1

        if char == '\n':
            self.__current_line += 1
            self.__current_column = 1

    def preview_next_char(self):
        position = self.__file.tell()
        char = self.__file.read(1)
        self.__file.seek(position)

        return char

