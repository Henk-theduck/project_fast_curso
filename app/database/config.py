import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL_DEV = os.getenv('DATABASE_URL_DEV')

engine = create_engine(DATABASE_URL_DEV, pool_pre_ping=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)