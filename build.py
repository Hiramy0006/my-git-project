import unittest
import subprocess
import sys
import os
import shutil

# Запускаємо тести
def run_tests():
    print("Запуск модульних тестів...")
    
    # Завантажуємо тести з файлу task_manager_test.py
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='*_test.py')
    
    # Запускаємо тести
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(suite)
    
    # Повертаємо True, якщо всі тести пройшли успішно
    return result.wasSuccessful()

# Створюємо виконуваний файл
def build_executable():
    print("Створення виконуваного файлу...")
    
    try:
        # Перевіряємо наявність PyInstaller
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], 
                      check=True)
        
        # Перевіряємо, що файл tasks.json існує
        if not os.path.exists("tasks.json"):
            print("Створюємо порожній файл tasks.json...")
            with open("tasks.json", "w") as f:
                f.write("[]")
        
        # Створюємо виконуваний файл з виводом всіх повідомлень
        result = subprocess.run(["pyinstaller", "--onefile", "main.py"], 
                      capture_output=True, text=True)
        
        # Виводимо деталі виконання
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        
        # Перевіряємо успішність виконання
        result.check_returncode()
        
        print("Виконуваний файл успішно створено в директорії dist/")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Помилка при створенні виконуваного файлу: {e}")
        print(f"STDERR: {e.stderr if hasattr(e, 'stderr') else 'Немає додаткової інформації'}")
        return False
    except Exception as e:
        print(f"Неочікувана помилка: {e}")
        return False

if __name__ == "__main__":
    # Запускаємо тести
    tests_passed = run_tests()
    
    if tests_passed:
        print("Всі тести пройшли успішно!")
        # Створюємо виконуваний файл
        build_successful = build_executable()
        
        if build_successful:
            print("Збірка завершена успішно!")
        else:
            print("Помилка при створенні виконуваного файлу")
            sys.exit(1)
    else:
        print("Модульні тести не пройшли. Збірка скасована.")
        sys.exit(1)