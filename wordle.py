import random

class word:

    def get_word():
        pass    
        

    def __init__(self):
        f = open("words.txt", "r")
        words = f.read().splitlines()
        f.close()
        self.local_word = random.choice(words)
        print (self.local_word)
    
    def compare(self, guess):
        self.guess = guess
        
        if guess == self.local_word:
            print("Correct!") 
            return True
        
        else:
            tmpword=self.local_word
            print("Wrong!")
            for i in range(5):
                if guess[i] == self.local_word[i]:
                    print("\033[1;32;40m▉\n")
                    tmpword[i]="*"
                else:
                    if guess[i] in tmpword:
                        print("\033[1;33;40m▉\n")
                    else:
                        print("\033[1;37;40m▉\n")

            return False


class game:
    
    def __init__(self):
        self.guesses = 0
        self.max_guesses = 6
        my_word = word()
        
        while self.guesses<self.max_guesses:
            self.guesses = self.guesses + 1
            print("Guesses:", self.guesses)
            if my_word.compare(input("Enter a word: ")):
                break
                
        
def main():
    game()


if __name__ == "__main__":
    main()
