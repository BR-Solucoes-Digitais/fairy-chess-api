from sqlmodel import SQLModel, create_engine

from fairy_chess.config import DATABSE_URI



engine = create_engine(DATABSE_URI)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)