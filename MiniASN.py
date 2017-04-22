import traceback

from miniasn.lexer.Lexer import Lexer
from miniasn.parser.Parser import Parser
from miniasn.reader.FileReader import FileReader


def main():
    try:
        file_reader = FileReader('example.miniasn')
        lexer = Lexer(file_reader)
        p = Parser(lexer)
        tree = p.parse()

        print(tree)
    except Exception as ex:
        print(traceback.format_exc())


if __name__ == "__main__":
    main()
