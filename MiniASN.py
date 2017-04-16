from miniasn.lexer.Lexer import Lexer
from miniasn.reader.FileReader import FileReader


def main():
    file_reader = FileReader('example.miniasn')
    lexer = Lexer(file_reader)
    t = lexer.read_next_token()
    while t:
        print(t)
        t = lexer.read_next_token()


if __name__ == "__main__":
    main()
