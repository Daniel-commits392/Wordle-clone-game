# Wordle-clone-game Code Description:

The provided code defines two functions: evaluate_guess and evaluate_words_from_file. These functions work together to evaluate word guesses against a target word, mimicking the logic of popular word-guessing games like Wordle.

1. evaluate_guess(guess: str, target: str) -> str:

This function compares a guessed word (guess) against a target word (target) and returns a string representing how closely the guess matches the target word.

Steps:

Normalization: The guess and target are converted to lowercase to make the comparison case-insensitive.

Initial Setup:

The result list is initialized with the "❌" (cross) symbol, which signifies incorrect letters by default.

A target_count dictionary is created to keep track of how many times each letter in the target word has been matched or used. This helps handle repeated letters correctly.

Step 1 - Exact Matches (✅):

The function first checks if a letter in the guess exactly matches the corresponding letter in the target word at the same position. If a match is found, it marks the position with "✅". If no match is found, it updates the target_count for that letter.

Step 2 - Incorrect Position Matches (🟨):

Next, the function checks for letters in the guess that are present in the target but at different positions. For each such letter, if it exists in the target_count dictionary and hasn't been fully matched already, it marks the position with "🟨" (yellow) and decreases the count for that letter in target_count.

Final Output:

The function then joins the result list into a string and returns it, showing a combination of "✅", "🟨", and "❌" to represent the evaluation of the guess.

Example Output:

If the guess is "pale" and the target is "apple", the result might look like: "🟨✅❌✅".

2. evaluate_words_from_file(file_path: str, target: str):

This function reads words from a file and evaluates each one using the evaluate_guess function.

Steps:

The function tries to open the file specified by file_path and reads the lines.

Each word is stripped of whitespace and converted to lowercase.

For each word in the file, it calls evaluate_guess to check how closely the word matches the target and prints the result in a human-readable format (capitalized guess with corresponding evaluation).

Error Handling:

If the file is not found, it catches a FileNotFoundError and prints an appropriate error message.

Any other exceptions during file handling are caught and printed with the exception message.

Example Usage (if __name__ == "__main__" block):

The script sets the target word to "apple".

It then calls evaluate_words_from_file to read guesses from the file 'words.txt' and evaluates each guess against the target word "apple".

Example Flow:

Suppose 'words.txt' contains the following words:

apricot
apple
grape


When evaluate_words_from_file('words.txt', 'apple') is executed, the output would look like:

Guess: Apricot -> ❌❌❌❌❌❌
Guess: Apple -> ✅✅✅✅✅
Guess: Grape -> 🟨❌🟨❌❌

Key Features:

Correct Positioning (✅): If a letter is in the correct position, it gets marked with a green check.

Wrong Position (🟨): If a letter is present in the target but in the wrong position, it's marked with a yellow square.

Incorrect (❌): If a letter is not in the target at all, it's marked with a red cross.

Handles Duplicates: The code ensures that repeated letters are handled correctly, even if they appear multiple times in the target or guess.

This code is useful for games like Wordle where users guess a word, and you want to provide feedback in terms of correct letters, wrong letters in the wrong place, and incorrect letters.
