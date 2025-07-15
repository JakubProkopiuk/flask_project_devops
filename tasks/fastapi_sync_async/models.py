from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

from database import engine
Base.metadata.create_all(bind=engine)

