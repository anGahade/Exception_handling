"""
Створіть функцію, яка приймає два числа від користувача
та обробляє помилку, якщо введені дані не є числами.
"""


def get_two_numbers():
    x = input("Введіть перше число: ")
    y = input("Введіть друге число: ")

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Ви ввели не числа. Спробуйте ще.")
        return get_two_numbers()

    return x, y


print(get_two_numbers())
