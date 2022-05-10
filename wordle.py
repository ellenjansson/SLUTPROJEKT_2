from pdb import Restart
import random
import os
from time import sleep
from collections import Counter
from colorama import init
init()

BOX = "▉"
GREEN = "\033[1;32;40m"
YELLOW = "\033[1;33;40m"
WHITE = "\033[1;37;40m"
LINE = "______________"

# TODO:
# - Fixa docstring
# - Fixa korrekt namngivning - 
# - Fixa längd på gissning (Inte mer eller mindre än 5) -
# - Låt användaren avsluta spelet (rensa konsollen innan nästa spel?) -

class Word:

    #En funktion som öppnar en text fil och gör den till en variabel self.local_word som kan användas i koden. 
    def __init__(self):
        f = open("words.txt", "r")
        words = f.read().splitlines()
        f.close()
        self.local_word = random.choice(words)
        print (self.local_word)
            
    #Funktion med en guess variabel som används till att korrigera om det gissade ordet är korrekt eller inte. 
    def compare(self, guess):
        """_summary_

        Args:
            guess (string): The word that the user guessed

        Returns:
            bool: True if correct guess, else False
        """
    
        self.guess = guess
        
        #En if-sats som kollar om det gissade ordet är lika med self.local_word (det slumpmässiga ordet)
        #Om self.local_word är lika med det gissade ordet skrivs det ut att man har rätt och 5 färgade rutor blir färgade grönt.
        if guess == self.local_word:
            print("\nCorrect!") 
            print(GREEN, BOX * 5)
            return True
        
        #Om self.local_word inte matchar det gissade ordet skrivs det ut att man har fel.
        else:
            print("Wrong!")
            #Här läser programmet igenom alla bokstäver i det gissade ordet och kollar vilka bokstäver som matchar in med det slumpmässiga ordet från self.local_word.
            color_matrix = []
            chars = Counter(self.local_word)            
            for i in range(len(self.local_word)):
                #Om bokstaven från det gissade ordet är på samma plats som bokstaven från self.local_word blir den motsvarande rutan till den bokstaven grön. 
                if guess[i] == self.local_word[i]:
                    color_matrix.append(GREEN + BOX)
                    chars[guess[i]] -= 1
                elif guess[i] in self.local_word:
                    color_matrix.append(YELLOW + BOX)
                else:
                    color_matrix.append(WHITE + BOX)
            #Här kollar programmet 
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
            
        print(WHITE + LINE * 5)
        restart = input("\nDo you want to restart the game? (y/n): ")
        
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