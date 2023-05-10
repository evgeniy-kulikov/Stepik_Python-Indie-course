# 5.4 Переходим на PyCharm
""""""

#  *  *  *   Задачи   *  *  *


"""
На вход программе поступает строка, состоящая из нескольких слов, 
знаком разделителем между словами будем считать символ пробела. 
Нужно сключить из строки дублирующие слова: 
первое появление слова остается в строке, 
второе и все последующие появления исключаются. 
При сравнении на дубли строк регистр букв не учитывать, это значит слова python и PyThOn считаются одинаковыми.
Input:  Python is best I love python
Output: Python is best I love
"""

s_in = list(input().split())
s = set()
for el in s_in:
    if el.lower() not in s:
        s.add(el.lower())
        print(el, end=' ')

# Вариант
s_in = input().split()
s = set()
for el in s_in:
    if el.lower() not in s:
        s.add(el.lower())
        print(el, end=' ')
