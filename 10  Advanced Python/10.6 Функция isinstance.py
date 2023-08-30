# 10.6 Встроенная функция isinstance
""""""

"""
Функция isinstance позволяет проверить к какому типу объектов относится ваше значение.
Параметры isinstance()
Метод isinstance() принимает два параметра:

object — непосредственно сам объект, который нам необходимо проверить
classinfo — класс, тип, или кортеж классов и типов
Метод isinstance() возвращает следующие значения:

True, если объект является экземпляром classinfo
False в случае если объект не является экземпляром

"""

numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers, 'instance of list?', result)
#  [1, 2, 3] instance of list? True

result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result)
#  [1, 2, 3] instance of dict? False

result = isinstance(numbers, (dict, list))
print(numbers, 'instance of dict or list?', result)
#  [1, 2, 3] instance of dict or list? True

number = 5
result = isinstance(number, list)
print(number, 'instance of list?', result)
#  5 instance of list? False

result = isinstance(number, int)
print(number, 'instance of int?', result)
#  5 instance of int? True


# По историческим причинам bool является подклассом int, а True/False также экземпляром int
number = True
result = isinstance(number, int)
print(number, 'instance of int?', result)
#  True instance of int? True

number = False
result = isinstance(number, int)
print(number, 'instance of int?', result)
#  False instance of int? True


#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Написать функцию count_strings, которая принимает произвольное количество аргументов. 
Функция должна среди всех переданных значений найти только строки, 
найти их количество и вернуть в качестве результата.

count_strings(1, 2, 'hello', [2, 3, 4], True) => 1
count_strings('am', 'world', 'hello', 'is') => 4
count_strings() => 0 
count_strings(True, False) => 0
"""

def count_strings(*args) -> int:
    rez = list(filter(lambda el: isinstance(el, str), args))
    return len(rez)

# Короче
def count_strings(*args):
    return sum(isinstance(el, str) for el in args)


# 02
"""
Написать функцию find_keys, которая принимает произвольное количество именованных аргументов. 
Функция должна отобрать только те имена параметров, у которых значения являются списками или кортежами. 
Функция find_keys должна собрать все имена таких параметров в список, 
отсортировать их по алфавиту вне зависимости от регистра букв 
и вернуть в качестве результата.

find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]) => ['A', 'b', 't', 'W']
find_keys(name='Bruce', surname='Wayne') => []
find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)) => ['Also', 'marks']
"""


def find_keys(**kwargs):
    d_out = {k: v for k, v in dict(kwargs).items() if isinstance(v, (list, tuple))}
    return sorted(list(d_out),key=str.lower)


# Хорошее решение
def find_keys(**kwargs):
    keys = [k for k, v in kwargs.items() if isinstance(v, (list, tuple))]
    keys.sort(key=str.lower)
    return keys

# print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
