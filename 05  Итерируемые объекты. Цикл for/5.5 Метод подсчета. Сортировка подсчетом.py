# 5.5 Метод подсчета. Сортировка подсчетом
""""""


#  *  *  *   Задачa 1   *  *  *
"""
Есть список из чисел от 0 до 5, в котором числа могут повторяться.
Подсчитать сколько раз встретилось каждое число в списке."""

a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
# Поскольку у нас в этом списке могут быть только 6 значений из множества (0, 1, 2, 3, 4, 5),
# то создадим дополнительный список из 6 нулей.
count = [0] * 6  # [0, 0, 0, 0, 0, 0]
for i in a:
    count[i] += 1
print(count)  # [1, 2, 5, 5, 1, 1]

# К предыдущей задаче вывести сколько раз встретилось каждое число.
a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0] * 6
for i in a:
    count[i] += 1
for i in range(6):
    print(i, count[i])
# 0 0
# 1 2
# 2 6
# 3 5
# 4 1
# 5 1

# Убрать вывод тех значений, которые не встретились в нашем списке.
a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0] * 6
for i in a:
    count[i] += 1
for i in range(6):
    if count[i] > 0:
        print(i, count[i])
# 1 2
# 2 6
# 3 5
# 4 1
# 5 1

#  Также при помощи цикла мы можем раскрыть наш список и отсортировать его по возрастанию:
a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0] * 6
for i in a:
    count[i] += 1  # [0, 2, 6, 5, 1, 1]
for i in range(6):
    if count[i] > 0:
        print((str(i) + " ") * count[i], end="")
# 1 1 2 2 2 2 2 2 3 3 3 3 3 4 5


#  *  *  *   Задачa 2   *  *  *
"""
Дана строка и нужно подсчитать сколько раз каждая буква встречалась в строке.  
При этом не имеет разницы большая буква или нет.
"""

s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
# Создадим список из такого же числа нулей, как и букв в английском алфавите:
letters = [0] * 26
# И здесь на нулевой позиции подсчитываем количество раз,
# когда встретилась буква a, на первой позиции – буква b и т.д.
# Отсечём условным оператором все символы, которые не являются буквами.
for i in s.lower():
    # if i >= "a" and i <= "z":
    if "a" <= i <= "z":
        print(i, end="")  # j h d f h g j g k f y g g j h g k d f
"""
Установим соответствие для букв в виде: a = 0, b = 1 и т.д.
Для этого нужно воспользоваться функцией ord()
ord(a) = 97, ord(z) = 122  -->  символы букв имеют коды от 97 до 122
Индексы списка лежат в пределах от 0 до 25
В итоге, чтобы получить нужные нам значения, 
нужно отнимать от получившихся значения число 97 (ord("a") = 97, 
чтобы получить 0 необходимо 97-97, ord("z") = 122, 
чтобы получить 25 необходимо 122-97).
"""
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if "a" <= i <= "z":
        idx = ord(i) - 97
        letters[idx] += 1
for i in range(26):
    if letters[i] > 0:
        print(i, letters[i])
# 3 2
# 5 3
# 6 5
# 7 3
# 9 3
# 10 2
# 24 1

# Отобразим буквы
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in s.lower():
    if "a" <= i <= "z":
        idx = ord(i) - 97
        letters[idx] += 1  # [0, 0, 0, 2, 0, 3, 5, 3, 0, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97), letters[i])
# d 2
# f 3
# g 5
# h 3
# j 3
# k 2
# y 1

# Также мы можем отсортировать нашу строку:
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if "a" <= i <= "z":
        idx = ord(i) - 97
        letters[idx] += 1
for i in range(26):
    if letters[i] > 0:
        print(chr(i+97) * letters[i], end="")  # ddfffggggghhhjjjkky


#  *  *  *   Задачa 3   *  *  *
"""
Заполним список случайными числами в пределах от -10 до 10.
"""
import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
print(a)  # [-4, -8, -10, 4, 1, 8, 3, -7, 5, 6]

"""
В итоге нулевой индекс отвечает за число -10, первый индекс за -9 … и 20 индекс отвечает за число 10.
Значит нужно значение -10 превратить в индекс 0, -9 в 1 и т.д. 
Здесь мы видим, что необходимо сместить значение на +10
"""
import random
a = []
for i in range(10):
    a.append(random.randint(-10, 10))

count = [0] * 21
for i in a:  # [-3, 4, -4, 5, 1, 6, -8, 4, -3, 7]
    count[i + 10] += 1  # [0, 0, 1, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 1, 1, 1, 0, 0, 0]
print(a)  # [-3, 4, -4, 5, 1, 6, -8, 4, -3, 7]

for i in range(21):
    if count[i] > 0:
        print(i - 10, count[i])
# -8 1
# -4 1
# -3 2
# 1 1
# 4 2
# 5 1
# 6 1
# 7 1


#  *  *  *   Задачи   *  *  *

"""
На вход вашей программе поступает положительное целое число n, 
Вывести в порядке возрастания все цифры, которые встречались в этом числе, 
и напротив каждого также необходимо вывести сколько раз данная цифра встречалась в числе n
Input:  45654
Output: 4 2
        5 2
        6 1
"""
num = input()
# num = "45654"
cnt = [0] * 10

for el in num:
    cnt[int(el)] += 1  # [0, 0, 0, 0, 2, 2, 1, 0, 0, 0]

for i in range(10):
    if cnt[i] > 0:
        print(i, cnt[i])


"""
Сортировка подсчетом
Необходимо отсортировать список, состоящий только из чисел в пределах от -100 до 100 включительно, 
Программа получает на вход число n - количество элементов в списке, затем сами элементы списка
Вам необходимо вывести отсортированный список.
P.S. не пользуйтесь встроенной функцией sorted или методом sort
Input:  7
        -8 5 -7 4 -8 0 4
Output: -8 -8 -7 0 4 4 5
"""
n = int(input())
lst = list(map(int, input().split()))

res = []
cnt = [0] * 201
for el in lst:
    cnt[el + 100] += 1

for i in range(201):
    if cnt[i] > 0:
        res += [i - 100] * cnt[i]
print(*res)

