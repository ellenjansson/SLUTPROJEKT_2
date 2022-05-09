import random
from collections import Counter

BOX = "▉"
GREEN = "\033[1;32;40m"
YELLOW = "\033[1;33;40m"
WHITE = "\033[1;37;40m"

class word:

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
            print(GREEN.encode('utf-8'), BOX * 5)
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
                #Om bokstaven från det gissade ordet finns i self.local_word fast inte är på rätt plats, blir den motsvarande rutan till den bokstaven gul.
                elif guess[i] in self.local_word:
                    color_matrix.append(YELLOW + BOX)
                #Om bokstaven från det gissade ordet inte finns i self.local_word blir motsvarande rutan till ordet grått. 
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
    
class game:
    
    def __init__(self):
        self.guesses = 0
        self.max_guesses = 6
        
    def play_game(self):
        my_word = word()
        
        while self.guesses<self.max_guesses:
            self.guesses = self.guesses + 1
            print("Guesses:", self.guesses)
            if my_word.compare(input("Enter a word: ")):
                break
        
def main():
    new_game = game()
    new_game.play_game()


if __name__ == "__main__":
    main()