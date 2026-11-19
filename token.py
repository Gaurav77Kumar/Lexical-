from enum import Enum

class TokenType(Enum):

    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"

    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    GREATER = "GREATER"
    LESS = "LESS"
    ASSIGN = "ASSIGN"

    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    COMMA = "COMMA"
    SEMICOLON = "SEMICOLON"
    EOF = "EOF"

class Token:

    def __init__(self, type, value, position,line, column):
        self.type = type
        self.value = value
        self.position = position
        self.line = line
        self.column = column

    def __str__(self):
        return (
            f"({self.type.value}, {self.value}, "
            f"line={self.line}, column={self.column})"
        )


    