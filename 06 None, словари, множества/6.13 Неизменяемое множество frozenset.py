#  6.13 Неизменяемое множество frozenset
""""""

"""
frozenset представляет собой такое же множество как и тип данных set , 
но с единственным и главным отличием - frozenset является неизменяемым объектом.
"""
# Создание пустого неизменяемого множества
froz = frozenset()  # frozenset()
empty = frozenset([])  # frozenset()
empty = frozenset('')  # frozenset()

"""
Создать frozenset можно на основании любой другой итерируемой коллекции, а именно  на основании:
- строки
- списка
- кортежа
- множества
- словаря
"""
fr_abra = frozenset('abracadabra')
print(fr_abra)  # frozenset({'c', 'b', 'a', 'd', 'r'})

fr_nums = frozenset([2, 1, 2, 4, 5, 2, 1])
print(fr_nums)  # frozenset({1, 2, 4, 5})

lang = {'eng':'Английский', 'ru':'Русский'}
print(frozenset(lang))  # frozenset({'ru', 'eng'})

my_set = {1, 2, 2, 3}
print(frozenset(my_set))  # frozenset({1, 2, 3})


"""
Операции над frozenset
Все операции, которые можно применять над обычным множеством set, можно использовать и над frozenset
"""
# Нахождение длины frozenset
a = frozenset([1, 3, 2])
len(a)  # 3
# Проверка на нахождение
a = frozenset([1, 2, 3])
print(2 in a)  # True

# Поиск максимума и минимума
# Функции min(), max() позволяют найти минимальный и максимальный элемент неизменяемого множества,
# если там хранятся элементы одного типа
num = frozenset([1, 2, 3])
max(num)  # 3

st = frozenset(['a', 'b', 'c'])
min(st)  # 'a'


# Суммирование элементов
# Просуммировать элементы frozenset(если оно состоит исключительно из чисел):
a = frozenset((2, 4, 5, 7, 8, 9))
print(sum(a)) # 35


"""
Сортировка frozenset
При помощи функции sorted() можно отсортировать frozenset, если в нем содержатся однородные элементы.
Результатом работы функции sorted() всегда будет являться список
"""
my_set = frozenset([8, 4, 7, 5, 2, 3, 6])
sorted_list = sorted(my_set)  # [2, 3, 4, 5, 6, 7, 8]

st = frozenset(['c', 'b', 'a'])
sorted_list = sorted(st)  # ['a', 'b', 'c']


"""
Операции, которые нельзя выполнять над frozenset^
- Индексация
- Функция reversed
"""


"""
Методы frozenset
frozenset является неизменяемым объектом, 
поэтому вызов метода множества не окажет влияние на состояние элементов неизменяемого множества , 
у которого вызывается метод. Если вы хотите изменить объект frozenset необходимо пользоваться присваиванием.
"""
# Метод .copy()
person = {"name": "Jack", "age": 21, "Country": "India"}

frozen_dict = frozenset(person)
print(f'{frozen_dict = }')  #

a = frozen_dict.copy()
print(f'{a = }')  # a = frozenset({'Country', 'age', 'name'})

# Метод .difference()
frozen1 = frozenset([1, 2, 3, 4])
frozen2 = frozenset([3, 4, 5, 6])
frozen_diff = frozen1.difference(frozen2)  # frozenset({1, 2})
frozen_diff = frozen2.difference(frozen1)  # frozenset({5, 6})


# Метод .union()
frozen1 = frozenset([1, 2, 3, 4])
frozen2 = frozenset([3, 4, 5, 6])
frozen_union = frozen1.union(frozen2)  # frozenset({1, 2, 3, 4, 5, 6})


#  Метод .intersection()
frozen1 = frozenset([1, 2, 3, 4])
frozen2 = frozenset([3, 4, 5, 6])
frozen_intersection = frozen1.intersection(frozen2)  # frozenset({3, 4})


#  Метод .symmetric_difference()
frozen1 = frozenset([1, 2, 3, 4])
frozen2 = frozenset([3, 4, 5, 6])
frozen_symm_diff = frozen1.symmetric_difference(frozen2)  # frozenset({1, 2, 5, 6})


"""
Использование frozenset в словаре
Так как объект frozenset является неизменяемым, его можно использовать в качестве ключа в словаре. 
Обычные множества set не могли быть использованы в качестве ключа.
Объект frozenset хранит свои элементы без учета порядка и с удалением повторяющихся элементов, 
поэтому два набора, построенные в разном порядке, будут эквивалентными ключами в словаре — они одинаковы.
"""
print(frozenset([1,2,2,3,3]) == frozenset([3,2,1,1,1]))  # True

d = {}
d[frozenset([1,1,2,3])] = 'hello'
print(d)  # {frozenset({1, 2, 3}): 'hello'}
print(d[frozenset([1,2,3,3])])  # hello
print(d[frozenset([3,3,3,2,1,1,1])])  # hello
print(d[frozenset([2,1,3])])  # hello


#
#  *  *  *   Задачи   *  *  *
#


# 1
my_frozen = frozenset()
print(my_frozen)


# 2
"""
В переменную my_frozen, сохраните объект frozenset , содержащий 77 элементов
Сами элементы это последовательность из 77-ми следующих чисел: 7, 77, 777, 7777, 77777, 777777, ..... 
В конце этой последовательности стоит число из 77-ми цифр 7, на предпоследнем месте - число из 76-ти цифр 7
Выводить ничего не нужно, только создать переменную my_frozen и правильно ее заполнить
"""
ls = [int('7' * el) for el in range(1, 78)]
my_frozen = frozenset(ls)