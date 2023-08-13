"""
Реалізуйте функцію, яка ділить два числа, але обробляє помилку
**`ZeroDivisionError`**, якщо друге число дорівнює нулю.
"""


def division():
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        print("Помилка: На нуль ділити заборонено")
        return

    return result

print(division())

