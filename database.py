from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

DATABASE_URL = "sqlite:///database.db"  # یه دیتابیس SQLite می‌سازه

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models  # این باید به مدل‌های دیتابیس‌ت اشاره کنه
    Base.metadata.create_all(bind=engine)
from models import db

def init_db():
    db.create_all()