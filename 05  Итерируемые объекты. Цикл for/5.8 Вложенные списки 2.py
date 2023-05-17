#  5.8 Вложенные списки 2
""""""

#  *  *  *   Задачи   *  *  *


"""
Дана матрица размером NxN, требуется найти максимальное значение среди элементов, 
расположенных на побочной диагонали.
Под побочной диагональю матрицы подразумевается диагональ, 
проведённая из правого верхнего угла до левого нижнего угла.
Input:  2
        1 2
        3 4
Output: 3
"""
# n = 2
# matrix = [[1, 2], [3, 4]]  # 3
# n = 3
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 7
# n = 5
# matrix = [[100, 2, 3, 90, 100], [1, 54, 3, 90, 100], [1, 2, 5, 90, 100], [1, 2, 3, 2, 100], [1, 2, 3, 90, 100]]  # 100

n = int(input())
matrix = [[int(el) for el in input().split()] for row in range(n)]

matrix.reverse()  # Список в обратном порядке (переворот матрицы по горизонтали)
n_max = matrix[0][0]

for row in range(1, n):  # Первая строка уже обработана
    for col in range(n):
        if row == col:
            if matrix[row][col] > n_max:
                n_max = matrix[row][col]
print(n_max)

# Без переворота матрицы
n = int(input())
matrix = [[int(el) for el in input().split()] for row in range(n)]
n_max = matrix[0][-1]

for row in range(1, n):
    for col in range(n):
        if row + col == n - 1:
            if matrix[row][col] > n_max:
                n_max = matrix[row][col]
print(n_max)

"""
Сформировать квадратную матрицу размером NxN, в которой используется следующее заполнение:
все элементы, находящиеся выше главной диагонали, заполняются значением A;
все элементы, находящиеся ниже главной диагонали, заполняются значением B;
все элементы, находящиеся на главной диагонали, заполняются значением C.
В качестве ответа, выведите на экран полученную матрицу
Input:  3
        1 0 3
Output: 3 1 1
        0 3 1
        0 0 3
"""
# n = 3
# a, b, c = 1, 0, 3

n = int(input())
a, b, c = map(int, input().split())

matrix = []
for row in range(n):
    matrix.append([0] * n)

for row in range(n):
    for col in range(n):
        if row > col:
            matrix[row][col] = b
        elif row == col:
            matrix[row][col] = c
        else:
            matrix[row][col] = a

for el in matrix:
    print(*el)

# Идеальное решение
n = int(input())
a, b, c = map(int, input().split())
matrix = [[a if row < col else (b, c)[row == col] for col in range(n)] for row in range(n)]
[print(*el) for el in matrix]

"""
A. Матчи
https://stepik.org/lesson/332555/step/3?unit=315943
https://www.youtube.com/watch?v=Q6A2LWKll9M
https://codeforces.com/problemset/problem/268/A
Input:  3
        1 2
        2 4
        3 4
Output: 1
"""
# n = 3
# matrix = [[1, 2], [2, 4], [3, 4]]  # 1
# n = 4
# matrix = [[100, 42], [42, 100], [5, 42], [100, 5]]  # 5
# n = 2
# matrix = [[1, 2], [1, 2]]  # 0

n = int(input())
matrix = [[int(el) for el in input().split()] for row in range(n)]

cnt = 0
for el in range(n):
    for row in range(n):
        if matrix[el][0] == matrix[row][1]:
            cnt += 1

print(cnt)

# Короче
matrix = [input().split() for el in range(int(input()))]
res = [1 for el in matrix for row in matrix if el[0] == row[1]]
print(sum(res))

"""
Морской бой - 2
https://stepik.org/lesson/332555/step/4?unit=315943
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=750
http://egoroffartem.pythonanywhere.com/course/decision/BA9zmfQyfdo
Input:  4 4
        ****
        **..
        *...
        *...
Output: 4
"""
# Добавляем бордюр из "."
# w, h = 4, 4
# matrix = ['......', '.****.', '.**...', '.*....', '.*....', '......']  # 4
# w, h = 4, 3
# matrix = ['.....', '.***.', '.....', '.....', '.....']  # 0
# w, h = 2, 3
# matrix = ['.....', '.....', '.....', '.....']  # 6
# w, h = 3, 5
# matrix = ['.......', '.***...', '...**..', '....**.', '.......']


w, h = map(int, input().split())
matrix = ['.' * (h + 2)]  # При создании списка сразу добавляем "бордюрные точки"
for el in range(w):
    row = '.' + input() + '.'
    matrix.append(row)
matrix.append('.' * (h + 2))

cnt = 0

for row in range(1, w + 1):
    for col in range(1, h + 1):
        if matrix[row][col] == '.':
            if matrix[row - 1][col] == '.' and matrix[row][col + 1] == '.' and \
                    matrix[row + 1][col] == '.' and matrix[row][col - 1] == '.':
                cnt += 1

print(cnt)

# Короче
w, h = map(int, input().split())
cnt = 0
matrix = ['.' * (h + 2)] + ['.' + input() + '.' for _ in range(w)] + ['.' * (h + 2)]
for row in range(1, w + 1):
    for col in range(1, h + 1):
        if matrix[row][col] == '.':
            cnt += matrix[row][col+1] == matrix[row][col-1] == matrix[row+1][col] == matrix[row-1][col] == '.'
print(cnt)


"""
Дана прямоугольная матрица размером NxM, в которой заполнены значения только в первом столбце и в первом ряду. 
Все остальные элементы равны нулю и мы считаем их незаполненными.
Требуется заполнить каждый пустой элемент путем сложения соседа слева и соседа сверху. 
Начинать нужно с тех элементов, у которых оба указанных соседа заполнены (не равны нулю)
Input:  3 6
        5 3 1 4 4 4
        3 0 0 0 0 0
        1 0 0 0 0 0
Output: 5 3 1 4 4 4
        3 6 7 11 15 19
        1 7 14 25 40 59
"""
# h, w = 3, 6
# matrix = [[5, 3, 1, 4, 4, 4], [3, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]

h, w = map(int, input().split())
matrix = [[el for el in map(int, input().split())] for _ in range(h)]
for row in range(1, h):
    for col in range(1, w):
        matrix[row][col] = matrix[row][col - 1] + matrix[row - 1][col]

for el in matrix:
    print(*el)


"""
Перевернутая матрица
Дана прямоугольная матрица размером NxM, в которой заполнены значения только  в последнем столбце и в последнем ряду. 
Все остальные элементы равны нулю и мы считаем их незаполненными.
Требуется заполнить каждый пустой элемент путем сложения соседа справа и соседа снизу.
Начинать нужно с тех элементов, у которых оба указанных соседа заполнены (не равны нулю)
Input:  3 5
        0 0 0 0 4
        0 0 0 0 2
        4 4 2 5 4
Output: 50 33 20 11 4
        17 13 9 7 2
        4 4 2 5 4
"""
# h, w = 3, 5
# matrix = [[0, 0, 0, 0, 4], [0, 0, 0, 0, 2], [4, 4, 2, 5, 4]]

h, w = map(int, input().split())
matrix = [[el for el in map(int, input().split())] for _ in range(h)]
for row in range(h - 2, -1,  -1):
    for col in range(w - 2, -1,  -1):
        matrix[row][col] = matrix[row][col + 1] + matrix[row + 1][col]

for el in matrix:
    print(*el)


"""
Заполнение змейкой
Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой.
Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.
Input:  4 10
Output: 0  1  2  3  4  5  6  7  8  9
        19 18 17 16 15 14 13 12 11 10
        20 21 22 23 24 25 26 27 28 29
        39 38 37 36 35 34 33 32 31 30
"""
row, col = map(int, input().split())

matrix = [[i + col * el if el % 2 == 0 else abs(i - col * el) + col - 1 for i in range(col)] for el in range(row)]

for el in matrix:
    print(*el)


# Проще
row, col = map(int, input().split())

for el in range(row):
    if el % 2 == 0:
        print(*list(range(el * col, el * col + col)))
    else:
        print(*list(range(el * col, el * col + col))[::-1])


"""
A. Фотографии Брейна
Фотография представляет собой матрицу размера n×m, в каждой ячейке которой хранится символ, 
обозначающий цвет соответствующего пикселя. Всего существует 6 цветов:
'C' (cyan) — голубой
'M' (magenta) — пурпурный
'Y' (yellow) — желтый
'W' (white) — белый
'G' (grey) — серый
'B' (black) — черный
Фотографию можно считать черно-белой, если в ней есть только белый, серый или черный цвет. 
Если же присутствует хоть один пиксель голубого, пурпурного или желтого цвета, она цветная.
Input:  2 2
        C M
        Y Y
Output: #Color

Input:  3 2
        W W
        W W
        B B
Output: #Black&White
"""
h, w = 2, 2
matrix = [['C', 'M'], ['Y', 'Y']]
# h, w = 3, 2
# matrix = [['W', 'W'], ['W', 'W'], ['B', 'B']]
# h, w = 3, 2
# matrix = [['W', 'W'], ['W', 'W'], ['B', 'B']]

# h, w = map(int, input().split())
# matrix = [[el for el in map(str, input().split())] for _ in range(h)]

color = ['C', 'M', 'Y']
flag = True

for row in range(h):
    if flag:
        for col in range(w):
            if matrix[row][col] in color:
                flag = False
                break

print('#Black&White' if flag else '#Color')

# Вариант
h, w = map(int, input().split())
matrix = [input().split() for _ in range(h)]
flag = '#Black&White'
for row in range(h):
    for col in range(w):
        if matrix[row][col] not in 'BWG':
            flag = '#Color'
            break
print(flag)


"""
Спираль
https://acmp.ru/index.asp?main=task&id_task=196
http://egoroffartem.pythonanywhere.com/course/decision/mHTMe_Q4-Xo
Программа получает на вход одно число n.
Программа должна вывести матрицу, заполненную числами от 1 до N2 по спирали, 
при этом между числами может быть любое количество пробелов. 
Не допускается:
начинать спираль в ином, кроме верхнего левого, углу, 
закручивать спираль против часовой стрелки или изнутри наружу.
Input:  3
Output: 1 2 3
        8 9 4
        7 6 5
"""


n = int(input())
matrix = [[0] * n for _ in range(n)]

el = 1  # Счетчик (значение) для обхода всех ячеек матрицы
row = 0  # Стартовая координата ряда
col = -1  # Стартовая координата колонки
d_row = 0  # Статус движения по рядам (верхний, тот же, нижний ряд). Значения -1, 0, 1
d_col = 1  # Статус движения по колонкам (левая, та же, правая колонка). Значения -1, 0, 1

while el <= n ** 2:
    # Если следующая клетка справа (в текущем ряду) существует и она пуста (равна нулю)
    if 0 <= row + d_row < n and 0 <= col + d_col < n and matrix[row + d_row][col + d_col] == 0:
        # то устанавливаем новую координату нашего положения в матрице
        row += d_row
        col += d_col
        matrix[row][col] = el
        el += 1
    else:  # Устанавливаем новое направление обхода
        if d_col == 1:
            d_col = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_col = -1
        elif d_col == -1:
            d_col = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_col = 1


for el in matrix:
    print(*el)


# Вариант
n = int(input())  # ввод размера матрицы
lst = [[0] * n for i in range(n)] # создание нулевой матрицы
i = 0  # i - строка (равен нулю потому, что цикл начинает свой обход с верхней строки)
j = 0  # j - столбец (равен нулю потому, что цикл начинает свой обход с левого столбца)
di = 0  # di - смещениe строки (равен нулю потому, что  обход начинается слева направо в  одной строке)
dj = 1  # dj - смещениe столбца (равен единице потому, что обход начинается  в пределах одной строки слева направо)

for k in range(n**2):  # цикл обходит все ЗНАЧЕНИЯ матрицы-вывода
    lst[i][j] = k + 1  # присваивание значения в выбранную ячейку
    if lst[(i + di) % n][(j + dj) % n]:
        """
        Если следующая ячейка равна положительному числу, то выполняется код ниже.
        Деление индекса по остатку на длину матрицы нужно во избежание IndexError,
        когда текущая ячейка явлется последней в своей последовательности(т.е. следующей не существует).
        Тогда этой ячейкой будет являться ранее заполненная(первой ячейкой текущей ряда или столбца).
        """
        di, dj = dj, -di
        """
        происходит изменение вектора движение "курсора" по ЧАСОВОЙ стрелке,
        в этом можно убедиться на примере:
        di = 0 => di = 1 => di = 0  => di = -1 => di = 0    пара вернулась
        dj = 1 => dj = 0 => dj = -1 => dj = 0  => dj = 1    к начальным значениям
        вправо => вниз   => влево   => вверх   => вправо    это вектор движения
        """
    i = i + di  # строка следующей ячейки
    j = j + dj  # столбец следующей ячейки

for el in lst:
    print(*el)


"""
A. Тортминатор
https://stepik.org/lesson/332555/step/12?unit=315943
https://youtu.be/kZcRNjw2UHM
http://codeforces.com/problemset/problem/330/A
Input:  3 4
        S...
        ....
        ..S.
Output: 8
"""
# r, c = 3, 4
# m_in = ['S...', '....', '..S.']  # 8
# r, c = 7, 3
# m_in = ['S..', 'S..', 'S..', 'S..', 'S..', 'S..', 'S..']  # 14
# r, c = 10, 10
# m_in = ['.....SSSSS', '.....SSSSS', '.....SSSSS', '.....SSSSS', '.....SSSSS',
#         '..........', '..........', '..........', '..........', '..........']  # 75
# r, c = 8, 9
# m_in = ['.........', '.........', '.........', '.........', '.........', '.........', 'SSSSSSSSS', '.........']  # 63
# r, c = 3, 4
# m_in = ['....', '....', '....']  # 12
# r, c = 3, 4
# m_in = ['SSSS', 'SSSS', 'SSSS']  # 0


r, c = map(int, input().split())
m_in = [input() for _ in range(r)]
m_out = [[0] * c for _ in range(r)]  # интерполяция в цифры матрицы m_in
res = 0

for row in range(r):  # проверяем строки
    if 'S' not in m_in[row]:
        for col in range(c):
            m_out[row][col] = 1

for col in range(c):  # проверяем столбцы
    flag = True
    for row in range(r):
        if 'S' in m_in[row][col]:
            flag = False
            break
    if flag:
        for row in range(r):
            m_out[row][col] = 1

for el in m_out:
    res += sum(el)

print(res)



r, c  = map(int, input().split())
tort = [list(input()) for _ in range(n)]  # создаём матрицу торта


row = sum(not 'S' in row for row in tort)  # подсчитываем кол-во свободных строк (длина c)  # 1
col = sum(not 'S' in col for col in zip(*tort))  # подсчитываем кол-во свободных столбцов (длина r)  # 2
# результат = сумма всех ячеек в свободных строках и столбцах, за вычетом пересечения строк и столбцов # 4 + 6 - 2
print(row * c + col * r - row * col)

""" На заметку """
# zip(*tort) производит транспонирование матрицы и выводит столбцы в виде кортежа:
# т.е. последовательно берет одинакового порядка элементы из элементов списка.
# (tort[0][0], tort[1][0],tort[2][0]), (tort[0][1], tort[1][1],tort[2][1]), и т.д.
# Но так происходит только с совместным применением оператора распаковки "*"
for el in zip(*tort):
    print(el)
# ('S', '.', '.')
# ('.', '.', '.')
# ('.', '.', 'S')
# ('.', '.', '.')

# Без применения оператора распаковки "*" выводятся кортежи строк
for el in zip(tort):
    print(el)
# (['S', '.', '.', '.'],)
# (['.', '.', '.', '.'],)
# (['.', '.', 'S', '.'],)

