# 7.2 Зачем нужны функции в программировании
""""""


"""
параметры - это имена переменных, которые используются при определении функции.
аргументы - это фактические значения (данные), которые передаются функции в момент вызова.
"""
def summa(a, b):  # Имена a и b будут являться параметрами данной функции
    return a + b

lst_1 = [1, 2]
lst_2 = [4, 5, 6]
print(summa(lst_1, lst_2))  # имена lst1 и lst2 - аргументы, которые мы передаем


#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Функция repeat_please_n_times должна n раз распечатать фразу "Just do it" в отдельной строчке
"""

def repeat_please_n_times(n):
    for _ in range(n):
        print("Just do it")

def repeat_please_n_times(n):
    print("Just do it\n" * n, end="")

def repeat_please_n_times(n):
    if n != 0:
        print('Just do it')
        repeat_please_n_times(n-1)


# 02
"""
Напишите функцию is_between, которая принимает три аргумента и печатает True, 
если первое число находится между двумя вторыми включительно, и False в противном случае.
Input:  5 3 6
Output: True
"""
def is_between(a, b, c):
    ls = sorted(list([a, b, c]))
    print(ls[1] == a)


a, b, c = map(int, input().split())
is_between(a, b, c)


# 03
"""
Напишите функцию count_letter(text, letter), которая принимает два параметра:
text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
letter – буква, количество которой мы должны посчитать в text.
Функция count_letter должна выводить на экран найденное количество букв  letter в тексте text
Input:  to be or not to be
Output: b
"""
def count_letter(text, letter):
    print(text.count(letter))

text = input()
symbol = input()

count_letter(text, symbol)


# 04
"""
Функция print_initials(name, surname, middlename), принимает три параметра:
name – имя человека;
surname – фамилия человека;
middlename – отчество человека;
а затем выводит на печать фамилию и инициалы в определенном формате 
Input:  евгЕний
        петросян
        ВаГАнович
Output: Петросян Е.В.
"""


def print_initials(name, surname, middlename):
    initial = name[0].upper() + '.' + middlename[0].upper() + '.'
    print(surname.capitalize(), initial)


name = input()
surname = input()
middlename = input()
print_initials(name, surname, middlename)


# Короче
def print_initials(name, surname, middlename):
    print(f'{surname.capitalize()} {name[0].upper()}.{middlename[0].upper()}.')
