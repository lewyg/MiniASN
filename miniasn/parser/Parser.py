from miniasn.exceptions.ParserExceptions import UnexpectedTokenException, EndOfFileException
from miniasn.node.NodeType import NodeType
from miniasn.parser import Nodes
from miniasn.token.TokenType import TokenType


class Parser:
    __nodes = Nodes.nodes

    def __init__(self, lexer):
        self.__lexer = lexer

    def parse(self):
        self.__advance()
        root = self.parse_node(NodeType.DATA_STRUCTURE)

        return root

    def parse_or_node_list(self, or_list):
        for node_type in or_list:
            if self.can_parse(node_type):
                return self.parse_node(node_type)

        token = self.__get_token()
        if token:
            raise UnexpectedTokenException(token.line, token.column, token.token_type, [node.name for node in or_list])
        else:
            raise EndOfFileException([node.name for node in or_list])

    def can_parse(self, first):
        if first in TokenType:
            return self.__check_token_type(first)

        if first in NodeType:
            type = self.__nodes[first]
            return self.can_parse(type.first)

        for node_type in first:
            if self.can_parse(node_type):
                return True

        return False

    def parse_node(self, node_type):
        if node_type in NodeType:
            type = self.__nodes[node_type]
            node = type.parse(self)
        else:
            node = self.__parse_token(node_type)

        return node

    def end_of_file(self):
        return self.__get_token() is None

    def __parse_token(self, token_type):
        token = self.__get_token()
        if self.__check_token_type(token_type):
            self.__advance()
        else:
            if token:
                raise UnexpectedTokenException(token.line, token.column, token.token_type, token_type)
            else:
                raise EndOfFileException(token_type)

        return token

    def __advance(self):
        return self.__lexer.read_next_token()

    def __get_token(self):
        return self.__lexer.get_token()

    def __check_token_type(self, expected_type):
        token = self.__get_token()
        return token.token_type is expected_type if token else False
