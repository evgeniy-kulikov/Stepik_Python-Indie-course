# 8.2 Импорт стандартных модулей
""""""


#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Импортируйте стандартный модуль os и выведите на экран значение переменной name из этого модуля
"""
import os
print(os.name)  # 'nt'


# 02
"""
https://stepik.org/lesson/372098/step/7?unit=359652
"""
print(os.environ.get('HOME'))  # None



# 03
"""
https://stepik.org/lesson/372098/step/8?unit=359652
"""
from string import Template


values = {'one': 'Привет', 'copter': 'Квадракоптер'}

t = Template("""
Ну что, мои хорошие, всем $one
Это шаблонная строка
В нее можно вставлять значения по ключам
Хочу сюда вставлю слово $copter, хочу сюда $copter
""")

print(t.substitute(values))


# 04
"""
https://stepik.org/lesson/372098/step/9?unit=359652
"""
from sys import getrecursionlimit

rez = getrecursionlimit()
print(rez)  # 1000


# 05
"""
https://stepik.org/lesson/372098/step/10?unit=359652
Из модуля string импортируйте следующие переменные: 

ascii_lowercase - строка, содержащая английский буквы англ. алфавита в нижнем регистре
ascii_uppercase - строка, содержащая английский буквы англ. алфавита в верхнем регистре
punctuation - строка, содержащая символы пунктуации
Необходимо в отдельных строках вывести сперва все знаки пунктуации, 
затем заглавные символы и уже потом маленькие.
"""
from string import ascii_lowercase as a_low, ascii_uppercase as a_up, punctuation as pn

print(pn, a_up, a_low, sep='\n')

# Вариант
[print(_) for _ in [pn, a_up, a_low]]

# Вариант
for _ in [pn, a_up, a_low]:
    print(_)
