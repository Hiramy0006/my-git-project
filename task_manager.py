import json
import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Завантажує задачі з JSON файлу"""
        try:
            if os.path.exists("tasks.json"):
                with open("tasks.json", 'r', encoding='utf-8') as file:
                    self.tasks = json.load(file)
                    print(f"Завантажено {len(self.tasks)} задач із файлу tasks.json")
            else:
                self.tasks = []
                print("Файл tasks.json не знайдено. Створено порожній список задач.")
                # Створюємо порожній файл
                with open("tasks.json", 'w', encoding='utf-8') as file:
                    json.dump([], file)
        except Exception as e:
            print(f"Помилка при завантаженні задач: {e}")
            self.tasks = []
        return self.tasks
    
    def save_tasks(self):
        """Зберігає задачі у JSON файл"""
        try:
            with open("tasks.json", 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=4)
            print(f"Збережено {len(self.tasks)} задач у файл tasks.json")
            return True
        except Exception as e:
            print(f"Помилка при збереженні задач: {e}")
            return False
    
    def add_task(self, title):
        """Додає нову задачу до списку"""
        new_task = {
            "title": title,
            "completed": False
        }
        self.tasks.append(new_task)
        self.save_tasks()
        return True
    
    def complete_task(self, index):
        """Відмічає задачу як виконану за індексом"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, index):
        """Видаляє задачу за індексом"""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            return True
        return False