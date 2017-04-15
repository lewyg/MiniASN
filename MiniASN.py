from miniasn.lexer.Lexer import Lexer
from miniasn.reader.FileReader import FileReader


def main():
    file_reader = FileReader('example.miniasn')
    lexer = Lexer(file_reader)
    t = lexer.get_token()
    while t:
        print(t)
        t = lexer.get_token()


if __name__ == "__main__":
    main()
