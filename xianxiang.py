from termcolor import colored
from random import choice

class Shape:
    CIRCLE = ["(",")"]
    TRIANGLE = ["/", "\\"]
    SQUARE = ["[", "]"]

class Color:
    RED = "red"
    YELLOW = "yellow"
    BLUE = "blue"
    GREEN = "green"

class Symbol:
    CROSS = "X"
    POINTS = "P"
    WAVES = "W"
    TRIANGLE = "T"
    SQUARE = "S"

class Pion:
    def __init__(color, shape, symbol):
        self.col = color
        self.shape = shape 
        self.symbol = symbol

    def show():
        return colored(f"{self.shape[0]} {self.symbol} {self.shape[1]}", self.color)

class Board:
    def __init__():
        self.board = []

    def aleagen():
        for i in range(6):
            row = []
            for j in range(7):
                p = Pion(choice)


    def show():
        
