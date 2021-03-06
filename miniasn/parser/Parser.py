from miniasn.exceptions.ParserExceptions import UnexpectedTokenException
from miniasn.node.NodeType import NodeType
from miniasn.parser import Nodes
from miniasn.token.TokenType import TokenType


class Parser:
    __nodes = Nodes.nodes

    def __init__(self, lexer, nodes=__nodes):
        self.__lexer = lexer
        self.__nodes = nodes
        self.declared_types = []
        self.local_names = []

    def parse(self):
        self.__advance()
        root = self.parse_node(NodeType.DATA_STRUCTURE)

        return root

    def parse_node(self, node_type, *args, **kwargs):
        if node_type in NodeType:
            type = self.__nodes[node_type]
            node = type.parse(self, *args, **kwargs)
        else:
            node = self.__parse_token(node_type)

        return node

    def parse_or_node_list(self, or_list, *args, **kwargs):
        for node_type in or_list:
            if self.can_parse(node_type):
                return self.parse_node(node_type, *args, **kwargs)

        token = self.__get_token()
        raise UnexpectedTokenException(token.line, token.column, token.token_type, self.get_first(or_list))

    def end_of_file(self):
        return self.__get_token().token_type == TokenType.END_OF_FILE

    def can_parse(self, node):
        if node in TokenType:
            return self.__check_token_type(node)

        if node in NodeType:
            type = self.__nodes[node]
            return self.can_parse(type.first)

        for node_type in node:
            if self.can_parse(node_type):
                return True

        return False

    def get_first(self, node):
        if node in TokenType:
            return node.name

        if node in NodeType:
            type = self.__nodes[node]
            return self.get_first(type.first)

        return [self.get_first(node_type) for node_type in node]

    def check_if_name_exists(self, names, identifier):
        for name in names:
            if name.identifier.value == identifier.value:
                return name

        return None

    def __parse_token(self, token_type):
        token = self.__get_token()
        if self.__check_token_type(token_type):
            self.__advance()
        else:
            raise UnexpectedTokenException(token.line, token.column, token.token_type, token_type)

        return token

    def __advance(self):
        return self.__lexer.read_next_token()

    def __get_token(self):
        return self.__lexer.get_token()

    def __check_token_type(self, expected_type):
        token = self.__get_token()
        return token.token_type is expected_type if token else False
