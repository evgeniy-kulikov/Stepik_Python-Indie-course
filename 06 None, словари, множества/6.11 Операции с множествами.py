#  6.11 Операции с множествами
""""""
# С множествами можно выполнять множество операций: находить объединение, пересечение...

"""  *  *  *  *  *  """
# Сравниваем множества setA и setB
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}

setC = {8, 9, 10}
setD = {1, 2}

setA.isdisjoint(setB)  # истина, если setA и setB не имеют общих элементов.
# False

setA == setB  # все элементы setA принадлежат setB, все элементы setB принадлежат setA.
# False

setA != setB
# True

setD == setA  # False - Множество setD полностью присутствует в множестве setA, но его длина отличается.
setD < setA   # True - Множество setD полностью присутствует в множестве setA, но его длина меньше.
setA < setD   # False

setA.issubset(setB)  # или setA <= setB - все элементы setA принадлежат setB.
# False

setA.issuperset(setB)  # или setA >= setB - аналогично.
# False


"""  *  *  *  *  *  """
# объединение нескольких множеств
setA.union(setB, ...)  # или setA | setB | ... - объединение нескольких множеств.
setN = setA | setB
# Результатом этого оператора будет новое множество


# пересечение нескольких множеств
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
setN = setA & setB
# {3, 4}
setA.intersection(setB, ...)  # или setA & setB & ... - пересечение множеств (общие элементы множеств).



# или setA - setB - ... - множество из всех элементов setA, не принадлежащие ни одному из setB.
setA.difference(setB, ...)

setB.difference(setA)  # множество из всех элементов setB, не принадлежащие ни одному из setA.

# Множество из элементов, встречающихся в каждом множестве, но не встречающиеся в обоих.
# Другими словами - операция, позволяющая получить новое множество,
# в которое включены все элементы двух множеств,
# не принадлежащие одновременно обоим исходным множествам.
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
setN = setA.symmetric_difference(setB)  # setA ^ setB
# {1, 2, 5, 6, 7}

setN = setB.symmetric_difference(setA)
# {1, 2, 5, 6, 7}


print(5 in setA)  # принадлежит ли 5 множеству setA.
len(setA)  # число элементов в множестве (размер множества).
setA.copy()  # копия множества.


#  Разность (от английского difference) двух множеств это операция, позволяющая получить новое множество,
#  в которое входят все элементы первого множества, не входящие во второе множество
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
setN = setA - setB
# {1, 2}

"""  *  *  *  *  *  """
# Операции изменения множеств

setA = setA & setB   # Перезаписываем множество setA результатом пересечения множеств setA и setB

setA &= setB  # короткая запись
setA.intersection_update(setB)   # аналогичный результат через встроенную функцию.

setA = setA | setB   # Перезаписываем множество setA результатом объединения множеств setA и setB

setA |= setB   # короткая запись
setA.update(setB)  # аналогичный результат через встроенную функцию.
setA = setA.union(setB)  # аналогичный результат через встроенную функцию.

setA = setA - setB

setA -= setB   # короткая запись
setA.difference_update(setB)  # аналогичный результат через встроенную функцию.


# Сравнение множеств
# два множества называются равными или эквивалентными,
# если они состоят из одних и тех же элементов и имеют одинаковое количество элементов.
a = {1, 2, 3}
b = {3, 1, 2}
print(a == b)  # True

#
#  *  *  *   Задачи   *  *  *
#

# 1 пересечение множеств set_a и set_b
set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75, ...}
set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31, ...}

print(len(set_a & set_b))
# или
print(len(set_a.intersection(set_b)))


# 2 объединение множеств set_a и set_b
set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75, ...}
set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31, ...}

print(len(set_a | set_b))
# или
print(len(set_a.union(set_b)))


# 3 Разность множеств
print(len(set_a - set_b))
print(len(set_b - set_a))


# 4 Симметрическая разность множеств set_a и set_b
print(len(set_a ^ set_b))
# или
print(len(set_a.symmetric_difference(set_b)))


# 5
"""
https://stepik.org/lesson/779028/step/12?thread=solutions&unit=781552
"""
words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
         'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
         'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
         'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
         'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
         'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
         'control', 'value', 'few', 'generation', 'service', 'national',
         'tradition', 'government', 'mention', 'proposal']
res = set([el for el in words if len(el) > 6])
print(len(res))

# Вариант
print(len([el for el in set(words) if len(el) > 6]))
print(len({el for el in set(words) if len(el) > 6}))


# 6
"""
Программе поступают на вход N списков, содержащих целые числа.
Для каждого введенного списка определить, сколько в нем встречается различных чисел.
Input:  2
        1 2 3 2 1
        2 2 2 2 2 2
Output: 3
        1
"""
# s = [[1, 2, 3, 2, 1], [2, 2, 2, 2, 2, 2]]
num = int(input())
s = [input().split() for el in range(num)]
for el in range(len(s)):
    print(len(set(s[el])))

# Хорошее решение
for _ in range(int(input())):
    print(len(set(input().split())))

