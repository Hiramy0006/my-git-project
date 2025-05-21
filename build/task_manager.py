import json
import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, title):
        """Додає нове завдання до списку"""
        task = {
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def complete_task(self, index):
        """Позначає завдання як виконане"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, index):
        """Видаляє завдання за індексом"""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            return True
        return False
    
    def save_tasks(self):
        """Зберігає завдання у файл"""
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)
    
    def load_tasks(self):
        """Завантажує завдання з файлу"""
        if os.path.exists("tasks.json"):
            try:
                with open("tasks.json", "r") as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = []