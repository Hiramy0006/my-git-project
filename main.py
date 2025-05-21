import os
import json
from datetime import datetime

# Шлях до файлу з завданнями
TASKS_FILE = "tasks.json"

from task_manager import TaskManager

def main():
    # Створюємо екземпляр TaskManager
    manager = TaskManager()
    
    # Виводимо поточні задачі
    print("Поточні задачі:")
    for i, task in enumerate(manager.tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['title']}")
    
    # Додаємо нову задачу для демонстрації
    print("\nДодаємо нову задачу...")
    manager.add_task(f"Нова задача від {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    # Виводимо оновлений список
    print("\nОновлений список задач:")
    for i, task in enumerate(manager.tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

if __name__ == "__main__":
    try:
        main()
        # Додаємо паузу, щоб вікно не закривалося автоматично
        print("\nПрограма виконана успішно!")
        input("Натисніть Enter для завершення...")
    except Exception as e:
        print(f"Сталася помилка: {e}")
        input("Натисніть Enter для завершення...")