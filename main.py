
from database import SessionLocal,engine,Base
from model import Word
from utils import pick_largest_word,check_word_length


Base.metadata.create_all(bind=engine)

def main():
    session=SessionLocal()

    word_list=["apple","grape","mango","pearl","zebra","lemon"]

    for w in word_list:
        if check_word_length(w) and not session.query(Word).filter_by(text=w).first():
            session.add(Word(text=w))
    session.commit()


    words=[w.text for w in session.query(Word).all()]
    print("Words in DB:",words)


    largest=pick_largest_word(words)
    print("Largest word:",largest)

#looping part
    secret_word=largest
    word_length=len(secret_word)
    Attempts=6

    for attempt in range(1,Attempts+1):
       print(f'Attempt {attempt} out of {Attempts} attempts')
       players_guess=input('Enter your guess : ')
       lower_guess=players_guess.lower()

       if len(lower_guess)!=word_length:
          print(f'Error! Guess has to be {word_length} letters long')
          continue #this skips the current round ofthe game and asks for a new one
       if lower_guess==secret_word:
          print('👏Congrats🎉.YOU WIN!!')
          break
       

       Feedback=[]
       for i in range(word_length):
          if lower_guess[i]==secret_word[i]:
             Feedback.append('🟩') 
          elif lower_guess[i] in secret_word:
             Feedback.append('🟨')
          else:
             Feedback.append('⬜')
       print(''.join(Feedback))
             
    session.close()

if __name__=="__main__":
    main()

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

