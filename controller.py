from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Task, Base
from abstract_controller import ToDoControllerInterface


class ToDoController(ToDoControllerInterface):
    def __init__(self):
        self.__setup_database()

    def __setup_database(self) -> None:
        self.engine = create_engine('sqlite:///todo.db')
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def add_task(self, task: str) -> None:
        new_task = Task(task=task)
        with self.session() as session:
            session.add(new_task)
            session.commit()

    def get_tasks(self) -> List[Task]:
        with self.session() as session:
            return session.query(Task).all()

    def delete_task(self, task_id: int) -> None:
        with self.session() as session:
            task = session.query(Task).get(task_id)
            if not task:
                return
            session.delete(task)
            session.commit()
