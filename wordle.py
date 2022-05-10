from pdb import Restart
import random
import os
from time import sleep
from collections import Counter
from colorama import init
init()


# Constants that have ANSI-code which is used to color boxes in the code. The line is used inbetween guesses in the console.
BOX = "▉"
GREEN = "\033[1;32;40m"
YELLOW = "\033[1;33;40m"
WHITE = "\033[1;37;40m"
LINE = "______________"


class Word:

    def __init__(self):
        """Opens a word txt file and makes the words into a variable that can be used in the code.
        """
        f = open("words.txt", "r")
        words = f.read().splitlines()
        f.close()
        self.local_word = random.choice(words)
        print (self.local_word)
            
    def compare(self, guess):
        """Function that compares the guess word with the correct word. 

        Args:
            guess (string): The word that the user guessed

        Returns:
            bool: True if correct guess, else False
        """
    
        self.guess = guess
        
        if guess == self.local_word:
            print("\nCorrect!") 
            print(GREEN, BOX * 5)
            return True
        
        else:
            print("Wrong!")
            color_matrix = []
            chars = Counter(self.local_word)            
            for i in range(len(self.local_word)):
                if guess[i] == self.local_word[i]:
                    color_matrix.append(GREEN + BOX)
                    chars[guess[i]] -= 1
                elif guess[i] in self.local_word:
                    color_matrix.append(YELLOW + BOX)
                else:
                    color_matrix.append(WHITE + BOX)
            counter = 0
            for color, char in zip(color_matrix, self.local_word):
                if color == YELLOW+BOX and chars[char] >= 0:
                    color_matrix[counter] = WHITE + BOX
                counter += 1
            for color in color_matrix:
                print(color, end = " ")
            print()
        return False
            
    
class Game:
    
    def __init__(self):
        self.guesses = 0
        self.max_guesses = 6
        
    def play_game(self):
        """
           A function which initializes the game and sends out a restart option that clears the console. 
           The function also includes a guess counter aswell as a letter interval that corrects you if you 
           write a too short/long word. 
        """
        my_word = Word()
        
        while self.guesses<self.max_guesses:
            print(WHITE + LINE)
            self.tmp_guess = input("Enter a word: ")

            if (len(self.tmp_guess)<5):
                print("\nToo short word, guess again!\n")
                
            elif (len(self.tmp_guess)>5):        
                print("\nToo long word, guess again!")

            else: 
                self.guesses = self.guesses + 1
                print("Guesses:", self.guesses)
                if my_word.compare(self.tmp_guess):
                    break
            
        print(WHITE + LINE)
        restart = input("Do you want to restart the game? (y/n): ")
        
        if restart == "y":
            print("\nThe game will now restart")
            sleep(2)
            os.system('cls')
            self.__init__()
            self.play_game()
        elif restart == "n":
            os.system('cls')
            print("\nYou have chosen to exit the game, thank you for playing!")
            exit()
        else:
            else_restart = input("Please write y or n: ")
            if else_restart == "y":
                os.system('cls')
                self.__init__()
                self.play_game()
            elif else_restart == "n":
                exit()
            else:
                print("You are too dumb to play this game...")
                exit()
                
def main():
    new_game = Game()
    new_game.play_game()

if __name__ == "__main__":
    main()