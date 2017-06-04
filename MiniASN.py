import sys

from miniasn.lexer.Lexer import Lexer
from miniasn.parser.Parser import Parser
from miniasn.reader.ByteReader import ByteReader
from miniasn.reader.FileReader import FileReader


def main(args):
    try:
        if (len(args)) < 3:
            print("Missing arguments!")
            return

        file_reader = FileReader(open(args[0]))
        lexer = Lexer(file_reader)
        p = Parser(lexer)
        tree = p.parse()

        reader = ByteReader(open(args[1]))
        print(tree.read_value(reader, args[2], arguments=args[3:]))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv[1:])
