# game_flow.py
"""
Handles the game logic for Wordle:
- Validating guesses
- Scoring each guess against the target word
"""

 # Length of the word to guess

def validate_guess(guess: str,word_length:int) -> bool:
    """
    Check if the guess is valid:
    - Must be a string
    - Must be alphabetic
    - Must match the required word length
    """
    if not isinstance(guess, str):
        return False
    guess = guess.strip()
    return len(guess) == word_length and guess.isalpha()

def score_guess(guess: str, target: str) -> list:
    """
    Compare the guess to the target word and return a list of results for each letter.
    Results:
    -    🟩= letter and position are correct
    -    🟨 = letter exists in target but wrong position
    -    ⬜ = letter not in target
    """
    guess = guess.lower()
    target = target.lower()
    feedback = ["⬜"] * len(guess)
    target_counts = {}

    # First pass: correct letters
    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            feedback[i] = "🟩"
        else:
            target_counts[t] = target_counts.get(t, 0) + 1

    # Second pass: present letters
    for i, g in enumerate(guess):
        if feedback[i] == "🟩":
            continue
        if target_counts.get(g, 0) > 0:
            feedback[i] = "🟨"
            target_counts[g] -= 1

    return feedback
