# 10.2 Функция генератор. Создание генератора при помощи yield
""""""
"""
Инструкция yield. Общая форма
Чтобы функция могла генерировать последовательность значений и замораживать свое состояние, 
нужно, чтобы эта функция поддерживала протокол итераций. 
В этом случае функция должна возвращать результат инструкцией yield вместо инструкции return.
Формирование значений, возвращаемых из функции, может производиться одним из двух известных операторов цикла: 
for или while.


Если значения в теле функции-генератора формируются с помощью цикла for, то примерно общая форма такой функции следующая:

def FuncName(list_of_parameters):
    ...
    for value in iterObj:
        ...
        yield value

FuncName – имя функции;
list_of_parameters – список параметров, которые получает функция;
iterObj – итерированный объект. Этот объект может создаваться стандартными средствами, например методом range();
value – элемент из множества значений, сформированных в итерированном объекте iterObj.



Если функция-генератор использует цикл while для генерирования значений, то общая форма такой функции следующая

def FuncName(list_of_parameters):
    ...
    while condition:
        ...
        yield return_value

FuncName – имя функции;
list_of_parameters – список параметров, которые получает функция;
condition – условие выполнения цикла while;
return_value – значение, возвращаемое функцией.

"""


#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Создать функцию-генератор gen_squares, 
которая принимает аргумент n и генерирует квадраты чисел от 1 до n включительно. 
"""

def gen_squares(num):
    for el in range(1, num + 1):
        yield el ** 2

# n = 3
# s = gen_squares(n)
# for _ in range(n):
#     print(next(s))


# 02
"""
Создать функцию-генератор gen_fibonacci_numbers, 
которая принимает аргумент n и генерирует n-ое количество чисел Фибоначчи.
Последовательность Фибоначчи: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""
from typing import Generator

def gen_fibonacci_numbers(num: int) -> Generator[int, int]:
    a, b = 1, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


# n = 9
# s = gen_fibonacci_numbers(n)
# for _ in range(n):
#     print(next(s))



# 03
"""
Копия range
Создать функцию-генератор my_range_gen, которая копирует работу range
https://stepik.org/lesson/372106/step/7?unit=359660
"""

def my_range_gen(*args):
    if len(args) == 1:
        start,step = 0, 1
        stop = args[0]  # для ухода от кортежа
    elif len(args) == 2:
        start, stop = args
        step = 1
    elif len(args) == 3:
        start, stop, step = args
        if step == 0:
            return 'arg 3 must not be zero'
    else:
        return f'range expected at most 3 arguments, got {len(args)}'

    if step > 0:
        while stop > start:
            yield start
            start += step
    else:
        while stop < start:
            yield start
            start += step

