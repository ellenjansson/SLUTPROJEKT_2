import random
from collections import Counter

class word:

    def __init__(self):
        f = open("words.txt", "r")
        words = f.read().splitlines()
        f.close()
        self.local_word = random.choice(words)
        print (self.local_word)
    
    def compare(self, guess):
        self.guess = guess
        
        if guess == self.local_word:
            print("\nCorrect!") 
            print("\033[1;32;40m▉" * 5)
            return True

        else:
            print("Wrong!")
            color_matrix = []
            chars = Counter(self.local_word)            
            for i in range(len(self.local_word)):
                if guess[i] == self.local_word[i]:
                    color_matrix.append("\033[1;32;40m▉")
                    chars[guess[i]] -= 1
                elif guess[i] in self.local_word:
                    color_matrix.append("\033[1;33;40m▉")
                else:
                    color_matrix.append("\033[1;37;40m▉")
            
            counter = 0
            for color, char in zip(color_matrix, self.local_word):
                if color == "\033[1;33;40m▉" and chars[char] >= 0:
                    color_matrix[counter] = "\033[1;37;40m▉"
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