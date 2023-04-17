# 4.3 Обход всех цифр числа с помощью while
""""""

# Обход всех цифр числа
n = 4782
while n > 0:
    print(n % 10, end=' ')
    n = n // 10
# 2 8 7 4


# Обход всех цифр числа в двоичной системе
n = 14
while n > 0:
    print(n % 2, end='')
    n = n // 2
# 0111 - вывод в обратном порядке. На самом деле должно быть 1110

# Узнаем сколько разрядов в числе
n = int(input())
count = 0  # Количество цифр
while n > 0:
    n = n//10
    count += 1
print(count)

#  Найдем сколько всего четных цифр
n = int(input())
count_even = 0  # Количество четных цифр
while n > 0:
    last = n % 10
    if last % 2 == 0:
        count_even = count_even + 1
    n = n//10
print(count_even)

# Посчитаем сумму всех цифр числа
n = int(input())
s = 0  # Сумма всех цифр
while n > 0:
    s = s + n % 10
    n = n//10
print(s)

#  Посчитаем произведение всех цифр числа
n = int(input())
product = 1  # Произведение всех цифр
while n > 0:
    last = n % 10
    product = product * last
    n = n//10
print(product)

# Найдем самую большую и самую маленькую цифру в числе
n = int(input())
maximum = 0
minimum = 9
while n > 0:
    last = n % 10
    if last > maximum:
        maximum = last
    if last < minimum:
        minimum = last
    n = n//10
print(maximum)
print(minimum)


#  *  *  *   Задачи   *  *  *

# Отложенные решения на отпуск (11)
# https://stepik.org/lesson/296615/step/6?unit=278349
"""
Программа принимает на вход одно натуральное число и выводит его цифры в столбик в обратном порядке.
Input:  412
Output: 2
        1
        4
"""
n = int(input())
while n > 0:
    print(n % 10)
    n = n // 10


# Отложенные решения на отпуск (12)
# https://stepik.org/lesson/296615/step/7?unit=278349
"""
Программа принимает на вход одно натуральное число и выводит на экран сумму цифр данного числа
Input:  123
Output: 6
"""
n = int(input())
s = 0
while n > 0:
    s += n % 10
    n = n // 10

print(s)

# Отложенные решения на отпуск (13)
# https://stepik.org/lesson/296615/step/8?unit=278349
"""
Программа принимает на вход одно натуральное число и выводит на экран произведение цифр данного числа
Input:  415
Output: 20
"""
n = int(input())
mult = 1
while n > 0:
    mult *= n % 10
    n = n // 10

print(mult)

# Отложенные решения на отпуск (14)
# https://stepik.org/lesson/296615/step/9?unit=278349
"""
Программа принимает на вход одно натуральное число и 
выводит на экран минимальную и максимальную цифры данного числа в отдельных строчках
Input:  480
Output: 0
        8
"""
n = int(input())
n_min = n_max = n % 10
while n > 0:
    last = n % 10
    if last < n_min:
        n_min = last
    elif last > n_max:
        n_max = last
    n = n // 10

print(n_min, n_max, sep='\n')


# Отложенные решения на отпуск (15)
# https://stepik.org/lesson/296615/step/10?unit=278349
"""
Программа принимает на вход одно натуральное число. Найти сколько раз встречается цифра 7 в этом числе
Input:  777
Output: 3

"""
n = int(input())
cnt = 0
while n > 0:
    last = n % 10
    if last % 7 == 0:
        cnt += 1
    n = n // 10

print(cnt)


# Отложенные решения на отпуск (16)
# https://stepik.org/lesson/296615/step/11?unit=278349
"""
Программа принимает на вход одно натуральное число и выводит его цифры в двоичной системе в столбик в обратном порядке.
Input:  8
Output: 0
        0
        0
        1
"""
n = int(input())
while n > 0:
    print(n % 2)
    n = n // 2

