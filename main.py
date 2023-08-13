"""
Обробіть виняток IndexError, коли програма намагається отримати доступ до неправильного індексу в списку.
"""

numbers_list = ['1', '2', '3']
try:
    first_number = numbers_list[0]
    print(first_number)
    last_number = numbers_list[len(numbers_list)]
    print(last_number)
except IndexError as e:
    print(e)