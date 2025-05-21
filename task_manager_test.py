import unittest
import os
import json
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        """Підготовка перед кожним тестом - очищення списку задач"""
        # Створюємо новий екземпляр TaskManager для кожного тесту
        self.manager = TaskManager()
        # Очищаємо список задач
        self.manager.tasks = []
        # Зберігаємо порожній список
        self.manager.save_tasks()
    
    def tearDown(self):
        """Очищення після кожного тесту"""
        # Знову очищаємо список задач
        self.manager.tasks = []
        self.manager.save_tasks()
    
    def test_add_task(self):
        """Тест додавання задачі"""
        # Викликаємо add_task("Test Task")
        result = self.manager.add_task("Test Task")
        
        # Перевіряємо, що задача додалася успішно
        self.assertTrue(result)
        # Перевіряємо, що задача справді у списку
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]["title"], "Test Task")
        self.assertFalse(self.manager.tasks[0]["completed"])
    
    def test_complete_task(self):
        """Тест позначення задачі як виконаної"""
        # Додаємо задачу
        self.manager.add_task("Test Complete")
        
        # Позначаємо задачу як виконану
        result = self.manager.complete_task(0)
        
        # Перевіряємо, що операція пройшла успішно
        self.assertTrue(result)
        # Перевіряємо, що задача позначена як виконана
        self.assertTrue(self.manager.tasks[0]["completed"])
    
    def test_delete_task(self):
        """Тест видалення задачі"""
        # Додаємо задачу
        self.manager.add_task("To Delete")
        
        # Видаляємо задачу
        result = self.manager.delete_task(0)
        
        # Перевіряємо, що операція пройшла успішно
        self.assertTrue(result)
        # Перевіряємо, що список задач порожній
        self.assertEqual(len(self.manager.tasks), 0)
    
    def test_load_save_tasks(self):
        """Тест завантаження та збереження задач"""
        # Додаємо задачу, яка автоматично збережеться у файл
        self.manager.add_task("Persistent Task")
        
        # Створюємо новий екземпляр TaskManager, який завантажить задачі з файлу
        new_manager = TaskManager()
        
        # Перевіряємо, що задача завантажилась
        self.assertEqual(len(new_manager.tasks), 1)
        self.assertEqual(new_manager.tasks[0]["title"], "Persistent Task")

if __name__ == "__main__":
    unittest.main()