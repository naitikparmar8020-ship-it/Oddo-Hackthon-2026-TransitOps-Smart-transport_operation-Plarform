import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load the secret keys from the .env file
load_dotenv()

# Grab the database URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# --- THE SAFETY TRIPWIRE ---
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("CRITICAL ERROR: Python cannot find DATABASE_URL. Your .env file is either missing, named incorrectly, or empty.")

# Set up the connection to Supabase
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()