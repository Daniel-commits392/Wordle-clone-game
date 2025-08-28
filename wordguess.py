import random

WORD_LIST = ["apple", "grape", "mango", "peach", "berry"]

def get_random_word():
    """Pick a random word from the list."""
    return random.choice(WORD_LIST)

def get_player_guess(word_length=5):
    """Prompt the player for a guess with letters only and correct length."""
    while True:     #the
        guess = input(f"Enter a {word_length}-letter word: ").strip()

        if guess.isalpha() and len(guess) == word_length:
            return guess.lower()
        else:
            print(f"Invalid input. Enter exactly {word_length} letters only!")

def check_guess(guess, secret_word):
    """Give feedback on the guess like Wordle: correct, close, wrong."""
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append("🟩")  # the letter is in the correct position
        elif guess[i] in secret_word:
            feedback.append("🟨")  # the letter is in the word but bin the wrong position
        else:
            feedback.append("⬛")  # the letter is not in the word at all
    return "".join(feedback)

def play_game():
    secret_word = get_random_word()
    attempts = 6
    print("Welcome to Wordle!")

    while attempts > 0:
        guess = get_player_guess(len(secret_word))
        result = check_guess(guess, secret_word)
        print(result)

        if guess == secret_word:
            print("🎉 Congratulations! You guessed the word!")
            break

        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"Game Over! The word was '{secret_word}'.")

if __name__ == "__main__":
    play_game()
