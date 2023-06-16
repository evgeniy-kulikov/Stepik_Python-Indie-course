# 7.3 Возвращаемое значение функции. Оператор return
""""""

#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
https://stepik.org/lesson/296972/step/6?unit=278700
Инструкция assert
глагол assert с английского переводится как «утверждать»
Утверждение — это логическое выражение, которое проверяет, является ли утверждение истинным или ложным.
Инструкция assert может использоваться для проверки правильности выполнения кода. 
При помощи assert  вы можете написать тесты и проверить работоспособность своей функции. 
"""

assert 200 > 100
assert [100] * 4 < [100, 100, 100, 10000]
assert sum([1, 3, 5]) == sum([6, 3])
assert min(3, -1, 9) == -1
print('Проверки пройдены')


# 02
"""
https://stepik.org/lesson/296972/step/7?unit=278700
"""
def is_person_teenager(age):
    return 11 < age < 18


# 03
"""
Напишите функцию factorial, которая принимает на вход одно неотрицательное число, 
и возвращает значение факториала данного числа.
"""

def factorial(n):
    fact = 1
    for el in range(2, n + 1):
        fact *= el
    return fact

n = int(input())
print(factorial(n))


# Решение с рекурсией
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

n = int(input())
print(factorial(n))


# 04
"""
https://stepik.org/lesson/296972/step/9?unit=278700
Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число n - размер списка. 
Функция generate_fizz_buzz_list должна:
обойти числа от 1 до n включительно и для каждого такого числа выполнить последовательно проверки с пункта 2 по пункт 5
- Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz 
- Если число кратно трем, то в список заносим строку Fizz
- Если число кратно пяти, то в список заносим строку Buzz
- Если число не кратно ни трем ни пяти, то в список заносим само это число
В итоге функция generate_fizz_buzz_list должна вернуть сформированный список из n элементов
Input:  10
Output: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
"""
def generate_fizz_buzz_list(n):
    ls = []
    for el in range(1, n + 1):
        if el % 15 == 0:
            ls.append('FizzBuzz')
        elif el % 3 == 0:
            ls.append('Fizz')
        elif el % 5 == 0:
            ls.append('Buzz')
        else:
            ls.append(el)
    return ls


# n = int(input())
# res = generate_fizz_buzz_list(n)
# print(res)


# 05
"""
Дана готовая функция gcd(a, b), 
которая принимает два числа и находит наибольших общий делитель для них.
Необходимо при помощи функции gcd определить НОД произвольного количества чисел.
На первой строке вводится натуральное число n – количество чисел. 
Далее идут n строк, в каждой из которых натуральное число.
Input:  3
        15
        18
        27
Output: 3
"""
# num = 3
# ls = [15, 18, 27]
# num = 4
# ls = [3, 5, 9, 18]

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

num = int(input())
ls = [int(input()) for el in range(num)]

res = gcd(ls[0], ls[1])

for el in range(2, num):
    res = gcd(res, ls[el])

print(res)


# 06
"""
Написать функцию find_duplicate, которая принимает один аргумент - список чисел. 
Функция должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке, 
в котором они встречаются в исходном списке. 
Под дублем будем подразумевать число, которое присутствовало в списке несколько раз. 

assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
print('Все успешно')
"""
def find_duplicate(ls: list):
    double = []
    for el in ls:
        if ls.count(el) > 1 and el not in double:
            double.append(el)
    return double


# 07
"""
Написать функцию first_unique_char, которая принимает строку символов 
и возвращает целое число: позицию первого уникального символа в строке. 
В случае, если уникальных символов в переданной строке нет, верните -1. 
Регистр символов не учитывать.
Input:  python
Output: 0
Input:  abraCadabra
Output: 4
Input:  abcabc
Output: -1
"""
def first_unique_char(s: str):
    for i, el in enumerate(s):
        if s.count(el) == 1:
            return i
    return -1

s = input().lower()
print(first_unique_char(s))


# 08
"""
Написать функцию format_name_list, которая принимает список словарей, 
у каждого словаря в этом списке есть только ключ name.
Функция format_name_list должна вернуть строку, 
в которой все имена из списка разделяются запятой кроме последних двух имен, 
они должны быть разделены союзом "и". 
Если в списке нет ни одного имени, функция должна вернуть пустую строку.

format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) => 'Bart, Lisa и Maggie'
format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) => 'Bart и Lisa'
format_name_list([{'name': 'Bart'}]) => 'Bart'
format_name_list([]) => ''
"""
def format_name_list(names: list):
    ls = [el.get('name') for el in names]  # ['Bart', 'Lisa', 'Maggie']
    if len(ls) > 1:
        return ', '.join(ls[:-1]) + ' и ' + ''.join(ls[-1:])
    return ''.join(ls)

names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
# names = [{'name': 'Bart'}, {'name': 'Lisa'}]
# names = [{'name': 'Bart'}]
# names = []

print(format_name_list(names))


# 09
"""
Написать функцию get_domain_name, которая принимает строку url, 
извлекает из нее доменное имя и возвращает его в качестве строки

"http://google.com" == "google"
"http://google.co.jp" == "google"
"www.xakep.ru" == "xakep"
"https://youtube.com" == "youtube"
"http://github.com/carbonfive/raygun" =='github'
"http://www.zombie-bites.com" == 'zombie-bites'
"https://www.siemens.com" == 'siemens'
"https://www.mywww.com" == 'mywww'
"""

def get_domain_name(url: str):
    if '://' in url:
        ls = url.split('://')[1].split('.')
        if ls[0] != 'www':
            return ls[0]
        return ''.join(ls[1])
    return url.split('.')[1]


# Вариант (гораздо лучше)
def get_domain_name(url):
    if 'www' in url:
        return url.split('.')[1]
    return url.split('//')[1].split('.')[0]

# Короче
def get_domain_name(url: str):
    res = url.replace('http://', '').replace('https://', '').replace('www.', '', 1).split('.')
    return res[0]

# print(get_domain_name("https://youtube.com"))


# 10
"""
Сколько нулей на конце факториала N!
https://stepik.org/lesson/296972/step/15?unit=278700

Необходимо воспользоваться уже готовой функцией factorial, 
которая принимает неотрицательное число, и возвращает значение факториала данного числа.
Создать функцию trailing_zeros, которая принимает неотрицательное число, 
находит его факториал и возвращает сколько нулей на конце этого факториала .

trailing_zeros(6) =>  1, потому что 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
trailing_zeros(10) => 2, потому что 10! = 3 628 800
trailing_zeros(20) => 4, потому что 20! = 2 432 902 008 176 640 000
"""
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n):
    s = str(factorial(n))
    n = 0
    while s.endswith('0'):
        n += 1
        s = s[:-1]
    return n


# Короче
def trailing_zeros(n):
    fact = str(factorial(n))
    return len(fact) - len(fact.rstrip('0'))

# print(trailing_zeros(10))


# 11
"""
Азотистые основания нуклеотидов ДНК
https://stepik.org/lesson/296972/step/16?unit=278700

Создать функцию count_AGTC, которая принимает на вход строку - последовательность ДНК, 
состоящая только из символов A, G, T, C. 
Функция count_AGTC должна подсчитать количество каждого элемента в переданной последовательности 
и вернуть кортеж из найденных четырех количеств. 
Порядок элементов в кортеже должен быть именно таким A, G, T, C

count_AGTC('AGGTC') => (1, 2, 1, 1)
count_AGTC('AAAATTT') => (4, 0, 3, 0)
count_AGTC('AGTTTTT') => (1, 1, 5, 0)
count_AGTC('CCT') => (0, 0, 1, 2)
"""
def count_AGTC(dna: str):
    return dna.count('A'), dna.count('G'), dna.count('T'), dna.count('C')

# Короче
def count_AGTC(dna):
    return tuple(dna.count(el) for el in 'AGTC')
