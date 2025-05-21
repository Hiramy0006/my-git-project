import os
import json
from datetime import datetime

# Шлях до файлу з завданнями
TASKS_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Завантаження завдань з файлу"""
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, 'r', encoding='utf-8') as file:
                    self.tasks = json.load(file)
            except:
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Збереження завдань у файл"""
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=2)
    
    def list_tasks(self):
        """Показати список завдань"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n===== Список завдань =====")
        
        if not self.tasks:
            print("Немає завдань.")
            input("\nНатисніть Enter для продовження...")
            return
        
        for i, task in enumerate(self.tasks, 1):
            status = "[✓]" if task.get("completed", False) else "[ ]"
            date = task.get("date", "Немає дати")
            print(f"{i}. {status} {task['title']} (створено: {date})")
        
        input("\nНатисніть Enter для продовження...")
    
    def add_task(self):
        """Додати нове завдання"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n===== Додавання завдання =====")
        
        title = input("Введіть назву завдання: ").strip()
        
        if not title:
            print("Назва завдання не може бути порожньою!")
            input("\nНатисніть Enter для продовження...")
            return
        
        task = {
            "title": title,
            "completed": False,
            "date": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        
        self.tasks.append(task)
        self.save_tasks()
        
        print(f"\nЗавдання '{title}' успішно додано!")
        input("\nНатисніть Enter для продовження...")
    
    def complete_task(self):
        """Позначити завдання як виконане"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n===== Завершення завдання =====")
        
        if not self.tasks:
            print("Немає завдань для завершення.")
            input("\nНатисніть Enter для продовження...")
            return
        
        for i, task in enumerate(self.tasks, 1):
            status = "[✓]" if task.get("completed", False) else "[ ]"
            print(f"{i}. {status} {task['title']}")
        
        try:
            choice = int(input("\nВведіть номер завдання для завершення: "))
            if 1 <= choice <= len(self.tasks):
                task = self.tasks[choice-1]
                task["completed"] = True
                self.save_tasks()
                print(f"\nЗавдання '{task['title']}' позначено як виконане!")
            else:
                print("\nНеправильний номер завдання!")
        except ValueError:
            print("\nВведіть коректний номер!")
        
        input("\nНатисніть Enter для продовження...")
    
    def delete_task(self):
        """Видалити завдання"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n===== Видалення завдання =====")
        
        if not self.tasks:
            print("Немає завдань для видалення.")
            input("\nНатисніть Enter для продовження...")
            return
        
        for i, task in enumerate(self.tasks, 1):
            status = "[✓]" if task.get("completed", False) else "[ ]"
            print(f"{i}. {status} {task['title']}")
        
        try:
            choice = int(input("\nВведіть номер завдання для видалення: "))
            if 1 <= choice <= len(self.tasks):
                task = self.tasks.pop(choice-1)
                self.save_tasks()
                print(f"\nЗавдання '{task['title']}' успішно видалено!")
            else:
                print("\nНеправильний номер завдання!")
        except ValueError:
            print("\nВведіть коректний номер!")
        
        input("\nНатисніть Enter для продовження...")

def main():
    """Головна функція програми"""
    task_manager = TaskManager()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Task Manager")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task_manager.list_tasks()
        elif choice == '2':
            task_manager.add_task()
        elif choice == '3':
            task_manager.complete_task()
        elif choice == '4':
            task_manager.delete_task()
        elif choice == '5':
            print("\nДякую за використання Task Manager!")
            break
        else:
            print("\nНеправильний вибір! Спробуйте ще раз.")
            input("\nНатисніть Enter для продовження...")

if __name__ == "__main__":
    main()
    from task_manager import TaskManager

def print_tasks(tasks):
    """Виводить всі завдання на екран"""
    if not tasks:
        print("Немає жодного завдання!")
        return
    
    print("\nСписок завдань:")
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else " "
        print(f"{i+1}. [{status}] {task['title']}")
    print()

def main():
    manager = TaskManager()
    
    while True:
        print("\n===== Менеджер завдань =====")
        print("1. Додати завдання")
        print("2. Позначити завдання як виконане")
        print("3. Видалити завдання")
        print("4. Показати всі завдання")
        print("0. Вихід")
        
        choice = input("\nВиберіть дію: ")
        
        if choice == "1":
            title = input("Введіть назву завдання: ")
            manager.add_task(title)
            print(f"Завдання '{title}' додано!")
        
        elif choice == "2":
            print_tasks(manager.tasks)
            try:
                index = int(input("Введіть номер завдання для позначення як виконане: ")) - 1
                if manager.complete_task(index):
                    print("Завдання позначено як виконане!")
                else:
                    print("Невірний номер завдання!")
            except ValueError:
                print("Будь ласка, введіть число!")
        
        elif choice == "3":
            print_tasks(manager.tasks)
            try:
                index = int(input("Введіть номер завдання для видалення: ")) - 1
                if manager.delete_task(index):
                    print("Завдання видалено!")
                else:
                    print("Невірний номер завдання!")
            except ValueError:
                print("Будь ласка, введіть число!")
        
        elif choice == "4":
            print_tasks(manager.tasks)
        
        elif choice == "0":
            print("До побачення!")
            break
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()