##game file
import board
from typing import TypeVar, List, Union
import random
import os


class Game:
    def __init__(self):
        self.end_game = 0
        self.code=['B','R','C','W','P','G']
        self.turn=1
        self.board=()
        self.run_game()

    def quit(self) -> None:
        self.end_game = 1
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_game(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        self.end_game = 0
        self.turn=1
        key= []
        for index in range(4):
            symbol=self.code[random.randrange(1,6)]
            key.append(symbol)
        self.board = board.MastermindBoard(key)
        print('''
        =======================================
        Welcome to Mastermind!
        1. You will be attempting to guess a
        sequence of 4 characters: B, R, C, W, P,
        G, with 12 guesses.
        2. The number of characters in the rig-
        ht spot and the number of characters
        that are in the sequence, but not in
        the right spot, are indicated by the
        numbers seperated by the slash, respec-
        tively.
        3. Quit the game at any time by
        entering quit.
        =======================================
        ''')
        a = 'n'
        while a!="y":
            a=str(input('Ready? (y/n): '))
            if a=="quit":
                self.quit()
                return
        self.board.print_board()
        while not self.end_game:
            self.play_turn()
        a = str(input('Play again? (y/n): '))
        while 1:
            if a=="quit":
                self.quit()
                return
            if a=='y' or a=='Y':
                self.run_game()
                return
            elif a != "n":
                print("Input not valid")
                a = str(input('Play again? (y/n): '))
            else:
                return


    def play_turn(self) -> None:
        guess= self.take_turn()
        if guess==[' ',' ',' ',' ']:
            self.quit()
            print("You quit the game.")
            return
        if self.check_win(guess):
            print('You won the game!')
            self.quit()
            return
        else:
            self.turn+=1
        if self.turn==13:
            print("You lost.")
            self.quit()
            return

    def take_turn(self)->List[str]:
        output=[]
        a = str(input('Enter your guess: ')).upper()
        if a.lower()=="quit":
            return [' ',' ',' ',' ']
        while not self.check_valid_guess(a):
            print('Not a valid guess.')
            a = str(input('Enter your guess: ')).upper()
            if a.lower()=="quit":
                self.quit()
                return
        for text in a:
            if text !=" ":
                output.append(text)
        self.board.set_row(output, self.turn)
        return output

    def check_valid_guess(self, text_string: str)->bool:
        characters=0
        for char in text_string:
            if char==" ":
                continue
            elif char not in self.code:
                print('Use the following characters: B, R, C, W, P, G.')
                return False
            else:
                characters+=1
        if characters>4:
            print('You can only use 4 characters.')
        return characters==4

    def check_win(self, guess: List[str]) -> bool:
        return self.board.checkmatches(guess)==4

if __name__ == '__main__':
    new_game=Game()
