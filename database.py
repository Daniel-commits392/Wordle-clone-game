
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL, create_engine, text

from model import Base


db_credentials={
    "drivername":"postgresql+psycopg2",
    "username":"postgres.lsjljzfjtkuebozgqhcj",
    "password":"GQIIYnF8VZJbtjJ3",
    "host":"aws-1-ap-southeast-1.pooler.supabase.com",
    "port":"5432",
    "database":"postgres"
}

Database_URL=URL.create(**db_credentials)
engine=create_engine(Database_URL,echo=True,future=True)

Base.metadata.create_all(bind=engine)

SessionLocal=sessionmaker(bind=engine, autoflush=False, autocommit=False)