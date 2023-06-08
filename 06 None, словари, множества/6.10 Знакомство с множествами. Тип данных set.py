#  6.10 Знакомство с множествами. Тип данных set
""""""
# Множество (тип данных set) – это неупорядоченная коллекция уникальных элементов

# Способы создания множества
a = {1, 2, 3}

# При помощи функции set() мы можем преобразовать другую коллекцию в множество
a = set('abcdeabc')  # {'e', 'd', 'a', 'b', 'c'}

b = set([1, 2, 3, 2, 3, 1, 3])  # {1, 2, 3}

c = set(range(5))  # {0, 1, 2, 3, 4}


# Создание пустого множества. Использованием функции set() без указания аргументов.
a = set()  # <class 'set'>

# Но нельзя задать пустыми скобками {} так будет создан словарь.
b = {}  # <class 'dict'>

# Множество может состоять только из неизменяемых объектов.
"""
К неизменяемым объектам, относятся:
строки
числа int и float
кортежи
frozenset
"""

# Из вложенных списков НЕЛЬЗЯ
b = [[1, 2, 3]]
b = set(b)  # TypeError: unhashable type: 'list'


"""
Операции над множествами
"""

# Нахождение длины множества
a = {1, 2, 3}
len(a)  # 3

# Проверка на нахождение
a = {1, 2, 3}
print(2 in a)  # True
print(5 in a)  # False
print(4 not in a)  # True
print(1 not in a)  # False

# Поиск максимума и минимума в множестве
a = {1, 2, 3}
min(a)  # 1
max(a)  # 3

# Функции min(), max() можно использовать только если множество состоит из однотипных элементов
a = {1, 2, 'hi', 4, 5}
min(a)  # TypeError: '>' not supported between instances of 'str' and 'int'

# Суммирование элементов множества

# суммировать элементы множества возможно, если оно состоит исключительно из чисел
a = {2, 4, 5, 7, 8, 9}
sum(a)  # 35

a = {1, 2, 'hi', 4, 5}
sum(a)    # TypeError: unsupported operand type(s) for +

# Сортировка множества
"""
При помощи функции sorted() можно отсортировать множество, если в нем содержатся однородные элементы
Результат работы функции sorted() всегда является список
"""
my_set = {8, 4, 7, 5, 2, 3, 6}
sorted_list = sorted(my_set)  # [2, 3, 4, 5, 6, 7, 8]

my_set = {"a", "b", "c"}
sorted_list = sorted(my_set)  # ['a', 'b', 'c']

# НО !!!
# Функцию reversed() нельзя использовать для множества,
# так как множество представляет собой неупорядоченную коллекцию.

# К элементам множества нельзя обращаться по индексу


#
#  *  *  *   Задачи   *  *  *
#


# 2
"""
https://stepik.org/lesson/772400/step/11?unit=774833
"""
my_list = [56, 59, 53, 75, 62, 61, 75, 65, 59, 62, 64, 53,
           54, 62, 69, 53, 55, 62, 54, 66, 55, 57, 58, 75,
           72, 55, 51, 56, 71, 66, 57, 56, 59, 73, 68, 57,
           50, 54, 62, 68, 59, 64, 59, 59, 71, 68, 57, 54, 53, 72]

my_set = set(my_list)
res = sum(my_set) / len(my_set)
print(res)  # 61.95


# 3
"""
Девушка или Юноша
https://stepik.org/lesson/772400/step/12?unit=774833
"""
name = input().lower()
m = 'IGNORE HIM!'
f = 'CHAT WITH HER!'
res = set(name)
print(f if len(res) % 2 == 0 else m)


# 4
"""
Не смешите мои подковы
https://stepik.org/lesson/772400/step/13?unit=774833
"""
color = list(map(int, input().split()))
print(color)
print(4 - len(set(color)))


# 5
"""
Не смешите мои подковы
https://stepik.org/lesson/772400/step/14?unit=774833
Input:  *
Output: *
"""
# Преобразуем строку в список символов (без пробелов)
st = [char for char in input().lower() if char != ' ']
res = len(set(st))
print('YES' if res == 26 else 'NO')

# По условию задачи дается только одно слово, а не предложение
print('YES' if len(set(input().lower())) == 26 else 'NO')


# 6
"""
Красивый год
https://stepik.org/lesson/772400/step/15?unit=774833
Задан номер года, найдите наименьший номер года, который строго больше заданного и в котором все цифры различны.
Input:  1987
Output: 2013
"""
num_in = int(input()) + 1

while len(set(str(num_in))) != 4:
    num_in += 1
print(num_in)


# 7
"""
Антон и буквы
https://stepik.org/lesson/772400/step/16?unit=774833
Input:  {a, b, c}
Output: 3
"""

s = [el for el in input() if el.isalpha()]
print(len(set(s)))


# Лучше
s ={el for el in input() if el.isalpha()}
print(len(s))
