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

x = float(input("Введите значение x: "))
print(f"Результат e^{x}: {maclaurin_exp(x)}")

if __name__ == "__main__":
    menu()
