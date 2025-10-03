from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config

engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()