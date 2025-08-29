# display.py
from colorama import Fore, Style

def print_rules():
    """
    Prints the game rules.
    """
    print("""
Welcome to Wordle!
Rules:
- You have 6 attempts to guess the 5-letter word.
- Correct letter in correct position: GREEN
- Correct letter in wrong position: YELLOW
- Letter not in word: GRAY
    """)

def show_guess(guess, feedback):
    """
    Shows each guess with colors:
    Green for correct, Yellow for present, Gray for absent.
    """
    colored_output = ""
    for letter, result in zip(guess, feedback):
        if result == "correct":
            colored_output += Fore.GREEN + letter.upper() + Style.RESET_ALL + " "
        elif result == "present":
            colored_output += Fore.YELLOW + letter.upper() + Style.RESET_ALL + " "
        else:
            colored_output += Fore.LIGHTBLACK_EX + letter.upper() + Style.RESET_ALL + " "
    print(colored_output)

def show_all_guesses(guesses):
    """
    Prints all previous guesses.
    """
    print("\nYour guesses so far:")
    for guess, feedback in guesses:
        show_guess(guess, feedback)
    print()
