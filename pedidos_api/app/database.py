from sqlmodel import create_engine, Session
from pathlib import Path

DATABASE_URL = "sqlite:///pedidos.db"
engine = create_engine(DATABASE_URL, echo=False)

def get_session():
    return Session(engine)
