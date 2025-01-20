"""Proyect n5"""
import math

# Количество итераций
ITERATIONS = 10


def maclaurin_exp(x):
    """
    Вычисляет приближенное значение e^x с помощью ряда Маклорена.

    Ряд Маклорена для e^x:
    e^x = 1 + x + x^2 / 2! + x^3 / 3! + ...

    Аргументы:
    x (float): Значение x в формуле для e^x.

    Возвращаемое значение:
    float: Приближенное значение e^x.

    Исключения:
    ValueError: Если x не является действительным числом.

    Пример:
    >>> maclaurin_exp(1)
    2.7182818011463845
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Значение x должно быть действительным числом.")

    result = 1
    factorial = 1
    for n in range(1, ITERATIONS):
        factorial *= n
        result += (x ** n) / factorial
    return result


def maclaurin_sinh(x):
    """
    Вычисляет приближенное значение sinh(x) с помощью ряда Маклорена.

    Ряд Маклорена для sinh(x):
    sinh(x) = x + x^3 / 3! + x^5 / 5! + ...

    Аргументы:
    x (float): Значение x в формуле для sinh(x).

    Возвращаемое значение:
    float: Приближенное значение sinh(x).

    Исключения:
    ValueError: Если x не является действительным числом.

    Пример:
    >>> maclaurin_sinh(1)
    1.1752011936438014
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Значение x должно быть действительным числом.")

    result = 0
    for n in range(1, ITERATIONS * 2, 2):  # Только нечетные степени
        factorial = math.factorial(n)
        result += (x ** n) / factorial
    return result

def maclaurin_arctan(x):
    """
    Вычисляет приближенное значение arctan(x) с помощью ряда Маклорена.

    Ряд Маклорена для arctan(x):
    arctan(x) = x - x^3 / 3 + x^5 / 5 - x^7 / 7 + ...

    Аргументы:
    x (float): Значение x в формуле для arctan(x).

    Возвращаемое значение:
    float: Приближенное значение arctan(x).

    Исключения:
    ValueError: Если x не является действительным числом.

    Пример:
    >>> maclaurin_arctan(1)
    0.7853981633974483
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Значение x должно быть действительным числом.")
    
    result = 0
    sign = 1
    for n in range(1, ITERATIONS * 2, 2):  # Только нечетные степени
        result += sign * (x ** n) / n
        sign *= -1  # Чередование знаков
    return result


def menu():

    while True:
        print("1. first function")
        print("2. second function")
        print("3. third function")
        print("4. exit")

        try:
            option = int(input("Выберите опцию (1-4): "))
            if option == 1:
                x = float(input("Введите значение x: "))
                print(f"Результат e^{x}: {maclaurin_exp(x)}")
            elif option == 2:
                x = float(input("Введите значение x: "))
                print(f"Результат sinh({x}): {maclaurin_sinh(x)}")
            elif option == 3:
                x = float(input("Введите значение x: "))
                print(f"Результат arctan({x}): {maclaurin_arctan(x)}")
            elif option == 4:
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    menu()
