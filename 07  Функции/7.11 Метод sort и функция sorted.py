#  7.11 Сортировка коллекций. Метод sort и функция sorted
""""""

"""
sort – это метод списка, а sorted – это функция. 
Отсюда следует, что sort можно применять только к спискам, причём вызывать как метод. 
А в функция sorted может сортировать не только списки, но и другие коллекции
"""

# sort(self, *, key=..., reverse=...)

a = [4, -10, 43, -300, 54, 89, -34]
a.sort()  # a = [-300, -34, -10, 4, 43, 54, 89]

b = sorted(a)  # [-300, -34, -10, 4, 43, 54, 89]
# sorted(__iterable, *, key, reverse=...)
"""
Функция sorted может принять до трёх аргументов: iterable, key, reverse
b = sorted(a, key=func, reverse=True/False)
"""

# Отсортируем по последней цифре числа в списке
def get_last_digit(num: int) -> int:
    return num % 10

a = [4, 10, 43, 300, 54, 289, 34, 8, 749]
b = sorted(a, key=get_last_digit)  # b = [10, 300, 43, 4, 54, 34, 8, 289, 749]


# Чтобы выполнить сортировку в обратном порядке без применения аргумента reverse
# можно в функции get_last_digit указать обратное значение
def get_last_digit(num: int) -> int:
    return -(num % 10)

a = [4, 10, 43, 300, 54, 289, 34, 8, 749]
b = sorted(a, key=get_last_digit)  # b = [289, 749, 8, 4, 54, 34, 43, 10, 300]


"""
Можно сделать двойной критерий сортировки. 
Первый критерий сортировки будет первичным: применяться в первую очередь, 
а при равенстве значений будет задействован второй критерий. 
Например, числа 10 и 300 оба заканчиваются на 0, но если сортировать ещё и по второй цифре, 
то значение 10 будет больше, чем 300

В этом примере нужно понимать, что сортировка сначала происходит по первому значению, 
и только в том случае, если последние цифры равны, 
то произойдет сортировка и по второму значению между этими элементы. 
"""
def get_last_digit(num: int) -> int:
    return num % 10, num // 10 % 10

a = [4, 10, 43, 300, 54, 289, 34, 8, 749]
b = sorted(a, key=get_last_digit)  # b = [300, 10, 43, 4, 34, 54, 8, 749, 289]


# Заглавная буква по таблице ASCII будет иметь код меньше кода любой строчной буквы
a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
sorted(a)  # ['BBB', 'DDD', 'ZZZ', 'aaa', 'eee', 'www']

#  отсортировать  список в алфавитном порядке, несмотря на регистр букв
a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(a, key=str.lower))  # ['aaa', 'BBB', 'DDD', 'eee', 'www', 'ZZZ']


a = ['ZZZ 79', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 5', 'www 14']
b = sorted(a, key=lambda x: int(x.split()[1]))
# b = ['BBB 5', 'www 14', 'eee 43', 'aaa 45', 'ZZZ 79', 'DDD 800']


#  Есть две пары, которые имеют одинаковые числа (eee 43', 'BBB 43', ...  'ZZZ 800', 'DDD 800')
# Отсортируем их дополнительно по строке через второе условие
a = ['ZZZ 800', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 43', 'www 14']
b = sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0]))
# b = ['www 14', 'BBB 43', 'eee 43', 'aaa 45', 'DDD 800', 'ZZZ 800']


""""""
""""""
# Как отсортировать словарь
""""""

heroes = {
    'Spider-Man': 80,
    'Batman': 65,
    'Superman': 85,
    'Wonder Woman': 70,
    'Flash': 70,
    'Iron Man': 65,
    'Thor': 90,
    'Aquaman': 65,
    'Captain America': 65,
    'Hulk': 87,
}

for key, value in sorted(heroes.items(),
                         key=lambda item: item[1]):
    # словарь теперь отсортирован по значениям, при этом сортировки по ключам не происходит
    print(key, value)
"""
Batman 65
Iron Man 65
Aquaman 65
Captain America 65
Wonder Woman 70
Flash 70
Spider-Man 80
Superman 85
Hulk 87
Thor 90
"""


for k, v in sorted(heroes.items(),
                   key=lambda item: (item[1], item[0])):
    # словарь отсортирован по значениям и в случае одинаковых значений он отсортирован и по ключу.
    print(k, v)
"""
Aquaman 65
Batman 65
Captain America 65
Iron Man 65
Flash 70
Wonder Woman 70
Spider-Man 80
Superman 85
Hulk 87
Thor 90
"""


#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Напишите программу, которая отсортирует список subject_marks по возрастанию оценок. 
Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел
Input:  subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
Output: History 82
        English 88
        Science 90
        Physics 93
        Maths 97
"""
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]

ls = sorted(subject_marks, key=lambda el: el[1])

for el in ls:
    print(*el)


# 02
"""
Напишите программу, которая отсортирует список subject_marks по по убыванию оценок.. 
Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел
"""
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]

ls = sorted(subject_marks, key=lambda el: -el[1])

for el in ls:
    print(*el)


# 03
"""
Напишите программу, которая отсортирует список subject_marks по убыванию оценок. 
Предметы, имеющие одинаковые оценки, должны быть отсортированы в алфавитном порядке
"""
subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

ls = sorted(subject_marks, key=lambda el: (-el[1], el[0].lower()))

for el in ls:
    print(*el)


# 04
"""
Отсортировать список models по цвету в лексикографическом порядке (по алфавиту)
распечатайте элементы этого списка, каждый элемент на новой строке в формате:
Производитель: <make>, модель: <model>, цвет: <color>
Output:
Производитель: Nokia, модель: 216, цвет: Black
Производитель: Honor, модель: 3, цвет: Black
Производитель: Samsung, модель: 7, цвет: Blue
Производитель: Mi Max, модель: 2, цвет: Gold
Производитель: Huawei, модель: 4, цвет: Grey
Производитель: Oppo, модель: 9, цвет: Red
Производитель: Apple, модель: 10, цвет: Silver
"""
models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]

ls = sorted(models, key=lambda el: el['color'])

for el in ls:
    print(f"Производитель: {el['make']}, модель: {el['model']}, цвет: {el['color']}")
    # print(f"Производитель: {ls[el]['make']}, модель: {ls[el]['model']}, цвет: {ls[el]['color']}")
    # print('Производитель: {}, модель: {}, цвет: {}'.format(*item.values()))


# 05
"""
Есть список товаров и их стоимость, Отсортировать его: вверху самые дорогие товары, внизу самые дешевые.
Программа будет принимать строки, в которых сперва указывается название товара, 
а затем через двоеточие с пробелом его цена - целое положительное число.
Строка «конец» означает завершение списка товаров и соответственно окончание ввода
Все товары имеют уникальные названия, цены не дублируются.

Input:  Sony PlayStation 5: 46000
        Телевизор QLED Samsung QE65Q60TAU: 87090
        Смартфон Samsung Galaxy A11: 10000
        Планшет Samsung Galaxy Tab S6: 26600
        конец
Output: Телевизор QLED Samsung QE65Q60TAU
        Sony PlayStation 5
        Планшет Samsung Galaxy Tab S6
        Смартфон Samsung Galaxy A11
"""
# ls = [['Sony PlayStation 5', 46000],
#       ['Телевизор QLED Samsung QE65Q60TAU', 87090],
#       ['Смартфон Samsung Galaxy A11', 10000],
#       ['Планшет Samsung Galaxy Tab S6', 26600]]

ls = list()
while True:
    s = input()
    if s != 'конец':
        ls.append(s.split(':'))
    else:
        break

for el in sorted(ls, key=lambda el: -int(el[1])):
    print(el[0])

# Хорошее решение
for el in sorted([st.split(': ') for st in iter(input, 'конец')], key=lambda x: -int(x[1])):
    print(el[0])


# 06
"""
https://stepik.org/lesson/372111/step/10?unit=359665
Программа принимает на вход в первой строке натуральное число n - количество вручаемых сегодня наград. 
И затем в n следующих строках вводятся имена актеров - победителей.
Нужно вывести в  отдельных строках имена актеров набравших наибольшее и наименьшее количество статуэток 
и через запятую их количество. 
Гарантируется, что всегда будет только один человек, набравший наибольшее и наименьшее количество статуэток.
Input:  6
        Леонардо Ди Каприо
        Джонни Депп
        Леонардо Ди Каприо
        Леонардо Ди Каприо
        Джонни Депп
        Мэтт Деймон
Output: Леонардо Ди Каприо, 3
        Мэтт Деймон, 1
"""
n = int(input())
ls = [input() for _ in range(n)]
# ls = ['Леонардо Ди Каприо', 'Джонни Депп', 'Леонардо Ди Каприо', 'Леонардо Ди Каприо', 'Джонни Депп', 'Мэтт Деймон']

st = set(ls)
# {'Мэтт Деймон', 'Леонардо Ди Каприо', 'Джонни Депп'}

d = {k: v for k, v in zip(st, [ls.count(el) for el in st])}
# {'Джонни Депп': 2, 'Леонардо Ди Каприо': 3, 'Мэтт Деймон': 1}

d_sort = sorted(d, key=lambda x: -d[x])

print(f'{d_sort[0]}, {d.get(d_sort[0])}')
print(f'{d_sort[-1]}, {d.get(d_sort[-1])}')


# Хорошее решение
d = dict()
for _ in range(int(input())):
    el = input()
    d[el] = d.get(el, 0) + 1  # Сразу формируем словарь

el_max, el_min = max(d, key=d.get), min(d, key=d.get)
print(el_max, d[el_max], sep=', ')
print(el_min, d[el_min], sep=', ')


# 07
"""
https://stepik.org/lesson/372111/step/11?unit=359665
Input:  3
        444444 Женя
        79129874521 Женя
        79604845827 Оля
        3
        Оля
        Олег
        Женя
Output: 79604845827
        Неизвестный номер
        444444 79129874521
"""
# tel = {'Женя': ['444444', '79129874521'], 'Оля': ['79604845827']}
# query = ['Оля', 'Олег', 'Женя']

tel = dict()
for _ in range(int(input())):
    phone, name = input().split()
    tel.setdefault(name, []).append(phone)  # Так можно добавить значение к существующему и НОВОМУ ключу
    # tel.get(name).append(name)  # Так можно добавить значение ТОЛЬКО к существующему ключу

query = [input() for _ in range(int(input()))]

for el in query:
    if el in tel.keys():
        print(*tel[el])
    else:
        print('Неизвестный номер')


# 08
"""
https://stepik.org/lesson/372111/step/12?unit=359665
Дни рождения
Имена всех одноклассников Игоря различны.

Input:  4
Саша 20 янв
Артем 15 июн
Карл 10 янв
Коля 20 июл
        3
        июн
        дек
        янв
Output: Артем
        Нет данных
        Карл Саша
"""
birthday = dict()
for _ in range(int(input())):
    name, day, month = input().split()
    birthday.setdefault(name, month)
# birthday = {'Саша': 'янв', 'Артем': 'июн', 'Карл': 'янв', 'Коля': 'июл'}

query = [input() for _ in range(int(input()))]
# query = ['июн', 'дек', 'янв']

for month in query:
    ls = list()
    for name in birthday:
        if month == birthday[name]:
            ls.append(name)
    if ls:
        print(*sorted(ls))
    else:
        print('Нет данных')


# 09
"""
https://stepik.org/lesson/372111/step/13?unit=359665
Рейтинг таксистов
Input:  Джек, 2
        Джек, 3
        Юля, 4
        Билл, 5
        Билл, 4
        Билл, 4
        Билл, 3
        конец
Output: Билл 4.0
        Юля 4.0
        Джек 2.5
"""

lst = [el.split(', ') for el in iter(input, 'конец')]
# lst = [['Джек', '2'], ['Джек', '3'], ['Юля', '4'], ['Билл', '5'], ['Билл', '4'], ['Билл', '4'], ['Билл', '3']]

d = dict()
for el in lst:
    d.setdefault(el[0], []).append(int(el[1]))
# {'Джек': [2, 3], 'Юля': [4], 'Билл': [5, 4, 4, 3]}

rez = [(sum(d[el]) / len(d[el]), el) for el in d]
# [(2.5, 'Джек'), (4.0, 'Юля'), (4.0, 'Билл')]

rez.sort(key=lambda el: (-el[0], el[1]))
# [(4.0, 'Билл'), (4.0, 'Юля'), (2.5, 'Джек')]

for el in rez:
    print(el[1], el[0])
# Билл 4.0
# Юля 4.0
# Джек 2.5


# 10
"""
https://stepik.org/lesson/372111/step/14?unit=359665
Дили Вили Били
Input:  Дили: a
        Дили: a
        Били: a
        Дили: a
        Били: ww
        конец
Output: Количество уникальных комментаторов у Били - 2
        Количество уникальных комментаторов у Дили - 1
        Количество уникальных комментаторов у Вили - 0
"""

ls = [el.split(': ') for el in iter(input, 'конец')]
# [['Дили', 'a'], ['Дили', 'a'], ['Били', 'a'], ['Дили', 'a'], ['Били', 'ww']]

d = {'Били': set(), 'Вили': set(), 'Дили': set()}
for el in ls:
    d.get(el[0]).add(el[1])
# {'Били': {'a', 'ww'}, 'Вили': set(), 'Дили': {'a'}}

rez = [(k, len(v)) for k, v in d.items()]
# [('Били', 2), ('Вили', 0), ('Дили', 1)]
rez = sorted(rez, key=lambda el: -el[1])
# [('Били', 2), ('Дили', 1), ('Вили', 0)]

for el in rez:
    print(f'Количество уникальных комментаторов у {el[0]} - {el[1]}')

