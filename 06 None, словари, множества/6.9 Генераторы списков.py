# 6.9 Вспомним вновь генераторы списков
""""""

a = [
    ("Sidorov", 1995),
    ("Lukov", 2002),
    ("Petrov", 1991),
    ("Gorbachev", 1984),
    ("Kostin", 2000),
    ("Isaev", 2005),
    ("Eliseev", 1999),
    ("Kozlov", 2004),
    ("Bukov", 1995),
    ("Gavrilov", 1980),
    ("Efremov", 2006),
]
name_start_e = [elem[0] for elem in a if elem[0].startswith("E")]
# ['Eliseev', 'Efremov']

more_2000 = [elem[0] for elem in a if elem[1] > 2000]
# ['Lukov', 'Isaev', 'Kozlov', 'Efremov']



a = {
    'Sidorov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
}

keys = [elem for elem in a]
values = [a[elem] for elem in a]

cars = [a[elem]['car'] for elem in a]
# ['Opel', 'BMW', 'Audi', 'BMW', 'Audi', 'Opel']

cars_lt_2000 = [a[elem]['car'] for elem in a if a[elem]['age'] < 2000]
# ['BMW', 'Audi']

name_with_car = [(elem, a[elem]['car']) for elem in a if a[elem]['age'] < 2000]
# [('Petrov', 'BMW'), ('Eliseev', 'Audi')]

larger_2000_and_soccer = [(elem, a[elem]['car']) for elem in a if
                          a[elem]['age'] > 2000 and a[elem]['hobby'] == 'soccer']
# [('Kozlov', 'Opel')]


s = 'gfdogjdf45i398gry74y543hgkgreiu'

int_digits = [int(i) for i in s if i.isdigit()]
# [4, 5, 3, 9, 8, 7, 4, 5, 4, 3]

letters = [i for i in s if i.isalpha()]
# ['g', 'f', 'd', 'o', 'g', 'j', 'd', 'f', 'i', 'g', 'r', 'y', 'y', 'h', 'g', 'k', 'g', 'r', 'e', 'i', 'u']


from random import randint
n = 5
m = 3
a = [[randint(1,6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)
"""
[4, 4, 1]
[2, 2, 2]
[2, 4, 5]
[5, 5, 1]
[5, 6, 3]
"""


"""
Сделаем квадратную таблицу и в список b будем вносить лишь элементы главной диагонали, 
а в список c только элементы со строки с индексом 2, 
а в список d только элементы столбца с индексом 3.
"""
# Формируем матрицу случайными элементами
from random import randint
n = 5
m = 5
a = [[randint(1,6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)
"""
[3, 1, 1, 6, 5]
[5, 3, 2, 5, 3]
[4, 3, 3, 4, 4]
[6, 6, 6, 1, 4]
[5, 5, 5, 5, 6]
"""
# элементы главной диагонали
b = [a[i][j] for i in range(n) for j in range(m) if i == j]
# [3, 3, 3, 1, 6]

# элементы со строки с индексом 2
с = [a[2][j] for j in range(m)]
# [4, 3, 3, 4, 4]

# элементы столбца с индексом 3
d =[a[i][3] for i in range(n)]
# [6, 5, 4, 1, 5]


# составить таблицу умножения
n = 5
m = 5
a = [[i * j for j in range(1, m + 1)] for i in range(1, n + 1)]
for i in a:
    print(i)
"""
[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
[3, 6, 9, 12, 15]
[4, 8, 12, 16, 20]
[5, 10, 15, 20, 25
"""


"""
Обойти элементы матрицы внутри генератора списка по значениям, 
для этого достаточно во внутреннем цикле обращаться к итерируемой переменной внешнего цикла
"""
# Формируем матрицу случайными элементами
from random import randint
n = 3
m = 4
matrix = [[randint(1, 10) for j in range(m)] for i in range(n)]
for current_row in matrix:
    print(current_row)

squares = [num ** 2 for row in matrix for num in row]
# [49, 100, 36, 81, 36, 16, 81, 1, 36, 64, 49, 9]


#
#  *  *  *   Задачи   *  *  *
#


"""
https://stepik.org/lesson/372102/step/2?unit=359656
Декартово произведение
Декартово произведение это когда вы каждый элемент из одного множества группируете с каждым элементом другого множества. 
Например, если бы у вас имелись такие списки^
colors = ['red', 'green']
sizes = ['S', 'M', 'L']
то их декартово произведение:
[('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L')]

создать список кортежей на основании переменных colors и sizes
Input:  *
Output: *
"""
colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']

res = [(c, s) for c in colors for s in sizes]
print(res)

# Вариант
import itertools
res = list(itertools.product(colors, sizes))
print(res)


"""
есть двумерный список vector. При помощи генератора-списка сделать на основании vector линейный(одномерный) 
Input:  *
Output: *
"""
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

res = [vector[row][col] for row in range(len(vector)) for col in range(len(vector[0]))]

# тоже самое
res = []
for row in range(len(vector)):
    for col in range(len(vector[0])):
        res += [vector[row][col]]


res = []
for row in vector:
    for el in row:
        res.append(el)

print(res)
