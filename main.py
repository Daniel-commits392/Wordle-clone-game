import game_flow
import display

target_word = "apple"
attempts = 6

print("Welcome to Wordle!")

for _ in range(attempts):
    guess = input(f"Enter your {game_flow.WORD_LENGTH}-letter guess: ").strip()
    if not game_flow.validate_guess(guess):
        print("Invalid guess. Try again.")
        continue

    feedback = game_flow.score_guess(guess, target_word)
    display.display_feedback(guess, feedback)

    if guess.lower() == target_word:
        print("Congratulations! You guessed it right!")
        break
else:
    print(f"Out of attempts! The word was: {target_word}")
