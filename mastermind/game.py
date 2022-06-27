##game file
import board
from typing import TypeVar, List, Union
import random


class Game:
    def __init__(self):
        self.end_game = 0
        self.code=['B','R','C','W','P','G']
        self.turn=0
        self.board=()
        self.run_game()

    def quit(self) -> None:
        self.end_game = 1

    def run_game(self) -> None:
        self.turn=0
        key= []
        for index in range(4):
            symbol=self.code[random.randrange(1,6)]
            key.append(symbol)
        self.board = board.MastermindBoard(key)
        self.board.print_board()
        while not self.end_game:
            self.play_turn()
        a = str(input('Play again? (y/n): '))
        if "y" in a or "Y" in a:
            self.run_game()

    def play_turn(self) -> None:
        guess= self.take_turn()
        if self.check_win(guess):
            print(f'You won the game!')
            self.quit()
            return
        else:
            self.turn+=1
        if self.turn==12:
            print("You lost.")
            self.quit()

    def take_turn(self)->List[str]:
        output=[]
        a = str(input('Enter your guess: '))
        while not self.check_valid_guess(a):
            print('Not a valid guess.')
            a = str(input('Enter your guess: '))
        for text in a:
            if text !=" ":
                output.append(text)
        self.turn+=1
        self.board.set_row(output, self.turn)
        return output

    def check_valid_guess(self, text_string: str)->bool:
        characters=0
        for char in text_string:
            if char==" ":
                continue
            elif char not in self.code:
                return False
            else:
                characters+=1

        return characters==4

    def check_win(self, guess: List[str]) -> bool:
        return self.board.checkmatches(guess)==4

if __name__ == '__main__':
    new_game=Game()
