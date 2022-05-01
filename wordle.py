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

class game:
    
    def __init__(self):
        word()
        
        
def main():
    game()


if __name__ == "__main__":
    main()
