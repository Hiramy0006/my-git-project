import unittest
import os
import json
from task_manager import TaskManager

class TaskManagerTest(unittest.TestCase):
    
    def setUp(self):
        """Підготовка перед кожним тестом"""
        self.task_manager = TaskManager()
        # Очищення списку завдань перед кожним тестом
        self.task_manager.tasks = []
        # Переконуємось, що файл з тестовими даними не впливає на тести
        if os.path.exists("tasks.json"):
            os.remove("tasks.json")
    
    def test_add_task(self):
        """Перевіряє чи додається задача правильно"""
        self.task_manager.add_task("Test Task")
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0]["title"], "Test Task")
        self.assertEqual(self.task_manager.tasks[0]["completed"], False)
    
    def test_complete_task(self):
        """Перевіряє чи можна позначити задачу як виконану"""
        self.task_manager.add_task("Test Complete")
        self.task_manager.complete_task(0)
        self.assertTrue(self.task_manager.tasks[0]["completed"])
    
    def test_delete_task(self):
        """Перевіряє чи видаляється задача з переліку"""
        self.task_manager.add_task("To Delete")
        self.task_manager.delete_task(0)
        self.assertEqual(len(self.task_manager.tasks), 0)
    
    def test_load_save_tasks(self):
        """Перевіряє чи працює збереження задач з tasks.json"""
        self.task_manager.add_task("Persistent Task")
        # Створюємо новий екземпляр для завантаження збережених даних
        new_manager = TaskManager()
        self.assertEqual(len(new_manager.tasks), 1)
        self.assertEqual(new_manager.tasks[0]["title"], "Persistent Task")
        self.assertEqual(new_manager.tasks[0]["completed"], False)
    
    def tearDown(self):
        """Очищення після кожного тесту"""
        # Видаляємо тестовий файл даних
        if os.path.exists("tasks.json"):
            os.remove("tasks.json")

if __name__ == "__main__":
    unittest.main()
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