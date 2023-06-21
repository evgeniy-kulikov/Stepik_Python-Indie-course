#  7.7 *args и **kwargs Python. Передача аргументов в функцию
""""""


#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Напишите функцию count_args, которая принимает произвольное количество аргументов. 
Данная функция должна возвращать количество переданных ей на вход аргументов
Output:
count_args(1, 2, 3) => 3
count_args(1, 3) => 2
count_args(2) => 1
count_args() => 0
"""

def count_args(*args):
    cnt = [*args]
    return len(cnt)

# print(count_args(1, 3))

# Короче
def count_args(*args):
    return len(args)


# 02
"""
Напишите функцию check_sum, которая принимает произвольное количество аргументов типа int.
Данная функция должна выводить not enough, если сумма всех элементов меньше 50, 
в противном случае выводить verification passed
Input:  8 11
Output: not enough
"""

def check_sum(*args: int):
    if sum(args) >= 50:
        print("verification passed")
    else:
        print('not enough')

# Короче
def check_sum(*args):
    print('not enough' if sum(args) < 50 else 'verification passed')

# check_sum(48, 2)


# 03
"""
Напишите функцию multiply, которая принимает произвольное количество числовых аргументов. 
Данная функция должна находить произведение всех переданных значений и возвращать его в качестве результата
Output:
multiply(1, 2, 3) => 6
multiply(1, 3) => 3
multiply(2) => 2
multiply() => 1
"""

def multiply(*args: int):
    res = 1
    for el in args:
        res *= el
    return res


# 04
"""
Напишите функцию  only_one_positive, которая принимает произвольное количество числовых аргументов 
и возвращает True, когда из всех переданных значений только одно положительное, 
в противном случае верните False
Output:
only_one_positive(1, 2) -> False
only_one_positive(-1, 0, -3, 5, -3) -> True
only_one_positive() -> False
"""

def only_one_positive(*args: int):
    cnt = 0
    for el in args:
        if el > 0:
            cnt += 1
    return cnt == 1


# Хорошее решение
def only_one_positive(*args):
    return sum(el > 0 for el in args) == 1

# print(only_one_positive(-1, 0, -3, 5, -3))



# 05
"""
Создать функцию print_goods, которая печатает список покупок. 
На вход она будет принимать произвольное количество значений, 
а товаром мы будем считать любые непустые строки. 
То есть числа, списки, словари и другие нестроковые объекты вам нужно будет проигнорировать. 
Функция print_goods должна печатать список товаров в виде: 
<Порядковый номер товара>. <Название товара> (см. пример ниже). 
В случае, если в переданных значениях не встретится ни одного товара, 
необходимо распечатать текст "Нет товаров"
Output:
print_goods('apple', 'banana', 'orange')
# Программа должна вывести следующее:
1. apple 
2. banana
3. orange
"""
def print_goods(*args: str):
    d = dict()
    k = 1
    for el in args:
        if type(el) == str and el != '':
            d[k] = el
            k += 1
    if d:
        for k, v in d.items():
            print(f'{k}. {v}')
    else:
        print('Нет товаров')


# Вариант
def print_goods(*args: str):
    cnt = 0
    for el in args:
        if isinstance(el, str) and el != '':
            cnt += 1
            print(f'{cnt}. {el}')
    if not cnt:
        print('Нет товаров')

# print_goods('apple', 'banana', 'orange')
# print_goods(1, True, 'Грушечка', '', 'Pineapple')
# print_goods([], {}, 1, 2)


# 06
"""
Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.
Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке 
в виде пары <Ключ> = <Значения>, 
причем ключи должны следовать в алфавитном порядке

Output:
info_kwargs(first_name="John", last_name="Doe", age=33) 
age = 33
first_name = John
last_name = Doe
"""
def info_kwargs(**kwargs):
    for el in sorted(kwargs):
        print(f'{el} = {kwargs[el]}')

# Вариант
def info_kwargs (**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

# info_kwargs(first_name="John", last_name="Doe", age=33)


# 07
"""
https://stepik.org/lesson/372076/step/16?unit=359630
Напишите функцию create_actor, 
которая принимает произвольное количество именованных аргументов 
и возвращает словарь с характеристиками актера. 
Если функции create_actor не передавать никаких аргументов, 
то она должна возвращать базовый словарь с ключами name, surname, age:
create_actor() -> {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }
Если передавать именованные параметры, которые отсутствуют в базовом словаре, они дополняются к этому словарю:
create_actor(height=190, movies=['Дедпул', 'Главный герой']) => {
    'name': 'Райан',
    'surname': 'Рейнольдс',
    'age': 46,
    'height': 190,
    'movies': ['Дедпул', 'Главный герой']
}
Если передавать именованные параметры, которые совпадают с ключами базового словаря, 
то значения в словаре должны заменяться переданными значениями:
create_actor(name='Jack', age=20) -> {
        'name': 'Jack',
        'surname': 'Рейнольдс',
        'age': 20,
    }
"""

def create_actor(name='Райан', surname='Рейнольдс', age=46, **kwargs):
    d1 = {'name': name, 'surname': surname, 'age': age}
    d2 = {k: v for k, v in kwargs.items()}  # d2 = kwargs
    res = d1 | d2
    # for k, v in res.items():
    #     print(f'{k}: {v}')
    return res

# Короче
def create_actor(name='Райан', surname='Рейнольдс', age=46, **kwargs):
    d = {'name': name, 'surname': surname, 'age': age}
    return d | kwargs

# Вариант
def create_actor(**kwargs) ->dict:
    d = {'name': 'Райан','surname': 'Рейнольдс','age': 46}
    d.update(kwargs)
    return d