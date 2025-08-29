from game_flow import validate_guess, score_guess, WORD_LENGTH

def print_rules():
    print("\nWelcome to Wordle!")
    print("Rules:")
    print(f"- You have 6 attempts to guess the {WORD_LENGTH}-letter word.")
    print("- Correct letter in correct position: GREEN")
    print("- Correct letter in wrong position: YELLOW")
    print("- Letter not in word: GRAY\n")

def main():
    target_word = "apple"  # The word to guess
    attempts = 6
    previous_guesses = []  # Stores guesses and their feedback

    print_rules()

    for attempt in range(attempts):
        guess = input(f"Enter your {WORD_LENGTH}-letter guess: ")

        # Validate guess
        if not validate_guess(guess, WORD_LENGTH):
            print("Invalid guess! Please enter a valid word.")
            continue

        # Score the guess and store result
        feedback = score_guess(guess, target_word)
        previous_guesses.append((guess, feedback))

        # Show feedback and previous guesses
        print(f"Feedback: {feedback}")
        print("Previous guesses:")
        for g, f in previous_guesses:
            print(f"{g} -> {f}")

        # Win condition
        if guess.lower() == target_word:
            print("\nCongratulations! You guessed the word!")
            break
    else:
        print(f"\nGame Over! The correct word was '{target_word}'.")

if __name__ == "__main__":
    main()
