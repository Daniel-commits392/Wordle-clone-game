def evaluate_guess(guess: str, target: str) -> str:
    """
    Evaluates a guess against the target word.
    Returns a string with ✅, 🟨 and ❌ for each letter
    Handles duplicates correctly
    """
    
    guess = guess.lower()
    target = target.lower()
    
    result = ["❌"] * len(guess)  # Default all to ❌
    target_count = {}  # Count letters in target not yet matched
    
    # Step 2: Mark correct positions (✅)
    for i in range(len(guess)):
        if guess[i] == target[i]:
            result[i] = "✅"
        else:
            target_count[target[i]] = target_count.get(target[i], 0) + 1
            
    # Step 2: Mark wrong spot letters (🟨)
    for i in range(len(guess)):
        if result[i] == "❌" and guess[i] in target_count and target_count[guess[i]] > 0:
            result[i] = "🟨"
            target_count[guess[i]] -= 1  # use up one occurrence
    
    return "".join(result)

def evaluate_words_from_file(file_path: str, target: str):
    """
    Reads words from a file and evaluates each guess against the target word.
    """
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()
        
        # Clean up each word (strip newline, handle case)
        words = [word.strip().lower() for word in words]
        
        for guess in words:
            result = evaluate_guess(guess, target)
            print(f"Guess: {guess.capitalize()} -> {result}")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    target_word = "apple"
    evaluate_words_from_file('words.txt', target_word)