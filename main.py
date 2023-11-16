import words_fetcher
import random


def check_previous_guesses():
    if guess in previous_guesses:
        print("You have already guessed this")
        return True
    return False


def congratulate_user():
    print(f"Congratulations, you won! your words: {guesses}")


def is_game_over():
    return guessed == WORDS_TO_WIN or errors == ERRORS_TO_LOSE


guessed = 0
errors = 0

guesses = []

WORDS_TO_WIN = 5
ERRORS_TO_LOSE = 3

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
full_list = words_fetcher.fetch_words(min_letters=3, max_letters=9)
word = words[random.randrange(0, len(words))]

print(f"Can you make up {WORDS_TO_WIN} words from letters in word provided by me?")
print(f"Your word is '{word}'")

previous_guesses = set()

while not is_game_over():
    guess = input("Your next take: ")
    check_previous_guesses()
    if guess in full_list:
        guessed += 1
        guesses.append(guess)
        if guessed == WORDS_TO_WIN:
            congratulate_user()
            exit()
        print(f"That's right! {WORDS_TO_WIN - guessed} to go")
    else:
        errors += 1
        print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
    previous_guesses.add(guess)


