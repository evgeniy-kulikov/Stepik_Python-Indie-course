# 6.6 Методы словаря
""""""

# Метод .clear()
# очищает весь словарь. В итоге после вызова получится пустой словарь
d = {1: 'one', 2: 'two', 3: 'three'}
d.clear()  # {}

# Метод get()
"""
Метод get() – позволяет получить значение ключа.  
Нужно указать внутри скобок один аргумент – ключ, значение которого хотим получить. 
Если ключа в словаре нет, то выведет None, но если в метод get() внести второй аргумент, 
то вместо None будет появляться это значение.
"""
d = {1: 'one', 2: 'two', 3: 'three'}
d.get(1)  # one
d.get(5)  # None
d.get(5, 'No such key')  # No such key


# Метод setdefault()
"""
Метод setdefault()  - получает значение ключа. 
Похож на метод get(), однако при обращении к несуществующему ключу 
он вносит в словарь новую пару ключ-значение. 
Значением будет второй аргумент, который был передан в этот метод, либо же None, 
если в методе только один аргумент
"""
d = {1: 'one', 2: 'two', 3: 'three'}
d.setdefault(1)  # one
print(d)  # {1: 'one', 2: 'two', 3: 'three'}

d.setdefault(6)  # None
print(d)  # {1: 'one', 2: 'two', 3: 'three', 6: None}

d.setdefault(7, 'семь')
print(d)  # {1: 'one', 2: 'two', 3: 'three', 6: None, 7: 'семь'}


# Метод pop()
"""
Метод pop() – возвращает значение, находящееся под указанным ключом, 
а из самого словаря удаляется пара с данным ключом.

Вызов метода без указания ключа, либо же без существующего ключа, приводит к ошибке TypeError
"""
d = {1: 'one', 2: 'two', 3: 'three'}
d.pop(2)  # two
print(d)  # {1: 'one', 3: 'three'}

deleted_value = d.pop(1)  # one
print(d)  # {3: 'three'}


# Метод popitem()
"""
Метод popitem() удалит и вернет двойной кортеж (key, value) из словаря. 
Пары возвращаются с конца словаря, в порядке LIFO (последним пришёл - первым ушёл).

Только начиная с версии Python-3.7 гарантируется порядок LIFO. 
В предыдущих версиях метод .popitem() возвращал бы произвольную пару ключ/значение.

При попытке удаления элементов из пустого словаря возникает ошибка KeyError
"""
d = {1: 'one', 2: 'two', 3: 'three'}
d.popitem()  # (3, 'three')
print(d)  # {1: 'one', 2: 'two'}

lang = {}
lang['ru'] = 'Русский'
lang['eng'] = 'Английский'
#  lang = {'ru': 'Русский', 'eng': 'Английский'}
lang.popitem()  # ('eng', 'Английский')  # LIFO (последним пришёл - первым ушёл)
lang.popitem()  # ('ru', 'Русский')


#  Метод keys()
# позволяет получить все ключи словаря

d = {1: 'one', 2: 'two', 3: 'three'}
d.keys()  # dict_keys([1, 2, 3])
keys = list(d.keys())  # [1, 2, 3]


#  Метод values()
# позволяет получить все значения словаря

d = {1: 'one', 2: 'two', 3: 'three'}
d.values()  # dict_values(['one', 'two', 'three'])
vals = list(d.values())  # ['one', 'two', 'three']


#  Метод items()
# возвращает коллекцию, в которой содержатся все пары «ключ-значение» в виде кортежей

d = {1: 'one', 2: 'two', 3: 'three'}
d.items()  # dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
couples = list(d.items())  # [(1, 'one'), (2, 'two'), (3, 'three')]


# Метод update()
"""
Метод update() обновляет словарь элементами из другого словаря. 
Другими словами, метод сливает(мержит от английского «merge») один словарь в другой: 
добавляются новые ключи из другого словаря, 
при совпадении ключей записывается значение из переданного словаря
"""
d = {1: 'one', 2: 'two', 3: 'three'}
w = {4: 'four', 5: 'five'}
d.update(w)  # {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


# Обход элементов словаря в цикле
"""
Словари относятся к коллекциям как и списки, строки и кортежи. Все коллекции объединяет то, 
что по их элементам можно итерироваться: обходить элементы коллекции при помощи цикла for

По умолчанию в словаре используются ключи в качестве значений при итерации цикла for
"""
d = {1: 'one', 2: 'two', 3: 'three'}
for el in d:
    print(el, end=' ')  # 1 2 3

# одинаковый вариант
d = {1: 'one', 2: 'two', 3: 'three'}
for el in d.keys():
    print(el, end=' ')  # 1 2 3

# итерироваться не по ключам, а по значениям словаря:
d = {1: 'one', 2: 'two', 3: 'three'}
for el in d:
    print(d[el], end=' ')  # one two three

d = {1: 'one', 2: 'two', 3: 'three'}
for el in d.values():
    print(el, end=' ')  # one two three


# можно сразу итерироваться и по ключу и по его значению
d = {1: 'one', 2: 'two', 3: 'three'}
for el in d.items():
    print(el, end=' ')  # (1, 'one') (2, 'two') (3, 'three')

d = {1: 'one', 2: 'two', 3: 'three'}
for key, val in d.items():
    print(key, val)
# 1 one
# 2 two
# 3 three


#  *  *  *   Задачи   *  *  *


"""
Есть два словаря, нужно в словарь d2 вмержить словарь d1 при помощи метода update
В качестве ответа выведите словарь d2
"""
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
d2.update(d1)
print(d2)  # {'x': 300, 'y': 200, 'z': 777, 'a': 100, 'b': 200, 'c': 333}


"""
Система регистрации
https://stepik.org/lesson/296967/step/4?unit=278695
https://www.youtube.com/watch?v=s7RS9lxpxwk&feature=youtu.be
"""
n = int(input())
password = {}

for _ in range(n):
    login = input()
    if login not in password:
        password[login] = 0
        print("OK")
    else:
        val = password.get(login)
        password[login] = val + 1
        print(login + str(val + 1))


# вариант
n = int(input())
d_pass = {}

for _ in range(n):
    login = input()

    if login not in d_pass:
        d_pass[login] = 0
        print('OK')
    else:
        d_pass[login] += 1
        d_pass[f'{login}{d_pass[login]}'] = 0
        print(f'{login}{d_pass[login]}')


"""
https://stepik.org/lesson/296967/step/5?unit=278695
На вход будет поступать название города в переменную city. 
Найти какой стране принадлежит введенный город. 
Если страна успешно найдена, необходимо вывести сообщение:
INFO: <City> is a city in <Country>
в противном случае:
ERROR: Country for {City} not found
"""
countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
place = None

for el in countries:
    if city in countries.get(el):
        place = el

if place:
    print(f'INFO: {city} is a city in {place}')
else:
    print(f'ERROR: Country for {city} not found')

# Хорошее решение
city = input()
result = f"ERROR: Country for {city} not found"

for el in countries:
    if city in countries[el]:
        text = f"INFO: {city} is a city in {el}"

print(result)



"""
https://stepik.org/lesson/296967/step/6?unit=278695
При помощи метода pop переименуйте в словаре 'user' следующие ключи:
ключ 'password' в ключ 'secret'
ключ 'last_name' в ключ 'surname'
"""
user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17"
}

user['secret'] = user.pop('password')
user['surname'] = user.pop('last_name')


"""
https://stepik.org/lesson/296967/step/7?unit=278695
Напишите код для преобразования списка из целых чисел произвольной длины в словарь, 
вложенность которого зависит от длины списка.
Input:  1 2 3
Output: {1: {2: 3}}

Input:  7 38 20 49 87 69
Output: {7: {38: {20: {49: {87: 69}}}}}
"""
# lst = [7, 38, 20, 49, 87, 69]
lst = list(map(int, input().split()))

d = {lst[-2]: lst[-1]}

for el in range(-3, -(len(lst) + 1), -1):
    d = {lst[el]: d}

print(d)


# Хорошее решение
lst = list(map(int, input().split()))

d = lst[-1]

for el in lst[-3::-1]:
    d = {el: d}

print(d)
