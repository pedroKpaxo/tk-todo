from sqlalchemy import create_engine, Column, Integer, String, DateTime
import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"<Task(task='{self.task}', date='{self.date}')>"


# Database setup
engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
