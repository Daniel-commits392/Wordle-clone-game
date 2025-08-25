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

    session.close()

if __name__=="__main__":
    main()