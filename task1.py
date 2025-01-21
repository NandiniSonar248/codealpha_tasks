"""Task 1:-Design a text-based Hangman game. The program
selects a random word, and the player guesses one
letter at a time to uncover the word. You can set a
limit on the number of incorrect guesses allowed."""

import random

def select_random_word():
    """Selects a random word from a predefined list."""
    word_list = ["python", "hangman", "programming", "development", "challenge", "computer"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Returns the word with guessed letters revealed and others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main function to play the Hangman game."""
    print("Welcome to Hangman!")
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    else:
        print("\nGame Over! You've run out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()
