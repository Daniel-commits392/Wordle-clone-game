
from database import SessionLocal,engine,Base
from model import Word
from utils import pick_largest_word,check_word_length
from game_flow import validate_guess,score_guess


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
    attempts=6

    for attempt in range(1,attempts+1):
       print(f'Attempt {attempt} out of {attempts} attempts')
       players_guess=input('Enter your guess : ')
       lower_guess=players_guess.lower()

       if not validate_guess(lower_guess,word_length):
            print(f'Invalid guess. Please enter a {word_length}-letter alphabetic word.')
            continue
         
       if lower_guess==secret_word:
          print('👏Congrats🎉.YOU WIN!!')
          break
       else:
           feedback=score_guess(lower_guess,secret_word)
           print(''.join(feedback))

    else:
          print(f'Out of attempts! The word was {secret_word}')

    
    session.close()

if __name__=="__main__":
    main()

