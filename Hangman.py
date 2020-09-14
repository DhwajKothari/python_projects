
from random import choice

# print("H A N G M A N")
# words_to_win = ['python', 'java', 'kotlin', 'javascript']
# win=random.choice(words_to_win)
# user=input("Guess the word: ")
# if user == win:
#     print("You survived!")
# else:
#     print("You are hanged!")

# class Hangman:
#     choice_list = ['python', 'java', 'kotlin', 'javascript']
#     def __init__(self):
#         self.welcome = "H A N G M A N"
#         self.word = random.choice(Hangman.choice_list)
#     def start(self):
#         print(self.welcome)
#         self.guess()
#     def guess(self):
#         hint = self.word[:3] + "-" * (len(self.word) - 3)
#         self.check(input(f"Guess the word {hint}:"))
#     def check(self,user_guess):
#         if user_guess == self.word:
#             print("You survived!")
#         else:
#             print("You are hanged!")
#
# game = Hangman()
# game.start()


class Hangman:

    choice_list = ['python', 'java', 'kotlin', 'javascript']

    def __init__(self):
        self.welcome = "H A N G M A N \n"
        self.word = choice(Hangman.choice_list)
        self.revealed = list("-" * len(self.word))
        self.try_set = set()
        self.lives = 8

    def start(self):
        print(self.welcome)
        self.choice = ""
        while self.choice != "exit":
            self.choice = input('Type "play" to play the game, "exit" to quit: ')
            if self.choice == "play":
                self.game()
        
    def game(self):
        while True:
            if self.lives == 0:
                print("You are hanged!")
                break
            if self.word == "".join(self.revealed):
                print(f"You guessed the word {self.word} \nYou survived!")
                break
            self.guess()
    def guess(self):
        print()
        print("".join(self.revealed)) 
        self.check(input("Input a letter: "))
        
    def check(self, user_guess):
        if len(user_guess) != 1:
            print("You should input a single letter")
        elif not user_guess.islower():
            print("It is not an ASCII lowercase letter")
        elif user_guess in self.try_set:
            print("You already typed this letter")
        else:
            if user_guess in self.word:
                for i, letter in enumerate(self.word):
                    if letter == user_guess:
                        self.revealed[i] = letter
            else:
                self.lives -= 1
                print("No such letter in the word")
            self.try_set.add(user_guess)


game = Hangman()
game.start()
