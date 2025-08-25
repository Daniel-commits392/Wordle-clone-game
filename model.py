from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer,String

Base=declarative_base()


class Word(Base):

    __tablename__="words"

    id=Column(Integer,primary_key=True,autoincrement=True)
    text=Column(String(5), nullable=False,unique=True)