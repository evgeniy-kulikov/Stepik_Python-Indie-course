# 4.5 Алгоритм Евклида
""""""

"""
Для двух чисел a  и b:
НОД — это наибольший общий делитель. 
НОК — это наименьшее общее кратное

a * b = НОД * НОК
НОК = (a * b) / НОД

a = 75
b = 120
НОК=(75 * 120) / 15
"""

# Медленный алгоритм Евклида для нахождения НОД для 2-х натуральных чисел
a = int(input())
b = int(input())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f'Нод={a}')

# Быстрый алгоритм Евклида для нахождения НОД для 2-х натуральных чисел
a = int(input())
b = int(input())
while b > 0:
    # c = a % b
    # a = b
    # b = c
    a, b = b, a % b
print(f'Нод={a}')


#  *   *   *   *   *   *   *   *   *   *   *

# Добрый, добрый Python
# https://stepik.org/lesson/567054/step/1?unit=561328
# 7.3 Алгоритм Евклида для нахождения НОД
import time


def get_nod(a, b):
    """
    Медленный алгоритм Евклида для нахождения НОД для 2-х натуральных чисел
    :param a: int
    :param b: int
    :return: int  (НОД)
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a  # можно и  return b   т.к. a  == b


# res = get_nod(8, 36)  # 4
# print(res)

# Вывод описания функции в терминале
# help(get_nod)


def get_nod_fast(a, b):
    """
    Быстрый алгоритм Евклида для нахождения НОД для 2-х натуральных чисел
    :param a: int
    :param b: int
    :return: int  (НОД)
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a


"""
Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных чисел a и b. 
В программе необходимо объявить функцию get_nod, которая принимает два аргумента a и b (натуральные числа) и 
возвращает вычисленное значение НОД(a, b).
"""
def get_nod_var(a: int, b: int) -> int:
    """
    Быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных чисел a и b
    :param a: int
    :param b: int
    :return: int (НОД)
    """
    while b:
        a, b = b, a % b
    return a


#  *  *  *   Задачи   *  *  *

# Отложенные решения на отпуск (19)
# https://stepik.org/lesson/296616/step/5?unit=278350
"""
Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель (НОД) методом вычитания
Input:  77 22
Output: 11
"""

a, b = map(int, input().split())

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)


# Отложенные решения на отпуск (20)
# https://stepik.org/lesson/296616/step/6?unit=278350
"""
Найти НОД двух чисел при помощи нахождения остатка от деления
Input:  200 30
Output: 10
"""

a, b = map(int, input().split())

while b:
    a, b = b, a % b
print(a)


# Отложенные решения на отпуск (21)
# https://stepik.org/lesson/296616/step/10?unit=278350
"""
Даны два натуральных числа A и B. Требуется найти их наименьшее общее кратное (НОК).
Input:  6 15
Output: 30
"""
a, b = map(int, input().split())

def get_nod_var(a, b):
    while b:
        a, b = b, a % b
    return a

nod = get_nod_var(a, b)
print(int((a * b) / nod))

# Без использования функции
a, b = map(int, input().split())
a1, b1 = a, b
while b > 0:
    a, b = b, a % b

nok = int((a1 * b1) / a)
print(nok)
