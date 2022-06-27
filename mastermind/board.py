# Place your Board class in this file
from typing import Union, List
import numpy as np
import os

class MastermindBoard:
    def __init__(self, key: List[str]):
        self.turn=0
        self.rows = 12
        self.cols = 4
        self.blank = 'x'
        self.items = [[self.blank for c in range(self.cols)] for r in range(self.rows)]
        self.key= key

    def set_row(self, item: List[str], row: int) -> List[List[str]]:
        row=row-1
        for index in range(self.cols):
            self.items[row][index]=item[index]
        self.print_board()
        return self.items

    def print_board(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("          R/W")
        for c in range(self.rows):
            print(str(c+1), end=" ")
            for item in self.items[c]:
                print(str(item), end=" ")
            print(str(self.checkmatches(self.items[c]))+"/"+str(self.checkclose(self.items[c])))
        print("---------------")
        return

    def checkmatches(self, checking: List[str])-> int:
        total=0
        for index in range(self.cols):
            if self.key[index]==checking[index]:
                total+=1
        return total

    def checkclose(self, checking: List[str])-> int:
        total=0
        tempkey,tempcheck=self.remove_matches(self.key, checking)
        for index in range(len(tempcheck)):
            if tempcheck[index]=='x':
                continue
            if tempcheck[index] in tempkey:
                total+=1
                tempkey.remove(tempcheck[index])
        return total

    def remove_matches(self, target: List[str], compare: List[str])-> List[str]:
        output_tar=target.copy()
        output_comp=compare.copy()
        outputsizediff=0
        for index in range(len(output_tar)):
            if target[index]==compare[index]:
                output_tar[index]='x'
                output_comp[index]='x'
        return output_tar, output_comp

##test case
if __name__ == '__main__':
    board=MastermindBoard(['R','B','W','R'])
    board.set_row(['R','B','R','B'],1)
    board.set_row(['R','R','B','B'],2)
    board.set_row(['R','B','R','W'],3)
