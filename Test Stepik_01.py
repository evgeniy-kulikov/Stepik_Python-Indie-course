# s = input()
# num = int(input())
# a, b = input(), input()
# num = float(input())
# title, author, page, coin = input(), input(), int(input()), float(input())
# c = input().split()
# a, b, c = map(int, input().split())
# a, b, c = int(input()), int(input()), int(input())
# a, b = map(str, input().split())
# s = list(map(int, input().split()))
# s = list(map(float, input().split()))
# lst = list(map(str, input().split()))

# множественный ввод
# h1, m1, s1, h2, m2, s2 = (int(input()) for _ in range(6))

# n = int(input())
# s = [int(input()) for el in range(n)]

"""
На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.
вывести список состоящий из указанных строк.
"""
# n = int(input())
# lst = []
# for el in range(n):
#     lst += [input()]
# [['abc'], ['def']]

# n = int(input())
# lst = []
# for el in range(n):
#     lst.append(input())

# n = int(input())
# s = [[el for el in (input())] for _ in range(n)]
# [['a', 'b', 'c'], ['d', 'e', 'f']]

# n = int(input())
# s = [[(input())] for _ in range(n)]
# [['abc'], ['def']]

# n = int(input())
# s = [(input()) for _ in range(n)]
# ['abc', 'def']

# еще короче
# s = [input() for _ in range(int(input()))]


# s = list(map(int, input().split()))
# n = int(input())
# rez = list(map(int, (n / 6,  (n / 3) * 2, n / 6)))
# print(*rez)

# n = int(input()) / 6
# rez = list(map(int, (n,  n * 4, n)))
# print(*rez)

# s = list(map(int, input().split()))
# s = [s[0] * 3, s[1] * 5, s[2] * 12]
# print(sum(s))

# s = list(map(int, input().split()))
# s = (lambda x, y, z: x * 3 + y * 5 + z * 12)(*s)
# print(s)

# s = list(map(int, input().split()))
# total = sum(s) - 1
# b1 = total - s[0]
# b2 = total - s[1]
# print(b1, b2)

"""
Вывод числа с ведущими нолями
max_width = 5
print(f'{10:0{max_width}}')      # 00010   - вывод с добавлением нолей
print(f'{-10:0{max_width}}')     # -0010   - минус забирает одну позицию
print(f'{-10000:0{max_width}}')  # -10000  - если число слишком большое, 
                                 #           строка будет длиннее, чем max_width
print(f'{10:+0{max_width}}')     # +0010   - обязательный вывод знака
print(f'{10.5:0{max_width}}')    # 010.5   - точка забирает одну позицию
print(f'{10:{max_width}}')       #    10   - можно заполнять пробелами


единицы            n % 10
десятки            n % 100 // 10
сотни              n % 1000 // 100
тысячи             n % 10000 // 1000
десятки тысяч      n // 10000"""

"""
На вход ...
Input:  ___
Output: ___
"""

# =================================================================================================================
# =================================================================================================================
# =================================================================================================================

"""
Input:  
Output: 
"""
