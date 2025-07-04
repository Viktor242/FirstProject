import json
from typing import List

class Task:
    def __init__(self, text: str, status: str = "Не начата"):
        self.text = text
        self.status = status

    def to_dict(self):
        return {"text": self.text, "status": self.status}

    @staticmethod
    def from_dict(data):
        return Task(data["text"], data["status"])

class TaskManager:
    def __init__(self, storage_file: str = "tasks.json"):
        self.tasks: List[Task] = []
        self.storage_file = storage_file
        self.load_tasks()

    def add_task(self, text: str):
        if text:
            self.tasks.append(Task(text))
            self.save_tasks()

    def delete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def change_status(self, index: int, new_status: str):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = new_status
            self.save_tasks()

    def get_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=2)

    def load_tasks(self):
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
