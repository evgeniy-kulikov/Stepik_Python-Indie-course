# 6.1 Значение None

""""""

"""
None — это специальный объект, принадлежащий типу данных NoneType. Он обозначает отсутствие значения.
None — это одноэлементный объект(синглтон) класса NoneType. 
Синглтон означает, что может быть только один его экземпляр. 
Фактически, все переменные, которым присвоено значение None, указывают на один и тот же объект в Python.

c = None
d = None
print(id(c), id(d))  # 140373018802496 140373018802496
print(c == d, c is d)  # True True
"""

"""
Операции со значением None:
None не поддерживает никакие математические операции. 

Сравнение со значением None:

print(None == None)  # True
print(None is None)  # True

print(None in [1, 2, 3])  # False
print(None in [1, None, 3])  # True

!!!  good practice для сравнения с None это использовать операторы is и is not

Если сравнить значение None с любым другим значением, отличным от None, всегда получите False
print(None == 1)  # False
print(None == 'Hello')  # False
print(None == '')  # False
print(None == 0)  # False
print(None == [])  # False
"""

"""
Важно отметить, что объект None имеет следующие особенности:

None не равно нулю 0 или 0.0
None не то же самое, что False
None — это не пустая строка ('')
None - это не пустой список и не любое другое значение
"""


#  *  *  *   Задачи   *  *  *


"""
Создайте две переменные empty и empty_too, сохраните в них значение None
При помощи оператора is выведите на первой строке результат их сравнения на равенство
и затем на второй строке результат их сравнения на неравенсто
"""
empty, empty_too = None, None
print(empty is empty_too)  # True
print(empty is not empty_too)  # False


"""
Создайте список i_love_none из 50 элементов None и распечатайте его
"""
i_love_none = [None] * 50
print(i_love_none)

# Вариант
print(i_love_none := [None] * 50)

