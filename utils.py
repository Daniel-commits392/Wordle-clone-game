#function to check length of the word
def check_word_length(word):
    return len(word)==5
        
#function to pick a word
def pick_largest_word(word_list):
    if not word_list:
        return None
    largest=word_list[0]
    for word in word_list:
        if word>largest:
            largest=word
    return largest

