#  5.7 Вложенные списки
""""""

# Вложенный список – это список, элементами которого являются также списки. Например:
a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
print(len(a))  # 3
print(a[2])  # [3, 10, 17, 19]
print(a[2][1])  # 10

#  список из строк тоже можно считать вложенной структурой
b = ["hello", "hi", "world"]
print(b[2])  # world
print(b[2][0])  # w

#  Чтобы разглядеть в нашем списке a таблицу сделаем несколько переносов
a = [
  [0, 2, 4, 6],
  [1, 5, 9, 13],
  [3, 10, 17, 19]
]
"""
Здесь, как и в обычных списках, существует 2 варианта обхода:
- обход по значению
- обход по индексу
"""

#  Обход по значению
for row in a:
    for k in row:
        print(k, end=" ")
    print()
# 0 2 4 6
# 1 5 9 13
# 3 10 17 19

for row in range(3):
    for col in range(4):
        print(a[row][col], end=" ")
    print()
# 0 2 4 6
# 1 5 9 13
# 3 10 17 19

# Изменение значений
for row in range(3):
    for col in range(4):
        a[row][col] += 10
        print(a[row][col], end=" ")
    print()
print(a)
# 10 12 14 16
# 11 15 19 23
# 13 20 27 29
# [[10, 12, 14, 16], [11, 15, 19, 23], [13, 20, 27, 29]]


"""
Варианты отображения
"""
a = [
  [0, 2, 4, 6],
  [1, 5, 9, 13],
  [3, 10, 17, 19]
]

#  Вывод по столбцам
for col in range(4):
    for row in range(3):
        print(a[row][col], end=" ")
    print()
# 0 1 3
# 2 5 10
# 4 9 17
# 6 13 19

#  Можно так же обходить элементы справа-налево, начиная снизу и двигаясь вверх
for row in range(2, -1, -1):
    for col in range(3, -1, -1):
        print(a[row][col], end=" ")
    print()
# 19 17 10 3
# 13 9 5 1
# 6 4 2 0

"""
Нахождение суммы строк или столбцов матрицы
"""
a = [
  [0, 2, 4, 6], 
  [1, 5, 9, 13], 
  [3, 10, 17, 19]
]
for row in range(3):
    sum = 0
    for col in range(4):
        sum += a[row][col]
    print(sum)
# 12
# 28
# 49

#  Для нахождения суммы по столбцам, необходимо поменять эти два цикла местами.
for col in range(4):
    sum = 0
    for row in range(3):
        sum += a[row][col]
    print(sum)
# 4
# 17
# 30
# 38


""" Заполнение вложенного списка """
a = []
row = 3
col = 4
for row in range(row):
    a.append([0] * col)
for row in a:
    print(row)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]


""" Квадратная матрица """
#  квадратные таблицы, с размерностью n на n
"""
В таких таблицах имеется главная диагональ, 
которая идёт из элемента [0][0] по пути [1][1], [2][2] и так до элемента [n][n]. 
Следовательно, у элементов главной диагонали номер строки совпадает с номером столбца, т.е. [row] = [col]

Эта диагональ делит матрицу на 2 треугольника. 
Первый треугольник состоит из элементов, расположенных выше главной диагонали: 
с элементами по индексу [0][1], [0][2], [1][2]. 
Второй треугольник с элементами по индексу [1][0], [2][0], [2][1].
В этих треугольниках наблюдается одна особенность:
У верхнего треугольника row < col, т.е. номер строки меньше номера столбца, 
а у нижнего треугольника row > col, т.е. номер строки больше номера столбца.
"""

a = []
n = 5  # Размер квадратной матрицы
for row in range(n):
    a.append([0] * n)

for row in range(n):
    for col in range(n):
        if row == col:
            a[row][col] = 10
        elif row > col:
            a[row][col] = 0
        else:
            a[row][col] = 1
for row in a:
    print(row)
# [10, 1, 1, 1]
# [0, 10, 1, 1]
# [0, 0, 10, 1]
# [0, 0, 0, 10]


""" считывание данных в матрицу """
matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)
# 1 2 3
# 4 5 6
# 7 8 9
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


#  *  *  *   Задачи   *  *  *


"""
Посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.
Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, 
а затем в N строках записаны элементы списка.
Input:  2
        1 2
        3 4
Output: 5
"""
n = int(input())
matrix = []
res = 0

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
# print(matrix)  # отобразить матрицу

for row in range(n):
    for col in range(n):
        if col == row:
            res += matrix[col][row]
print(res)

# Улыбнуло )))
n = int(input())
s = 0
for i in range(n):
    s += int(input().split()[i])
print(s)

"""
Обход элементов матрицы - 1
Задана целочисленная квадратная матрица размером N x N. 
Необходимо обойти элементы этой матрицы сверху вниз слева направо 
и вывести элементы именно в таком порядке в виде таблицы. 
Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. 
В каждой из последующих N строк записаны N целых чисел – элементы матрицы. 
Все числа во входных данных не превышают 100 по абсолютной величине.
Input:  5

        3 4 9 1 2
        8 2 0 5 1
        4 7 4 8 7
        7 1 3 3 8
        5 6 3 7 0

Output: 3 8 4 7 5
        4 2 7 1 6
        9 0 4 3 3
        1 5 8 3 7
        2 1 7 8 0
"""
n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
# print(matrix)  # отобразить матрицу

for row in range(n):
    for col in range(n):
        print(matrix[col][row], end=' ')
    print()


# Вариант с сохранением транспонированной матрицы:
n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

res = [[0 for row in range(n)] for col in range(n)]

for row in range(n):
    for col in range(n):
        res[row][col] = matrix[col][row]
        print(res[row][col], end=' ')
    print()

"""
Обход элементов матрицы - 2
Задана целочисленная квадратная матрица размером N x N. 
Необходимо обойти элементы этой матрицы снизу вверх справа налево 
и вывести элементы именно в таком порядке в виде таблицы. 
Input:  3
        5 4 1
        6 7 9
        9 3 0

Output: 0 9 1
        3 7 4
        9 6 5
"""
# n = 3
# matrix = [[5, 4, 1], [6, 7, 9], [9, 3, 0]]

n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for col in range(n - 1, -1, -1):  # col = 2, 1, 0  (при n = 3)
    for row in range(n - 1, -1, -1):  # row = 2, 1, 0  (при n = 3)
        print(matrix[row][col], end=" ")
    print()


"""
Обход элементов матрицы - 3
Задана целочисленная матрица, состоящая из N строк и M столбцов. 
Необходимо обойти элементы этой матрицы cправа налево сверху вниз 
и вывести элементы именно в таком порядке в виде таблицы.
Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы. 
Input:  3 4
        5 9 2 6
        6 2 4 3
        1 2 8 7

Output: 6 2 9 5
        3 4 2 6
        7 8 2 1
"""
# n, m = 3, 4
# matrix = [[5, 9, 2, 6],
#           [6, 2, 4, 3],
#           [1, 2, 8, 7]]

n, m = map(int, input().split())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in range(n):
    for col in range(m - 1, -1, -1):
        print(matrix[row][col], end=" ")
    print()


"""
Обход элементов матрицы - 4
Задана целочисленная матрица, состоящая из N строк и M столбцов. 
Необходимо обойти элементы этой матрицы слева направо снизу вверх 
и вывести элементы именно в таком порядке в виде таблицы. 
Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы.

Input:  3 4
        5 9 2 6
        6 2 4 3
        1 2 8 7

Output: 1 2 8 7
        6 2 4 3
        5 9 2 6
"""
# n, m = 3, 4
# matrix = [[5, 9, 2, 6],
#           [6, 2, 4, 3],
#           [1, 2, 8, 7]]

n, m = map(int, input().split())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in range(n - 1, -1, -1):
    for col in range(m):
        print(matrix[row][col], end=" ")
    print()


"""
Дана матрица размера 5х5, состоящая из 24-x нулей и единственной единицы. 
Строки матрицы пронумеруем числами от 1 до 5 сверху вниз, 
столбцы матрицы пронумеруем числами от 1 до 5 слева направо. 
За один ход разрешается применить к матрице одно из двух следующих преобразований:

Поменять местами две соседние строки матрицы, то есть строки с номерами i и i+1 для некоторого целого i (1 ≤ i < 5).
Поменять местами два соседних столбца матрицы, то есть столбцы с номерами j и j+1 для некоторого целого j (1 ≤ j < 5).
Вы считаете, что матрица будет выглядеть красиво, 
если единственная единица этой матрицы будет находиться в ее центре 
(в клетке, которая находится на пересечении третьей строки и третьего столбца). 
Посчитайте, какое минимальное количество ходов потребуется, чтобы сделать матрицу красивой.

Input:  0 0 1 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0

Output: 2
"""
matrix = []
flag = True

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in range(5):
    if flag:
        for col in range(5):
            if matrix[row][col] == 1:
                print(abs(2 - row) + abs(2 - col))
                flag = False
                break


"""
Задан целочисленный двумерный массив, состоящий из N строк и M столбцов. 
Требуется вычислить сумму элементов в каждой строке и в каждом столбце.
Программа получает на вход два натуральных числа N и M – количество строк и столбцов двумерного массива. 
В каждой из последующих N строк записаны M целых чисел – элементы массива. 
Все числа во входных данных не превышают 1000 по абсолютной величине.

В первой строке вам необходимо вывести N чисел – суммы элементов массива для каждой строки в отдельности.
Во второй строке в аналогичном формате выведите M чисел – суммы элементов для каждого столбца.

Input:  3 4
        5 9 2 6
        6 2 4 3
        1 2 8 7

Output: 22 15 18
        12 13 14 16
"""
# n, m = 3, 4
# matrix = [[5, 9, 2, 6],
#           [6, 2, 4, 3],
#           [1, 2, 8, 7]]

n, m = map(int, input().split())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in range(n):
    sum_row = 0
    for col in range(m):
        sum_row += matrix[row][col]
    print(sum_row, end=' ')

print()

for row in range(m):
    sum_col = 0
    for col in range(n):
        sum_col += matrix[col][row]
    print(sum_col, end=' ')


# Коротко
n, m = map(int, input().split())
matrix = []

matrix = [[int(el) for el in input().split()] for row in range(n)]

print(*[sum(row) for row in matrix])
print(*[sum(row[col] for row in matrix) for col in range(m)])


"""
Проверьте, является ли двумерный массив симметричным относительно главной диагонали. 
Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.
Программа получает на вход число n < 100, являющееся числом строк и столбцов в массиве. 
Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.
Программа должна выводить слово Yes для симметричного массива и слово No для несимметричного.
Input:  3
        0 1 2
        1 5 3
        2 3 4
Output: Yes
"""
n = int(input())
matrix = [[int(el) for el in input().split()] for row in range(n)]

# n = 3
# matrix = [[0, 9, 2],
#           [1, 5, 3],
#           [2, 3, 4]]

flag = True
for row in range(n):
    if flag:
        for col in range(n):
            if matrix[row][col] == matrix[col][row]:
                continue
            else:
                flag = False
            break  # Остановка внутреннего цикла

print('Yes' if flag else 'No')


"""
Состязания.
Входящие данные:
Первая строка: кол-во строк и столбцов. Остальные строки - наполнение матрицы.
Вывести:
- Максимальную сумму всех элементов в строке.
- Номер строки с наибольшей суммой элементов (Если таких строк несколько, то выводится номер наименьшей из них).
Input:  3 4
        1 2 3 4
        9 10 11 12
        5 6 7 8
Output: 42
        1
"""
# n, m = 3, 4
# matrix = [[1, 2, 3, 4], [9, 10, 11, 12], [5, 6, 7, 8]]

n, m = map(int, input().split())
matrix = [[int(el) for el in input().split()] for row in range(n)]

rez = [sum(row) for row in matrix]
print(max(rez))
print(rez.index(max(rez)))




"""
Состязания - 2
- Найти максимальное значение элемента  матрице.
- Номер строки и индекс этого элемента (Если таких элементов несколько, то выводится номер и индекс наименьшей из них)
Input:  2 4
        7 5 9 9
        9 2 1 9
Output: 9
        0 2
"""
# n, m = 2, 4
# matrix = [[7, 5, 9, 9], [9, 2, 1, 9]]


n, m = map(int, input().split())
matrix = [[int(el) for el in input().split()] for row in range(n)]

rez = [max(row) for row in matrix]  # Список максимальных значений
max_el = max(rez)
print(max_el)

flag = True
for row in range(n):  # Находим первое нахождение max_el и останавливаемся
    if flag:
        for col in range(m):
            if matrix[row][col] == max_el:
                print(row, col)
                flag = False
                break

# От автора (проверяем каждый элемент матрицы)
n, m = map(int, input().split())
matrix = [[int(el) for el in input().split()] for row in range(n)]

max_el, row_el, col_el = 0, 0, 0

for row in range(n):
    for col in range(m):
        if matrix[row][col] > max_el:
            max_el, row_el, col_el = matrix[row][col], row, col

print(max_el)
print(row_el, col_el)




"""
Состязания - 3
Найти строку, у которой максимален элемент. 
Если такой элемент есть в других строках, то из них выбираем строку, у которой наибольшая сумма ее элементов. 
Если и таких строк несколько, то выбираем из них строку с минимальным номером.
Вывести номер этой строки.
Input:  2 3
        7 5 7
        7 7 5
Output: 0


Input:  4 4
        9 9 9 9
        8 8 8 8
        1 1 10 1
        7 7 7 7
Output: 2
"""
# n, m = 2, 3
# # matrix = [[7, 5, 7], [7, 7, 5]]

# n, m = 4, 4
# matrix = [[9, 9, 9, 9], [8, 8, 8, 8], [1, 1, 10, 1], [7, 7, 7, 7]]

n, m = map(int, input().split())
matrix = [[int(el) for el in input().split()] for row in range(n)]

max_el, max_sum, rez = 0, 0, []

# Формируем матрицу (из 2-х значений в строке)
# с постепенным поиском большего элемента, и суммой элементов в строках matrix
for row in range(n):
    cnt = 0
    flag = False
    for col in range(m):
        cnt += matrix[row][col]
        if matrix[row][col] >= max_el:
            max_el = matrix[row][col]
            flag = True
    if flag:
        max_sum = cnt
        rez.append([max_el, max_sum])
    else:
        rez.append([0, 0])  # если элемент не больший, то заполняем нулями
        # [[9, 36], [0, 0], [10, 13], [0, 0]]

# поиск номера строки matrix согласно условиям задачи
max_num, total, winner = 0, 0, 0
for row in range(n):
    if rez[row][0] >= max_num and rez[row][1] > total:
        max_num, total, winner = rez[row][0], rez[row][1], row
    elif rez[row][0] > max_num:
        max_num, total, winner = rez[row][0], rez[row][1], row

print(winner)

# Хорошее решение
n, m = map(int, input().split())
matrix = [[int(el) for el in input().split()] for row in range(n)]

max_el = 0
res = []

# Находим наибольший элемент в матрице 'matrix'
for row in range(n):
    for col in range(m):
        if matrix[row][col] > max_el:
            max_el = matrix[row][col]

# Формируем список по условию: если в строке matrix есть наибольший элемент,
# о записываем сумму элементов этой строки, иначе пишем ноль.
for i in range(n):
    if max_el in matrix[i]:
        res.append(sum(matrix[i]))
    else:
        res.append(0)

print(res.index(max(res)))


"""
Состязания - 4
Найти количество строк, в которых есть элемент с максимальным значением. 
Input:  3 3
        3 1 2
        1 3 4
        4 3 3
Output: 2
"""
# n, m = 3, 3
# matrix = [[3, 1, 2], [1, 3, 4], [4, 3, 3]]
# n, m = 4, 3
# matrix = [[7, 8, 9], [9, 3, 10], [4, 3, 8], [5, 6, 7]]
# n, m = 5, 5
# matrix = [[1, 5, 2, 3, 5], [1, 3, 2, 3, 5], [4, 1, 4, 2, 4], [5, 5, 2, 1, 5], [5, 5, 1, 2, 5]]

n, m = map(int, input().split())
matrix = [[int(el) for el in input().split()] for row in range(n)]

max_el, cnt = 0, 0

# Находим наибольший элемент в матрице 'matrix'
for row in range(n):
    for col in range(m):
        if matrix[row][col] > max_el:
            max_el = matrix[row][col]

for i in range(n):
    if max_el in matrix[i]:
        cnt += 1

print(cnt)


"""
Симпатичный узор
https://stepik.org/lesson/296964/step/14?thread=solutions&unit=278692
https://acmp.ru/asp/do/index.asp?main=topic&id_course=1&id_section=8&id_topic=121
"""
# matrix = [['B', 'W', 'B', 'W'], ['B', 'B', 'W', 'B'], ['W', 'W', 'B', 'B'], ['B', 'W', 'W', 'W']]  # Yes
# matrix = [['B', 'B', 'W', 'B'], ['B', 'B', 'W', 'B'], ['W', 'W', 'B', 'W'], ['B', 'B', 'W', 'B']]  # No

matrix = [[el for el in input()] for row in range(4)]

flag = True
for row in range(3):
    if flag:
        for col in range(3):
            if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
                flag = False
print('Yes' if flag else 'No')


"""
Миша и негатив
https://stepik.org/lesson/296964/step/15?unit=278692
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=749
"""

# n, m = 3, 4
# positive = [['W', 'B', 'B', 'W'], ['B', 'B', 'B', 'B'], ['W', 'B', 'B', 'W']]
# negative = [['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']]  # 2

# n, m = 2, 2
# positive = [['B', 'W'], ['B', 'B']]
# negative = [['W', 'W'], ['B', 'W']]  # 2

n, m = map(int, input().split())
positive = [[el for el in input()] for row in range(n)]
zero = input()  # Принимаем пустую строку
negative = [[el for el in input()] for row in range(n)]


cnt = 0

for row in range(n):
    for col in range(m):
        if positive[row][col] == negative[row][col]:
            cnt += 1

print(cnt)



"""
A. Таблица умножения
https://stepik.org/lesson/296964/step/16?unit=278692
https://codeforces.com/problemset/problem/577/A
"""
n, num = map(int, input().split())
cnt = 0
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row * col == num:
            cnt += 1

print(cnt)

# Решение через нахождение общих делителей
# https://youtu.be/KGtPIAaE9sg
n, num = map(int, input().split())
cnt = 0
nod = 1

while nod ** 2 <= num:
    if num % nod == 0 and nod <= n and num // nod <= n:
        if nod != num // nod:
            cnt += 2
        else:
            cnt += 1
    nod += 1

print(cnt)
