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
    
    # Step 1: Mark correct positions (✅)
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