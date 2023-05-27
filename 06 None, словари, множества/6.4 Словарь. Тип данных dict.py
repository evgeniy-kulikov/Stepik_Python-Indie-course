# 6.4 Словарь. Знакомство с типом данных dict
""""""

# Способы создания словаря
# 1 - открыть фигурные скобки {}
cities = {
   "moscow": 495,
   "saint petersburg": 812,
   "penza": 8412
}
# {'moscow': 495, 'saint petersburg': 812, 'penza': 8412}

# 2 - при помощи функции dict()
# Внутри функции dict() пишем ключ и присваиваем ему значение (значение ключей мы пишем без кавычек)
# такой способ создания словарей используется только тогда, когда в качестве ключа выступает строковой тип данных.
# Использование чисел или иных типов данных приведёт к ошибке
cities = dict(moskva=495, piter=812, penza=8412)
# {'moskva': 495, 'piter': 812, 'penza': 8412}

# 2.2 Вложенный список,
# элементами которого будут списки, состоящие из двух элементов: первое будет ключом, второе – значением.
a = [['moskva', 495], ['piter', 812], ['penza', 8412]]
cities = dict(a)
# {'moskva': 495, 'piter': 812, 'penza': 8412}

# Способы создания пустого словаря
# 1 - при помощи пустых фигурных скобок {}
d = {}

#  2 - при помощи функции dict() с пустыми параметрами
d = dict()


""" ключи и значения словаря """
# связь в паре ключ:значение односторонняя:
# мы можем по ключу получить значение, а по значению ключ мы не получим

# Обращение по ключу

d = {1: 'one', 2: 'two', 'ru': 'Русский'}
d[2] # two
d['ru'] # Русский

# При обращении к ключу, которого в списке нет, мы получим ошибку KeyError.

# чтобы добавить новое значение в словарь необходимо обратится по новому ключу и присвоить туда значение
# словарь[новый ключ] = значение
lang = {'eng':'Английский', 'ru':'Русский'}
# {'eng': 'Английский', 'ru': 'Русский'}

lang['fra'] = 'Французский'
# {'eng': 'Английский', 'ru': 'Русский', 'fra': 'Французский'}

# Изменение существующей пары ключ:значение
# Если присвоить новое значение уже существующему ключу, то мы заменим старое значение.
lang = {'eng': 'Английский', 'ru': 'Русский'}
lang['ru'] = 'Russian'
# {'eng': 'Английский', 'ru': 'Russian'}

# Удаление существующей пары ключ:значение
d = {1: 'one', 2: 'two', 3: 'three'}
del d[2]
# {1: 'one', 3: 'three'}

# При попытке удалить ключ, которого нет в словаре,  возникнет ошибка KeyError

"""
Требования к ключу словаря:
Ключом может быть только неизменяемый объект

К неизменяемым объектам относятся:
целые(тип int) и вещественные(тип float) числа
строки (тип str)
None
кортежи (тип tuple) 
неизменяемые множества (тип frozenset)

К изменяемым объектам относятся:
списки (тип list)
множества (тип set)
сами словари (тип dict)
Из этого следует, что ключом словаря не может быть список, множество или словарь.
"""

# Можно выбрать любой тип данных в качестве значения словаря
# Для красивого вывода словаря можно использовать функцию pprint из модуля pprint
from pprint import pprint

person = {}
s = 'IVANOV IVAN 19 Samara SGU 4 5 5 5 4 3 5 3'
s = s.split()
# ['IVANOV', 'IVAN', '19', 'Samara', 'SGU', '4', '5', '5', '5', '4', '3', '5', '3']

person['last_name'] = s[0]
person['first_name'] = s[1]
person['age'] = int(s[2])
person['city'] = s[3]
person['university'] = s[4]
# {'last_name': 'IVANOV', 'first_name': 'IVAN', 'age': 19, 'city': 'Samara', 'university': 'SGU'}

person['marks'] = []
for el in s[5:]:
    person['marks'].append(int(el))

pprint(person)
"""
{'age': 19,
 'city': 'Samara',
 'first_name': 'IVAN',
 'last_name': 'IVANOV',
 'marks': [4, 5, 5, 5, 4, 3, 5, 3],
 'university': 'SGU'}
 """


#  *  *  *   Задачи   *  *  *


# https://stepik.org/lesson/761760/step/5?thread=solutions&unit=763882
person = dict(name='Vasya', surname='Petrov', age=25)
print(person)


# https://stepik.org/lesson/761760/step/8?unit=763882
sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}

print(sweet["name"])
print(sweet["calories"])
print(sweet["id"])


# https://stepik.org/lesson/761760/step/10?unit=763882
days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
n = int(input())
print(days[n])


# https://stepik.org/lesson/761760/step/12?unit=763882
sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125
}

sweet['weight'] = 230
sweet['have_topping'] = True
sweet['name'] = 'SuperCake'
sweet['calories'] = 350
print(sweet)


# https://stepik.org/lesson/761760/step/13?unit=763882
sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125
}

del sweet['ppu']
del sweet['type']
print(sweet)


"""
На вход программе поступает целое число n. Необходимо создать словарь, 
который будет включать в себя ключи от 1 до n, 
а значениями соответствующего ключа будет значение ключа в квадрате.
Input:  5
Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
n = int(input())
lst = [[el, el ** 2] for el in range(1, n + 1)]
d = dict(lst)
print(d)

# Вариант (генератор словарей)
n = int(input())
d = {el: el ** 2 for el in range(1, n + 1)}
print(d)


"""
Напишите программу, которая печатает словарь alphabet, 
где ключи  - строчные английские символы, 
а значения - порядковые номера букв в алфавите начиная с 1.
Начало вашего словаря должны быть таким {"a": 1, "b": 2 ... }
Английский алфавит можно взять в переменной ascii_lowercase из модуля string
"""

from string import ascii_lowercase as s  # 'abcdefghijklmnopqrstuvwxyz'

val_num = [el for el in range(1, len(s) + 1)]
alphabet = {key: val for key, val in zip(s, val_num)}

print(alphabet)


# Хорошее решение
from string import ascii_lowercase as a

alphabet = {a[i]: i + 1 for i in range(len(a))}
print(alphabet)


# Вариант
from string import ascii_lowercase

alphabet = {}
for i in range(len(ascii_lowercase)):
    alphabet[ascii_lowercase[i]] = i + 1
print(alphabet)
