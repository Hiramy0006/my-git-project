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

def check_git_initialized():
    """Перевіряє, чи ініціалізовано Git-репозиторій"""
    try:
        result = subprocess.run(["git", "status"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        print_color("Git не знайдено в системі. Встановіть Git перед продовженням.", Colors.RED)
        sys.exit(1)

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
    
    # Отримуємо поточну гілку
    result = subprocess.run(["git", "branch", "--show-current"], 
                          stdout=subprocess.PIPE, text=True, check=True)
    current_branch = result.stdout.strip()
    print_color(f"Поточна гілка: {current_branch}", Colors.YELLOW)
    
    # Отримуємо останній коміт
    result = subprocess.run(["git", "log", "-1", "--pretty=format:%h - %s"], 
                          stdout=subprocess.PIPE, text=True, check=True)
    last_commit = result.stdout.strip()
    print_color(f"Останній коміт: {last_commit}", Colors.YELLOW)
    
    # Копіюємо файли проекту в директорію збірки
    print_color("Копіювання файлів проекту...", Colors.BLUE)
    for file in os.listdir("."):
        if file != BUILD_DIR and file != DIST_DIR and file != ".git" and not file.startswith("."):
            if os.path.isfile(file):
                shutil.copy(file, os.path.join(BUILD_DIR, file))
            elif os.path.isdir(file):
                shutil.copytree(file, os.path.join(BUILD_DIR, file))
    
    print_color("Git-операції виконано успішно.", Colors.GREEN)

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
    if not check_git_initialized():
        print_color("Git-репозиторій не знайдено. Запустіть цей скрипт в директорії з Git-репозиторієм.", Colors.RED)
        sys.exit(1)
    
    create_directories()
    git_operations()
    build_project()
    
    print_color("=== Збірка проекту завершена успішно! ===", Colors.GREEN)

if __name__ == "__main__":
    main()