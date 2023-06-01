#  6.7 Ситуации, где полезно использовать словарь
""""""


#  *  *  *   Задачи   *  *  *

# 1
"""
Поднять зарплату Бреду до 8500 и затем вывести измененный словарь.
"""
workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}

workers['employer3']['salary'] = 8500
print(workers)

# Вариант
for el in workers:
    if workers[el]['name'] == 'Brad':
        workers[el]['salary'] = 8500

print(workers)


# 2
"""
программе поступает на вход строка, необходимо подсчитать 
сколько раз встретилась каждая буква в этой строке без учета регистра, 
при этом цифры и символы пунктуации нужно пропустить. 
Ответ нужно сохранить в словаре, в котором ключ - буква, а значение - количество раз, 
сколько эта буква встретилась в строке. В качестве ответа нужно вывести словарь
Input:  aabbbc
Output: {'a': 2, 'b': 3, 'c': 1}
"""
d = dict()
s = input().lower()

for el in s:
    if el.isalpha():
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
print(d)

# Короче
for el in s:
    if el.isalpha():
        d[el] = d.get(el, 0) + 1  # вместо блока if-else  (см. выше)
print(d)


# 3
"""
https://stepik.org/lesson/296968/step/5?unit=278696
Во сколько обойдется данная покупка?
Input:  *
Output: *
"""
supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}

total = 0
for el in supermarket:
    total += supermarket[el]["quantity"] * supermarket[el]["price"]
print(total)  # 528.37

# короче
for el in supermarket.values():
    total += el.get("quantity") * el.get("price")
print(total)  # 528.37


# 4
"""
Анаграмма
Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
Программа получает на вход две строки S1 и S2. 
Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO
Input:  abc
        cba
Output: YES
"""
s1, s2 = input(), input()
d1, d2 = dict(), dict()

for el in s1:
    d1[el] = d1.get(el, 0) + 1

for el in s2:
    d2[el] = d2.get(el, 0) + 1

print('YES' if d1 == d2 else 'NO')

# вариант 1 (добавляем проверку на длину строки из-за zip())
s1, s2 = input(), input()
d1, d2 = dict(), dict()

for el1, el2 in zip(s1, s2):
    d1[el1] = d1.get(el1, 0) + 1
    d2[el2] = d2.get(el2, 0) + 1

print('YES' if d1 == d2 and len(s1) == len(s2) else 'NO')

# вариант 2 (недостаток - много лишних итераций)
s1, s2 = input(), input()
d1 = {i: s1.count(i) for i in s1}
d2 = {i: s2.count(i) for i in s2}
print('YES' if d1 == d2 else 'NO')


# 5
"""
https://stepik.org/lesson/296968/step/7?unit=278696
Азбука Морзе.
дан английский текст. Закодируйте его с помощью азбуки Морзе.
Весь текст записан в единственной строке. 
Текст состоит из английских букв и пробелов, других символов в тексте нет. 
В тексте не может быть двух или более пробелов подряд.
Input:  Houston we have a problem
Output: •••• ——— ••— ••• — ——— —• 
        •—— • 
        •••• •— •••— • 
        •— 
        •——• •—• ——— —••• •—•• • —— 
"""
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}

st = input().lower().split()

for word in st:
    res = ''
    for el in word:
        res += morze.get(el) + ' '
    print(res)

# короче
lst = [[morze[el] for el in word] for word in st]
[print(*i) for i in lst]


# 6
"""
https://stepik.org/lesson/296968/step/8?unit=278696
создать словарь, где ключами будут имена, а значениями словарь из трех ключей: salary, gender и passport
Input:  [
        ('Bob Moore', 330000, 'M', '1635777202'),
        ('Gina Moore', 12500, 'F', '1639999999'),
        ]
Output: {
            'Bob Moore': {
                'salary': 330000,
                'gender': 'M',
                'passport': '1635777202'
            },
            'Gina Moore': {
                'salary': 12500,
                'gender': 'F',
                'passport': '1639999999'
            }
       }
"""
persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]
# from pprint import pprint

data = dict()

for el in persons:
    data.update({el[0]: {'salary': el[1], 'gender': el[2], 'passport': el[3]}})

# Генератор словарей
data = {
    name: {'salary': salary, 'gender': gender, 'passport': passport}
    for name, salary, gender, passport in persons}


# расставляем в словаре-значении ключи в нужном порядке
data = dict()

for el in persons:
    val = dict()
    val['salary'] = el[1]
    val['gender'] = el[2]
    val['passport'] = el[3]
    data[el[0]] = val

# pprint(data)


# 7

"""
https://stepik.org/lesson/296968/step/9?unit=278696
достать определенные данные из словаря 'data'
получить значения ключа first_name у всех элементов и вывести их в алфавитном порядке, каждое имя с новой строки
"""
data = {
    "my_friends": {
        "count": 10,
        "people": [{
            "first_name": "Kurt",
            "id": 621547005,
            "last_name": "Cobain",
            "bdate": "31.8.2005"
        }, {
            "first_name": "Виолетта",
            "id": 484200150,
            "last_name": "Кастилио",
        }, {
            "first_name": "Иринка",
            "id": 21886133,
            "last_name": "Бушуева",
            "bdate": "28.8.1942"
        }, {
            "first_name": "Данил",
            "id": 282456573,
            "last_name": "Греков",
            "bdate": "4.7.2002"
        }, {
            "first_name": "Валентин",
            "id": 184902932,
            "last_name": "Долматов",
            "bdate": "25.5"
        }, {
            "first_name": "Евгений",
            "id": 620469646,
            "last_name": "Шапорин",
            "bdate": "6.12.1982"
        }, {
            "first_name": "Ангелина",
            "id": 622328862,
            "last_name": "Краснова",
            "bdate": "4.11.1995"
        }, {
            "first_name": "Иван",
            "id": 576015198,
            "last_name": "Вирин",
            "bdate": "2.2.1915"
        }, {
            "first_name": "Паша",
            "id": 386922406,
            "last_name": "Воронов",
            "bdate": "27.9"
        }, {
            "first_name": "Ольга",
            "id": 622170942,
            "last_name": "Савченкова",
            "bdate": "20.12"
        }]
    }
}


ls = []

for el in data["my_friends"]['people']:
    ls += [el['first_name']]

ls.sort()

for el in ls:
    print(el)


# генератор списков
ls = [el['first_name'] for el in data["my_friends"]['people']]
ls.sort()
print(*ls, sep='\n')
