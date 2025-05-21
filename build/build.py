#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
import datetime

# Кольори для виводу інформації
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

def print_color(text, color):
    """Виводить текст з кольором"""
    print(f"{color}{text}{Colors.ENDC}")

# Інформація про проект
PROJECT_NAME = "HelloWorld"
BUILD_DIR = "build"
DIST_DIR = "dist"

# Шлях до Git - змініть його на ваш шлях до Git
# Типові шляхи для Windows:
GIT_PATH = "C:\\Program Files\\Git\\bin\\git.exe"
# Або
# GIT_PATH = "C:\\Program Files (x86)\\Git\\bin\\git.exe"

# Якщо не знайдено за цим шляхом, використовуємо просто 'git'
if not os.path.exists(GIT_PATH):
    GIT_PATH = "git"

def check_git_initialized():
    """Перевіряє, чи ініціалізовано Git-репозиторій"""
    try:
        # Виводимо повідомлення про шлях до Git
        print_color(f"Використовуємо Git за шляхом: {GIT_PATH}", Colors.YELLOW)
        
        # Спроба запустити git status
        result = subprocess.run([GIT_PATH, "status"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            return True
        else:
            print_color("Директорія не є Git-репозиторієм. Ініціалізуємо новий...", Colors.YELLOW)
            
            # Ініціалізуємо новий Git-репозиторій
            subprocess.run([GIT_PATH, "init"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Створюємо початковий коміт
            # Спочатку перевіряємо, чи є файли для коміту
            files_exist = False
            for file in ["main.py", "README.md", "build.py"]:
                if os.path.exists(file):
                    files_exist = True
                    break
            
            if files_exist:
                subprocess.run([GIT_PATH, "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                subprocess.run([GIT_PATH, "commit", "-m", "Початковий коміт"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print_color("Git-репозиторій ініціалізовано з початковим комітом.", Colors.GREEN)
            else:
                print_color("Немає файлів для початкового коміту. Створимо їх...", Colors.YELLOW)
                create_project_files()
                subprocess.run([GIT_PATH, "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                subprocess.run([GIT_PATH, "commit", "-m", "Початковий коміт"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print_color("Git-репозиторій ініціалізовано з початковим комітом.", Colors.GREEN)
            
            return True
    except FileNotFoundError:
        print_color(f"Git не знайдено за шляхом: {GIT_PATH}", Colors.RED)
        print_color("Продовжуємо без Git...", Colors.YELLOW)
        return True

def create_project_files():
    """Створює базові файли проекту, якщо вони відсутні"""
    # Створюємо main.py
    if not os.path.exists("main.py"):
        with open("main.py", "w", encoding="utf-8") as f:
            f.write("""#!/usr/bin/env python3

def main():
    \"\"\"
    Головна функція програми.
    \"\"\"
    print("Hello, World!")
    print("Це проект для лабораторної роботи з Управління ІТ-проектами")
    print("Автор: Ваше ім'я та прізвище")
    print("Група: ПП-35")

if __name__ == "__main__":
    main()
""")
        print_color("Створено файл main.py", Colors.GREEN)
    
    # Створюємо README.md
    if not os.path.exists("README.md"):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write("""# Проект для лабораторної роботи з Управління ІТ-проектами

## Опис
Цей проект створено в рамках лабораторних робіт з дисципліни "Управління ІТ-проектами".

## Структура репозиторію
- `main.py` - головний файл проекту
- `build.py` - скрипт для автоматизації збірки
- `README.md` - документація проекту

## Інструкція з використання

### Збірка проекту
Для збірки проекту виконайте:
```bash
python build.py
```

### Результати збірки
Результати збірки будуть доступні в директорії `dist/`.

## Автор
Ваше ім'я та прізвище
Група: ПП-35
""")
        print_color("Створено файл README.md", Colors.GREEN)

def create_directories():
    """Створює директорії для збірки"""
    print_color(f"Створення директорій для збірки проекту {PROJECT_NAME}...", Colors.BLUE)
    
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR)
    
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)
    
    print_color("Директорії створено успішно.", Colors.GREEN)

def git_operations():
    """Виконує необхідні Git-операції"""
    print_color("Виконання Git-операцій...", Colors.BLUE)
    
    try:
        # Отримуємо поточну гілку
        result = subprocess.run([GIT_PATH, "branch", "--show-current"], 
                              stdout=subprocess.PIPE, text=True)
        current_branch = result.stdout.strip() if result.returncode == 0 else "невідома"
        print_color(f"Поточна гілка: {current_branch}", Colors.YELLOW)
        
        # Отримуємо останній коміт
        result = subprocess.run([GIT_PATH, "log", "-1", "--pretty=format:%h - %s"], 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        last_commit = result.stdout.strip() if result.returncode == 0 else "немає комітів"
        print_color(f"Останній коміт: {last_commit}", Colors.YELLOW)
    except Exception as e:
        print_color(f"Помилка при виконанні Git-операцій: {str(e)}", Colors.RED)
        print_color("Продовжуємо з копіюванням файлів...", Colors.YELLOW)
    
    # Копіюємо файли проекту в директорію збірки
    print_color("Копіювання файлів проекту...", Colors.BLUE)
    for file in os.listdir("."):
        if file != BUILD_DIR and file != DIST_DIR and file != ".git" and not file.startswith("."):
            if os.path.isfile(file):
                shutil.copy(file, os.path.join(BUILD_DIR, file))
            elif os.path.isdir(file):
                shutil.copytree(file, os.path.join(BUILD_DIR, file))
    
    print_color("Копіювання файлів виконано успішно.", Colors.GREEN)

def build_project():
    """Створює збірку проекту"""
    print_color("Створення збірки проекту...", Colors.BLUE)
    
    # Створюємо архів проекту
    archive_name = f"{PROJECT_NAME}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.make_archive(
        os.path.join(DIST_DIR, archive_name),
        'zip',
        BUILD_DIR
    )
    
    print_color(f"Збірку проекту створено успішно: {DIST_DIR}/{archive_name}.zip", Colors.GREEN)

def main():
    print_color(f"=== Автоматизація збірки проекту {PROJECT_NAME} ===", Colors.BLUE)
    
    # Перевіряємо, чи Git ініціалізовано
    check_git_initialized()
    
    create_directories()
    git_operations()
    build_project()
    
    print_color("=== Збірка проекту завершена успішно! ===", Colors.GREEN)

if __name__ == "__main__":
    main()
import os
import sys
import unittest
import subprocess

def run_tests():
    """Функція для запуску всіх тестів"""
    print("Запуск тестів...")
    
    # Створюємо тестовий набір
    loader = unittest.TestLoader()
    
    # Знаходимо всі тести в поточній директорії
    start_dir = os.getcwd()
    suite = loader.discover(start_dir, pattern="*_test.py")
    
    # Запускаємо тести
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Перевіряємо результати тестування
    if result.wasSuccessful():
        print("Всі тести пройдені успішно!")
        return True
    else:
        print("Тести не пройдені!")
        return False

def build_project():
    """Функція для компіляції/збірки проекту"""
    print("Створення виконуваного файлу програми...")
    try:
        # Для простоти прикладу, використовуємо PyInstaller
        # (його треба встановити: pip install pyinstaller)
        subprocess.call(["pyinstaller", "--onefile", "main.py", "--name", "task_manager"])
        print("Виконуваний файл успішно створено!")
        return True
    except Exception as e:
        print(f"Помилка під час створення виконуваного файлу: {e}")
        return False

if __name__ == "__main__":
    # Запускаємо тести перед компіляцією
    tests_passed = run_tests()
    
    if tests_passed:
        # Якщо тести пройшли успішно, створюємо виконуваний файл
        build_success = build_project()
        if build_success:
            print("Проект успішно зібрано!")
        else:
            print("Помилка під час збірки проекту!")
            sys.exit(1)
    else:
        print("Не вдалося зібрати проект через помилки в тестах!")
        sys.exit(1)