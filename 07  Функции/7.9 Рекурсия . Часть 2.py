# 7.9 Рекурсия в Python. Рекурсивная функция Часть 2
""""""

# Дробление строки открывающими и закрывающими строками
def rec_str(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + ' (' + rec_str(s[1:-1]) + ') ' + s[-1]

string = 'input'
print(rec_str(string))  # i (n (p) u) t

string = 'return'
print(rec_str(string))  # r (e (tu) r) n



# Возведение в степень
# Возведение числа в целую степень (положительная степень числа)
"""
2^10 = 2^5 * 2^5
2^5 = 2^4 * 2^1
2^4 = 2^2 * 2^2
2^2 = 2^1 * 2^1
2^1 = 2^1 * 2^0
2^0 = 1
"""

def rec_power(num, degree):
    if degree == 0:  # 2^0 = 1
        return 1
    elif degree % 2 == 0:
        return rec_power(num, degree // 2) * rec_power(num, degree // 2)  # 2^4 = 2^2 * 2^2
    else:
        return rec_power(num, degree - 1) * num  # 2^5 = 2^4 * 2^1

num, degree = 2, 10
print(rec_power(num, degree))  # 1024


# Возведение числа в целую степень (положительная и отрицательная степень числа)
"""
2^3 = (1 / 2)^-3
"""

def rec_power(num, degree):
    if degree == 0:  # 2^0 = 1
        return 1
    elif degree < 0:
        return 1 / rec_power(num, - degree)  # Отрицательная степень числа
    elif degree % 2 == 0:
        return rec_power(num, degree // 2) * rec_power(num, degree // 2)  # 2^4 = 2^2 * 2^2
    else:
        return rec_power(num, degree - 1) * num  # 2^5 = 2^4 * 2^1

num, degree = 5, -4
print(rec_power(num, degree))  # 0.0016




# Определение глубины вложенности списков

def rec_list(lst, level=1):
    print(*lst, 'level =', level)

ls = [1, [8, 9], 2, [2, 3, 4, [5, 6], 7]]
rec_list(ls)  # 1 [8, 9] 2 [2, 3, 4, [5, 6], 7] level = 1



def rec_list(lst, level=1):
    print(*lst, 'level =', level)
    for el in lst:
        if type(el) == list:
            rec_list(el, level + 1)

ls = [1, [8, 9], 2, [2, 3, 4, [5, 6], 7]]
rec_list(ls)
"""
1 [8, 9] 2 [2, 3, 4, [5, 6], 7] level = 1
8 9 level = 2
2 3 4 [5, 6] 7 level = 2
5 6 level = 3
"""



# Посчитать сумму чисел, введенных с клавиатуры:

def rec_sum(n):
    if n == 1:  # Обработка крайнего случая
        return int(input())
    return rec_sum(n - 1) + int(input())  # Обработка рекуррентного случая

num = 3  # число цифр
print(rec_sum(num))
