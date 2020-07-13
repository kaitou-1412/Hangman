import json
import random


def selected_word():
    with open("words.json", "r") as f:
        words_list = json.load(f)["data"]
    return random.choice(words_list)


def decrypt(c, l):
    if c in l:
        return c
    return "*"


print("Starting a game of hangman...")
incorrect_attempts = 8
remaining_attempts = incorrect_attempts
print("\nIncorrect Attempts allowed:", incorrect_attempts)
print("Selecting a word")
word = selected_word()
prev_guesses = set()
wrong_guesses = set()
crypted_word = "*"*len(word)
attempt_number = 0
while remaining_attempts != 0:
    attempt_number += 1
    print("\nWord:", crypted_word)
    print("Remaining attempts:", remaining_attempts)
    if wrong_guesses != set():
        print("You've already tried:", end=" ")
        print(*wrong_guesses, sep=" ")
    if attempt_number == 1:
        print("Choose a letter:", end=" ")
    else:
        print("Choose the next letter:", end=" ")
    letter = input().lower()
    if letter in word:
        if letter in prev_guesses:
            print("You've already tried", letter)
            remaining_attempts -= 1
        else:
            prev_guesses.add(letter)
            print(letter, "is indeed in the word!")
            crypted_word = "".join([decrypt(og_letter, prev_guesses) for og_letter in word])
    else:
        remaining_attempts -= 1
        wrong_guesses.add(letter)
        print(letter, "is not in the word")
    if crypted_word == word:
        print("\nWord:", word, "\nWell played!!!")
        break
    if remaining_attempts == 0:
        print("\nBetter luck next time! The word was", word)