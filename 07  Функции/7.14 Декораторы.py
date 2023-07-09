# 7.14 Декораторы
""""""


def decorator(func):

    def inner():
        print('start decorator')
        func()
        print('finish decorator')

    return inner

def say():
    print('hello world')


var = decorator(say)
var()
# start decorator
# hello world
# finish decorator

# переменной var хранится ссылка не на функцию say(), а на функцию inner()
print(say)  # <function decorator.<locals>.inner at 0x00000269CD09F0A0>



# Передаем аргумент в функцию inner(n)
def decorator(func):

    def inner(n):
        print('start decorator')
        func(n)
        print('finish decorator')

    return inner

def say(name):
    print('hello', name)

var = decorator(say)
var('Vasya')
# start decorator
# hello Vasya
# finish decorator


# При создании декоратора, все аргументы, которые он принимает (вне зависимости есть ли они или нет),
# лучше добавлять их через *args и **kwargs.
def decorator(func):

    def inner(*args, **kwargs):
        print('start decorator')
        func(*args, **kwargs)
        print('finish decorator')

    return inner

def say(name, surname, age):
    print('hello', name, surname, age)

var = decorator(say)
var('Vasya', 'Ivanov', 30)

# start decorator
# hello Vasya Ivanov 30
# finish decorator


# Одной функции можно добавить несколько декораторов.
# Первой вызывается функция header() и она возвращает функцию inner,
# результатом которой будут строки h1, hello…, /h1
# и этот результат будет передаваться внутрь функции table
def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

def say(name, surname, age):
    print('hello', name, surname, age)

var = table(header(say))
var('Vasya', 'Ivanov', 30)
# <table>
# <h1>
# hello Vasya Ivanov 30
# </h1>
# </table>


# Стоит также отметить, что функции таким образом не декорируют. Декораторы «навешивают» при помощи @
def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner


@header  # var = header(say)
def say(name, surname, age):
    print('hello', name, surname, age)


say('Vasya', 'Ivanov', 30)
# <h1>
# hello Vasya Ivanov 30
# </h1>


# Можно «навесить» и несколько декораторов подобным образом:
def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


# say = header(table(say))

@header
@table
def say(name, surname, age):
    print('hello', name, surname, age)

say('Vasya', 'Ivanov', 30)

# <h1>
# <table>
# hello Vasya Ivanov 30
# </table>
# </h1>


""""""
""""""
# Проблема – при использовании декоратора теряется имя и строка документации декорированной функции.
# Для решения этой проблемы применяется использование декоратора wraps,
# который можно импортировать из модуля functools.
# Навешиваете декоратор wraps на вложенную функцию inner, передаете ему исходную функцию, которая декорируется.

from functools import wraps

def table(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

def sqr(x):
    """
    Функция возводит в квадрат
    :param x:
    :return:
    """
    print(x**2)

var = table(sqr)
print(var)
# <function sqr at 0x00000257D7D4F0A0>
print(sqr.__name__)
# sqr
help(sqr)
"""
Help on function sqr in module __main__:

sqr(x)
    Функция возводит в квадрат
    :param x:
    :return:
"""



#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Напишите декоратор text_decor, 
который оборачивает вызов декорированной функции фразами «Hello» и «Goodbye!»
"""

# декоратор
def text_decor(func):

    def inner(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')
    return inner


@text_decor
def simple_func():
    print('I just simple python func')

simple_func()
# Hello
# I just simple python func
# Goodbye!


@text_decor
def multiply(num1, num2):
    print(num1 * num2)

multiply(3, 5)
# Hello
# 15
# Goodbye!


# 02
"""
Напишите декоратор repeater, который дважды вызывает декорированную функцию

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7) # после этого распечатается две строки со значением 14
multiply(5, 3) # после этого распечатается две строки со значением 15
"""

def repeater(func):

    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return inner

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7)
# 14
# 14


# 03
"""
https://stepik.org/lesson/372080/step/10?unit=359634
Напишите декоратор double_it, который возвращает удвоенный результат вызова декорированной функции

@double_it
def multiply(num1, num2):
    return num1 * num2

res = multiply(9, 4) # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)

@double_it
def get_sum(*args):
    return sum(args)

res = get_sum(1, 2, 3, 4, 5)
print(res) # печатает 30
"""

def double_it(func):

    def inner(*args, **kwargs):
        rez = func(*args, **kwargs) * 2
        return rez

    return inner



@double_it
def multiply(num1, num2):
    return num1 * num2

res = multiply(9, 4)
print(res)  # 72

@double_it
def get_sum(*args):
    return sum(args)

res = get_sum(1, 2, 3, 4, 5)
print(res)  # 30


# 04
"""
https://stepik.org/lesson/372080/step/14?unit=359634
Напишите декоратор add_args, 
который добавляет к переданным аргументам еще два значения: 
строку begin в начало аргументов, строку end в конец. 
Также декоратор должен сохранить первоначальное имя декорируемой функцию и ее строку документации
"""
from functools import wraps

def add_args(func):

    @wraps(func)
    def inner(*args):
        rez = func('begin', *args, 'end')
        return rez

    return inner


@add_args
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


@add_args
def find_max_word(*args):
    """
    Возвращает слово максимальной длины
    """
    return max(args, key=len)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
print(find_max_word('hello', 'world', 'my', 'name is', 'Artem'))
print(find_max_word.__name__)
print(find_max_word.__doc__.strip())



# 05
"""
https://stepik.org/lesson/372080/step/15?unit=359634
Напишите декоратор validate_args, 
который валидирует (проверяет на корректность) переданные аргументы. 
Аргументы нужно проверить на следующее:

Должно быть передано именно два аргумента. Если передано меньшее количество, декоратор должен вернуть строку
Not enough arguments

Если передано более двух аргументов, то возвращаем строку
Too many arguments

Оба аргумента должны быть целыми числами. Если хотя бы одно из них не целое число, возвращаем строку
Wrong types

Если обе проверки выполняются, возвращаем результат декорируемой функции
"""
from functools import wraps


def validate_args(func):
    @wraps(func)
    def inner(*args):
        if len(args) < 2:
            rez = 'Not enough arguments'
        elif len(args) > 2:
            rez = 'Too many arguments'
        elif not all([type(el) == int for el in args]):
            rez = 'Wrong types'
        else:
            rez = func(*args)
        return rez

    return inner


@validate_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


a = add_numbers(4)
print(a)  # 'Not enough arguments'
b = add_numbers(4, 5, 6)
print(b)  # 'Too many arguments'
c = add_numbers('4', '5')
print(c)  # 'Wrong types'
d = add_numbers(4, 5)
print(d)  # 9


# 06
"""
https://stepik.org/lesson/372080/step/16?unit=359634
Декоратор-запоминатор
"""
from functools import wraps

# def memoize(func):
#     mem_dic = dict()
#
#     @wraps(func)
#     def inner(num):
#         if num in mem_dic:
#             return mem_dic[num]
#         else:
#             rez = func(num)
#             mem_dic[num] = rez
#         return rez
#     return inner

# Короче
def memoize(func):
    hash_fib = dict()

    @wraps(func)
    def inner(num):
        if num not in hash_fib:
            hash_fib[num] = func(num)
        return hash_fib.get(num)
    return inner

@memoize
def fibonacci(n):
    """
    Возвращает n-ое число Фибоначчи
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# a = fibonacci(50)
# print(a)  # 12586269025
