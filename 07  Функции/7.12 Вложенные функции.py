# 7.12 Вложенные функции в Python
""""""

"""
Посмотрим на примере функции print_red: 
внутри данной функции переменной g нет, 
поэтому поднимаемся на уровень выше к функции colors. 
Внутри области видимости функции colors  также нету переменной g  нет, 
поэтому поднимаемся на ещё один уровень выше, 
где в глобальной области видимости мы находим эту переменную и используем её значение.
"""
g = 'grey'

def colors() -> None:
    y = 'yellow'

    def print_red() -> None:
        r = 'red'
        print(r, y, g)

    def print_blue() -> None:
        b = 'blue'
        print(b, y, g)

    print_red()
    print_blue()

colors()


"""
приоритет в области видимости отдаётся локальным областям, 
т.е. в нашем случае g не нашлась в print_red, 
поэтому поиск поднялся на уровень выше – в функцию colors 
и здесь была найдена такая переменная и взялось это значение, 
в то время, как значение глобальной переменной g было проигнорировано.
Также есть возможность изменить переменную при помощи nonlocal
"""
g = 'grey'

def colors() -> None:
    y = 'yellow'
    g = 'green'

    def red() -> None:
        nonlocal y
        r = 'red'
        print(r, y, g)  # red yellow green
        y = 'изменили цвет'

    def blue() -> None:
        b = 'blue'
        print(b, y, g)  # blue изменили цвет green

    red()
    blue()

colors()
# red yellow green
# blue изменили цвет green


""""""
# Возврат вложенных функций в качестве результата
def get_math_func(operation="+"):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    if operation == "+":
        return add
    elif operation == "-":
        return subtract


"""
Как проаннотировать саму функцию get_math_func, 
ведь результат ее работы будет объект-функция. 
Для этого нужно импортировать из модуля typing тип Callable 
и списком ему проаннотировать значения следующим образом:
"""
from typing import Callable


def get_math_func(operation: str) -> Callable[[int, int], int]:
    def add(a: int, b: int) -> int:
        return a + b

    def subtract(a: int, b: int) -> int:
        return a - b

    if operation == "+":
        return add
    elif operation == "-":
        return subtract



#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Исправьте код так, чтобы на экран вывело bye и hello
def outer() -> None:
    def say_hello() -> None:
        print('hello')

    def say_bye() -> None:
        print('bye')


say_hello()
say_bye()

"""

def outer() -> None:
    def say_hello() -> None:
        print('hello')

    def say_bye() -> None:
        print('bye')

    say_bye()
    say_hello()


outer()


# Другой подход
class outer():
    @staticmethod
    def say_hello() -> None:
        print('hello')

    @staticmethod
    def say_bye() -> None:
        print('bye')


outer.say_bye()
outer.say_hello()


# 02
"""
https://stepik.org/lesson/372077/step/7?unit=359631
"""
def calculate(x:float, y:float, operation:str='a') -> None:

    if operation not in 'asmd':
        print('Ошибка. Данной операции не существует.')

    def addition(x, y, operation):
        if operation == 'a':
            print(float(x + y))

    def subtraction(x, y, operation):
        if operation == 's':
            print(float(x - y))

    def division(x, y, operation):
        if operation == 'd':
            if y != 0:
                print(x / y)
            else:
                print('На ноль делить нельзя!')

    def multiplication(x, y, operation):
        if operation == 'm':
            print(float(x * y))

    addition(x, y, operation)
    subtraction(x, y, operation)
    division(x, y, operation)
    multiplication(x, y, operation)


# Короче
def calculate(x: float, y: float, operation: str = 'a') -> None:
    def addition():
        print(float(x + y))

    def subtraction():
        print(float(x - y))

    def division():
        print(x / y if y != 0 else 'На ноль делить нельзя!')

    def multiplication():
        print(float(x * y))

    operation_dict = {'a': addition, 's': subtraction, 'd': division, 'm': multiplication}

    if operation in operation_dict:
        return operation_dict[operation]()
    else:
        print('Ошибка. Данной операции не существует')


# calculate(2, 1, 'a')
# calculate(2, 0)
# calculate(2, 0, 'w')

