import traceback

import io

from miniasn.lexer.Lexer import Lexer
from miniasn.parser.Parser import Parser
from miniasn.reader.FileReader import FileReader


def main():
    try:
        file_reader = FileReader(io.StringIO(
            """seq::= SEQUENCE[a b c] {
    d UINT_9
    e BOOL
}"""
        ))
        lexer = Lexer(file_reader)
        p = Parser(lexer)
        tree = p.parse()

        print(tree)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
