# 5.2 Цикл for. Обход элементов функции range
""""""
from random import randint

for i in range(5):

    a = randint(1, 100)
    print(a, end=" ")  # 38 89 99 35 80
                       # 58 9 100 84 84


#  *  *  *   Задачи   *  *  *


#
"""
Программа принимает на вход натуральное число N. 
Вывести на экран все числа от 1 до N, каждое число на отдельной строке. 
Input:  3
Output: 1
        2
        3
"""
num = int(input())
for el in range(1, num + 1):
    print(el)


#
"""
Вывести все элементы арифметической прогрессии от 0 до 500 включительно с шагом 5.
Input:  -
Output: 0
        5
        10
        ...
        495
        500
"""
for el in range(0, 501, 5):
    print(el)

#
"""
Программа принимает на вход натуральное число N
Вывести все числа от N до 1 в сторону уменьшения
Input:  3
Output: 3
        2
        1
"""
num = int(input())
for i in range(num, 0, -1):
    print(i)


#
"""
вывести 13 раз фразу «Надо было брать биткоин в 2012!», каждый раз на отдельной строк
Input:  -
Output: -
"""
for i in range(13):
    print('Надо было брать биткоин в 2012!')


#
"""
На вход  поступает фраза и затем количество раз, которое эту фразу нужно повторить.
Input:  -
Output: -
"""
s = input()
num = int(input())
for i in range(num):
    print(s)

#
"""
Напишите программу, которая считывает два натуральных числа a и b (гарантируется, что a < b), 
после чего для всех чисел от a до b включительно выводит:
“Fizz”, если это число делится на 3;
“Buzz”, если это число делится на 5;
“FizzBuzz”, если выполнены оба предыдущих условия;
само это число в остальных случаях.
Input:  9
        15
Output: Fizz
        Buzz
        11
        Fizz
        13
        14
        FizzBuzz
"""
n1, n2 = int(input()), int(input())
for el in range(n1, n2 + 1):
    if el % 3 == 0:
        print('Fizz')
    elif el % 5 == 0:
        print('Buzz')
    elif el % 15 == 0:
        print('FizzBuzz')
    else:
        print(el)


#
"""
На вход программе подается два натуральных числа a и b (гарантируется, что a<b), 
после чего для каждого целого числа на интервале от a до b включительно 
необходимо вывести фразу следующего вида:
«Число {число}; его квадрат = {квадрат}; его куб = {куб}»
Input:  1
        5
Output: Число 1; его квадрат = 1; его куб = 1
        Число 2; его квадрат = 4; его куб = 8
        Число 3; его квадрат = 9; его куб = 27
        Число 4; его квадрат = 16; его куб = 64
        Число 5; его квадрат = 25; его куб = 125
"""
n1, n2 = int(input()), int(input())
for el in range(n1, n2 + 1):
    print(f'Число {el}; его квадрат = {el ** 2}; его куб = {el ** 3}')


#
"""
Если перечислить все натуральные числа ниже 10, которые кратны 3 или 5, 
то получим 3, 5, 6 и 9. Сумма этих чисел 23.
Напишите программу, которая принимает натуральное число n и 
находит сумму всех чисел ниже переданного числа n, которые делятся на 3 или на 5.
Input:  10
Output: 23
"""
num = int(input())
sum_el = 0
for el in range(1, num):
    if el % 3 == 0 or el % 5 == 0:
        sum_el += el
print(sum_el)


#
"""
Поступает на вход одно целое число n (n >= 0)
Найдите и выведите на экран  n! (n!=1∗2∗3∗...∗n)
4!=1∗2∗3∗4=24
Input:  4
Output: 24
"""
num = int(input())
fact = 1
for el in range(1, num + 1):
    fact *= el
print(fact)


#
"""
Мишка и игра
Input:  3
        3 5
        2 1
        4 2
Output: Mishka
"""
num = int(input())
res_1, res_2 = 0, 0
for el in range(num):
    n1, n2 = map(int, input().split())
    if n1 > n2:
        res_1 += 1
    elif n2 > n1:
        res_2 += 1

if res_1 == res_2:
    print('Friendship is magic!^^')
else:
    print('Mishka' if res_1 > res_2 else 'Chris')


#
"""
На первой строке вводится натуральное число N — количество строк.
Далее следуют N строк.
Найдите, в каких строках из введённых и в каком месте упоминается "рок" (регистр букв не важен)
Для каждой строки, в которой есть сочетание символов «рок», 
нужно вывести (в порядке появления таких строк) номер этой строки (нумерация начинается с единицы) и 
номер символа, с которого начинается первое вхождение этой подстроки (нумерация символов также с единицы).
Input:  3
        Порок
        Учитель
        Рок
Output: 1 3
        3 1
"""
num = int(input())
for el in range(1, num + 1):
    s = input().lower()
    if 'рок' in s:
        print(el, (s.find('рок') + 1))


#
"""
https://stepik.org/lesson/296960/step/14?thread=solutions&unit=278688
Предположим, вы переписываете у друга рецепты в блокнотик, 
но вам не нравится "соль". Переписывайте без этого слова.
Input:  -
Output: -
"""
num = int(input())
res = ''
for el in range(num):
    s = input()
    if not 'соль' in s:
        res += s + ', '
print(res[:-2])

# Вариант
n=int(input())
a=[]
for i in range(n):
    s=input()
    if not 'соль' in s:
        a.append(s)
print(', '.join(a))


# https://stepik.org/lesson/296960/step/15?unit=278688
"""
Будем считать слово слишком длинным, если его длина строго больше 10 символов. 
«civilization» запишется как «c10n», а «internationalization» как «i18n».
Input:  4
        word
        civilization
        internationalization
        pneumonoultramicroscopicsilicovolcanoconiosis
Output: word
        c10n
        i18n
        p43s
"""
num = int(input())
for el in range(num):
    s = input()
    if len(s) > 10:
        s = s[0] + str(len(s) - 2) + s[-1]
        print(s)
    else:
        print(s)

