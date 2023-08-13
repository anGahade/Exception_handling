"""
Напишіть програму, яка відкриває файл для читання
та обробляє помилку FileNotFoundError, якщо файл не знайдено.
"""

try:
    file_name = str(input("Введіть ім'я вашого файлу у форматі file_name.txt: "))
    file = open(file_name, "r")
except FileNotFoundError:
    print(f"Помилка: файл не знайдено")
