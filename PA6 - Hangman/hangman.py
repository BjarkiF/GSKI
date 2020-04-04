
import random

# TODO: hægt að giska 2x á sama staf, hægt að giska á ekkert(enter), laga win/lose ef giskað er á allt orðið, fleira
class Hangman:
    def __init__(self):
        self._word_list = []
        self._guesses = 10
        self._word = ""
        self._failed = ""
        self._wins = 0
        self._losses = 0

    def _read(self):
        word_list = []
        file = open("wordbank.txt", "r")
        for line in file:
            word_list.append(line[:-1])
        return word_list

    def _add_word(self):
        while True:
            word = input("Input word, no spaces: ")
            if " " in word:
                print("Error: no spaces allowed")
            elif not word.isalpha():
                print("Error: Word must contain only letters")
            else:
                break
        with open("wordbank.txt", "a") as file:
            file.write(word + "\n")

    def play(self):
        self._setup()
        word_hidden = ["-"] * len(self._word)
        play = True
        while play:
            print("_" * 15)
            if self._guesses > 1:
                print(str(self._guesses) + " GUESSES REMAIN")
            else:
                print("LAST GUESS")
            for letter in word_hidden:
                print(letter, end="")
            print("\nNOT FOUND: " + self._failed)
            guess = input("GUESS: ")
            if len(guess) > 1:
                if guess == self._word:
                    print("WIN")
                    play = False
                else:
                    print("LOSE :(")
                    play = False
            elif guess in self._word:
                count = 0
                found_index = []
                for letter in self._word:
                    if letter == guess:
                        found_index.append(count)
                    count += 1
                for index in found_index:
                    word_hidden[index] = guess
            else:
                self._failed += guess + " "
            self._guesses -= 1
            if not "-" in word_hidden:
                self._wins += 1
                print(self._word)
                print("YOU WIN! :D")
                again = input("\nPLAY AGAIN? (y/n)")
                if again.upper() == "Y":
                    self.play()
                play = False
            elif self._guesses == 0:
                self._losses += 1
                print("YOU LOSE :(")
                print("WORD: " + self._word)
                again = input("\nPLAY AGAIN? (y/n)")
                if again.upper() == "Y":
                    self.play()
                play = False

    def _setup(self):
        print("1. Play Game \n2. Add Word To Bank")
        choice = input("Select: ")
        if choice == str(2):
            while True:
                self._add_word()
                more = input("Add more words? (y/n)")
                if not more.upper() == "Y":
                    break
        self._get_guess()
        self._word_list = self._read()
        self._word = random.choice(self._word_list)
        self._failed = ""
        return

    def _get_guess(self):
        guesses = input("Input number of guesses: ")
        try:
            guesses = int(guesses)
            if guesses > 0:
                self._guesses = guesses
                return
            else:
                print("Error, input must be larger than 0. Default amount of guesses used.")
                self._guesses = 10
                return
        except ValueError:
            print("Error, input must be a number. Default amount of guesses used.")
            self._guesses = 10
            return


hm = Hangman()
hm.play()
