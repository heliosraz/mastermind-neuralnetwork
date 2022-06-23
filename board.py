# Place your Board class in this file
from typing import Union, List

class MastermindBoard:
    def __init__(self, key: List[str]):
        self.turn=0
        self.rows = 12
        self.cols = 4
        self.blank = 'x'
        self.items = [[self.blank for c in range(self.cols)] for r in range(self.rows)]
        self.key= key

    def guess(self, guess: Union[str]) -> List[List[str]]:
        for index in range(self.col-1):
            self.items[turn][index]=guess[index]:
        self.print_board()
        return self.items

    def print_board(self) -> None:
        print(self.name)
        print("  ", end="")
        for c in range(self.rows-1):
            print(str(c+1), end=" ")
            for item in self.items[c][]:
                print(str(item), end=" ")
            print(str(self.checkmatches(self.items[c][]))+"/"+str(self.checkclose(self.items[c][]))+"/n")
        return

    def checkmatches(self)-> str:

    def checkclose(self)-> str:
