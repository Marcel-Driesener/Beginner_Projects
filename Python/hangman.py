import random

def hangman():
    """
    Plays a game of hangman.
    """

    words = ["python", "java", "javascript", "c++", "ruby", "swift", "golang"]
    word = random.choice(words)

    guessed_letters = set()
    tries = 6

    while tries > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(display_word)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if display_word == word:
                print("Congratulations! You won!")
                break
        else:
            print("Incorrect guess.")
            tries -= 1

        if tries == 0:
            print("Game over! The word was:", word)

if __name__ == "__main__":
    hangman()