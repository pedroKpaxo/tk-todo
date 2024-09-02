from abc import ABC, abstractmethod
from typing import List
from models import Task


class ToDoControllerInterface(ABC):
    @abstractmethod
    def add_task(self, task: str) -> None:
        pass

    @abstractmethod
    def get_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        pass
