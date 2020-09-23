from termcolor import colored
from random import choice
from enum import Enum

class Shape(Enum):
    CIRCLE = ["(",")"]
    TRIANGLE = ["/", "\\"]
    SQUARE = ["[", "]"]

class Color(Enum):
    RED = "red"
    YELLOW = "yellow"
    BLUE = "blue"
    GREEN = "green"

class Symbol(Enum):
    CROSS = "X"
    POINTS = "P"
    WAVES = "W"
    TRIANGLE = "T"
    SQUARE = "S"

class Pion:
    def __init__(self, color, shape, symbol):
        self.color = color
        self.shape = shape
        self.symbol = symbol

    def show(self):
        return colored(f"{self.shape[0]} {self.symbol} {self.shape[1]}", self.color)

class Board:
    def __init__(self):
        self.board = []

    def aleagen(self):
        colors = [i.value for i in Color]
        shapes = [i.value for i in Shape]
        symbol = [i.value for i in Symbol]
        for i in range(7):
            row = []
            for j in range(6):
                row.append(Pion(choice(colors), choice(shapes), choice(symbol)))
            self.board.append(row)

    def show(self):
        toret = ""
        for r in self.board:
            for p in r:
                toret += p.show() + " "
            toret += "\n"
        print(toret)

b = Board()
b.aleagen()
b.show()