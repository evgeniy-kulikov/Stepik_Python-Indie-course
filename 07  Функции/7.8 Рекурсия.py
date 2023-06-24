# 7.8 Рекурсия
""""""

def rec(a):
    if a < 4:
        print(a, end=' ')  # 1 2 3
        rec(a + 1)
        print(a, end=' ')  # 3 2 1

rec(1)  # 1 2 3 3 2 1


# Факториал от числа n
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n

print(fact(4))  # 24
"""
Мы вызвали функцию fact(4), которая будет равняться

fact(4) = fact(3) * 4,  
fact(3) = fact(2) * 3,
fact(2) = fact(1) * 2,
fact(1) = 1. 

И получается раз fact(1) = 1, то fact(2) = 1 * 2 = 2, fact(3) = 2 * 3=6, fact(4) = 6 * 4 = 24.
"""


# Нахождение чисел Фибоначчи
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(6))

"""
0, 1 - первые два числа ряда
Fib(n) = Fib(n−1) + Fib(n−2)
0, 1, 1, 2, 3, 5, 8, 13, 21 .....
"""


def is_palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])

print(is_palindrom("шалаш"))




def room(person: int = 1, capacity: int = 3):
    """Пример рекурсии наполнения комнаты
    по одному человеку при полном заполнении начинают выходить
    P.S. начальное количество людей в комнате остается"""
    if person <= capacity:
        print(f"There are {person} people in the room")
        room(person + 1, capacity)
        print(f"{person} people left in the room")  # при выгрузке стека
    else:
        print(f"* Maximum person in the room: {capacity} *")

room()


# 01
"""
Определите функцию print_from, которая принимает одно натуральное число n 
и распечатывает на экране убывающую последовательность целых чисел от n до 1 включительно. 
Input:  4
Output: 4
        3
        2
        1
"""
def print_from(n: int) -> None:
    if n > 0:
        print(n)
        print_from(n - 1)

# Вариант
def print_from(n: int) -> None:
    if n:
        print(n)
        print_from(n - 1)


# 02
"""
Определите функцию print_to, которая принимает одно натуральное число n 
и распечатывает на экране последовательность целых чисел от 1 до n включительно.
Input:  3
Output: 1
        2
        3
"""
def print_to(n: int) -> None:
    if n > 0:
        print_to(n - 1)
        print(n)


# 03
"""
Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эту последовательность в обратном порядке
Input:  5
        5 9 3 2 7
Output: 7 2 3 9 5
"""
# num = 5
# ls = [5, 9, 3, 2, 7]

num = int(input())
ls = input().split()  # ['5', '9', '3', '2', '7']


def rec_list(n: int):
    if n > 0:
        # print(ls.pop(), end=' ')  # можно и так
        rec_list(n - 1)
        print(ls.pop(), end=' ')

rec_list(num)


# Вариант
def rec_list(lst: list):
    if lst:
        print(lst[-1], end=' ')
        rec_list(lst[:-1])

rec_list(ls)


# 04
"""
https://stepik.org/lesson/372094/step/8?unit=359648
Двойной факториал
if n == 1  =>  1
if n == 2  =>  2
if n > 2  =>  n * (n - 2) * (n - 4) * (n - 6) * . . .

Output:
double_fact(7) => 105
double_fact(4) => 8
double_fact(5) => 48
double_fact(1) => 1
double_fact(10) => 3840
"""
def double_fact(n: int):
    if n < 3:
        return n
    return double_fact(n - 2) * n


# 05
"""
https://stepik.org/lesson/372094/step/9?unit=359648
Числа Фибоначчи
if n == 0  =>  0
if n == 1  =>  1
if n > 1  =>  fib(n - 1) + fib(n - 2)

Input:  10
Output: 55
"""
def rec_fib(n: int):
    if n < 2:
        return n
    return rec_fib(n - 1) + rec_fib(n - 2)


n = int(input())
print(rec_fib(n))


# 06
"""
https://stepik.org/lesson/372094/step/10?unit=359648
Числа Трибоначчи
Описать рекурсивную функцию tribonacci, 
которая принимает на вход целое число n - порядковый номер чисел Трибоначчи. 
Функция по параметру n должна вычислить и вернуть значение, 
стоящее на n-м месте в ряде чисел Трибоначчи
if n == 0  =>  0
if n == 1  =>  0
if n == 2  =>  1
if n > 1  =>  tr(n - 1) + tr(n - 2) + tr(n - 3)

Output:
tribonacci(0) => 0
tribonacci(2) => 1
tribonacci(4) => 2
tribonacci(6) => 7
tribonacci(7) => 13
"""
def tribonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


# 07
"""
https://stepik.org/lesson/372094/step/11?unit=359648
Число сочетаний
Описать рекурсивную функцию get_combin, 
которая принимает на вход два целых числа  и находит C(N,K)
— число сочетаний из N элементов по K — с помощью рекуррентного соотношения:
if k == 0  =>  1
if k == n  =>  1
if 0 < k < n  =>  C(n - 1, k) + C(n - 1, k - 1)

Output:
get_combin(5, 5) => 1
get_combin(5, 2) => 10
get_combin(3, 1) => 3
get_combin(7, 0) => 1
"""
def get_combin(n: int, k: int):
    if k == 0:
        return 1
    if k == n:
        return 1
    if 0 < k < n:
        return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


# 08
"""
https://stepik.org/lesson/372094/step/12?unit=359648
Функция Аккермана
Описать рекурсивную функцию ackermann, 
которая принимает на вход два целых числа  m и n находит значение, определенное следующим образом:
            /  if m == 0  =>  n + 1
A(m, n) =  { if m > 0, n == 0  =>  A(m - 1, 1)
            \  if m > 0, n > 0  =>  A(m - 1, A(m, n - 1))
Найденное значение функция ackermann должна вернуть в качестве результата
Output:
ackermann(3, 2) => 29
ackermann(3, 0) => 5
ackermann(1, 0) => 2
ackermann(3, 5) => 253
"""
def ackermann(m: int, n: int):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


# 09
"""
Напишите функцию list_sum_recursive, 
которая принимает на вход список из целых чисел и возвращает сумму элементов переданного списка. 
Input:  1 2 3
Output: 6
"""
def list_sum_recursive(ls: list) -> int:
    if not ls:
        return 0
    return ls[0] + list_sum_recursive(ls[1:])

# lst_num = [1, 2, 3]
# print(list_sum_recursive(lst_num))


# 10
"""
https://youtu.be/BbII9GhLkxs
Превращаем вложенный список в плоский
Есть список целых чисел неограниченной вложенности. 
То есть список может состоять из списков, внутри которых также могут быть списки. 
Необходимо превратить его в линейный список при помощи функции flatten
Output:
flatten([1, [2, 3, [4]], 5]) => [1, 2, 3, 4, 5]
flatten([1, [2, 3], [[2], 5], 6]) => [1, 2, 3, 2, 5, 6]
flatten([[[[9]]], [1, 2], [[8]]]) => [9, 1, 2, 8]
"""
def flatten(ls: list) -> list:
    if not ls:
        return []
    if isinstance(ls[0], list):
        return flatten(ls[0]) + flatten(ls[1:])
    return ls[:1] + flatten(ls[1:])


# Вариант
def flatten(ls):
    res = []
    for el in ls:
        if isinstance(el, int):
            res.append(el)
        else:
            res += flatten(el)
    return res

# print(flatten([7, [[9]], [1, 2]]))
