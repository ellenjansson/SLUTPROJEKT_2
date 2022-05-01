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
            print("rätt") 
            return True
        
        else:
            print("fel")
            return False


class game:
    
    def __init__(self):
        my_word = word()
        while True:
            my_word.compare(input("Enter a word: "))
            
    
def main():
    game()


if __name__ == "__main__":
    main()
