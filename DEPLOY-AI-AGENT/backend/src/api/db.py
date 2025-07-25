import os
import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL == "":
    raise NotImplementedError("`DATABASE_URL` not implemented")

DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://")

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print('Creating DB tables.....')
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
