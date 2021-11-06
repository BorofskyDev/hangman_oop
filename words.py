import random
from IPython.display import clear_output as co
states = ["kansas", "maine", "florida", "texas", "oklahoma", "colorado", "missouri", "iowa", "illinois", "kentucky", "tennessee", "california",
           "massachusetts", "georgia", "delaware", "virginia", "minnesota", "nebraska", "arkansas"]

class Hangman:
    def __init__(self):
        self.word = random.choice(states)
        self.display = ["_" for letter in self.word]
        self.guesses = 0
        self.guessed_words = []

    
    def show(self):
        display = "".join(self.display)
        print(f"Mystery Word: {display}")
        
        
    def get_word_index(self, guess):
        positions = []
        for index, char in enumerate(list(self.word)):
            if char == guess:
                positions.append(index)
        return positions
    
    def update(self, idx, letter):
        for number in idx:
            self.display[number] = letter

    def check_guess(self, guess):
        if  guess in self.word not in self.guessed_words:
            idx = self.get_word_index(guess)
            self.update(idx, guess)
        elif guess in self.guessed_words:
            print("You've already made this selection. Please try again.")
        elif guess not in self.word:
            self.guesses +=1
            self.guessed_words.append(guess)
            print("Incorrect. Try again.")
        # else: 
        #     print("This is not correct.")            

    def check_for_win(self):
        display = "".join(self.display)
        word = self.word
        if display == word:
            print("~*" * 30)
            print("You've completed the game and won!")
            print("~*" * 30)    
            return True
    
def game():
    played = []
    word = Hangman()
    while True:
        guess = input("\nType in your guess: ")
        word.check_guess(guess)
        word.show()
        # word.guesses += 1
        played.append(guess)
        if word.check_for_win():
            print("~*" * 30)
            print("You've completed the game and won!")
            print("~*" * 30)
            break 
        elif word.guesses > 7:
            print("You've run out of turns. ---GAME OVER---")
            break
        # elif guess in played:
        #     print ("You've already played this word.")
def loop():
    while True:
        print("=~=" * 30)
        response = input(
            "\nWelcome to Guess the Word. To play press any key. To exit press 'n':  ").lower()
        print("=~=" * 30)
        if response =="n":
            break
        game()
loop()

