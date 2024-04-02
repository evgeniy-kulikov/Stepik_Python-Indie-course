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


#  *  *  *   Задачи   *  *  *


# 01
"""
Имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен. 
Ключами словаря на любом уровне могут быть только строки, значения - только числа. 
Преобразовать этот вложенный словарь в плоский (состоящий только из одного уровня), 
где ключи формируются конкатенацией вложенных ключей, соединенных знаком _
Для этого необходимо определить рекурсивную функцию flatten_dict.
"""
def flatten_dict(input_dict: dict, key: str = '') -> dict:
    nested_dict = dict()
    for k, v in input_dict.items():
        if type(v) == int:
            nested_dict.update({f"{key}_{k}"[1:]: v})  # ключ без первого эл-та "_"
        else:
            nested_dict.update(flatten_dict(v, key=f"{key}_{k}"))
    return nested_dict

# Код для проверки
assert flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}) == {'Q_w_E_r_T_y': 123}
assert flatten_dict({'Germany_berlin': 7,
                     'Europe_italy_Rome': 3,
                     'USA_washington': 1,
                     'USA_New York': 4}) == {'Germany_berlin': 7, 'Europe_italy_Rome': 3, 'USA_washington': 1,
                                             'USA_New York': 4}
assert flatten_dict({'a': 100, 'b': 200}) == {'a': 100, 'b': 200}
assert flatten_dict(
    {'Geeks': {'for': {'for': 1, 'geeks': 4}}, 'for': {'geeks': {'Geeks': 3}}, 'geeks': {'Geeks': {'for': 7}}}) == \
    {'Geeks_for_geeks': 4, 'for_geeks_Geeks': 3, 'geeks_Geeks_for': 7, 'Geeks_for_for': 1}
assert flatten_dict(
    {"a": 1, "b": {"c": 2, "d": 3, "e": {"f": 4, '6': 100, '5': {"g": 6}, "l": 1}}}) == \
    {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 100, 'b_e_5_g': 6, 'b_e_l': 1}
print("good")


# 02
"""
https://stepik.org/lesson/372095/step/3?unit=359649
"""
# функция merge_two_list должна объединить два списка
def merge_two_list(a, b):
    i = j = 0
    c = list()
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


# функция merge_sort должна выполнить сортировку
def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


# 03
"""
https://stepik.org/lesson/372095/step/4?unit=359649
функция quick_sort должна выполнить сортировку
"""
def quick_sort(s):
    if len(s) <= 1:  # Если длина списка меньше 1
        return s  # То список является отсортированным.
    n = s.pop(len(s) // 2)  # Выбираем "опорный" элемент , выберем средниЙ(медианный) как опорный
    less = [i for i in s if i <= n]  # Элементы меньше выбранного элемента
    more = [i for i in s if i > n]  # Элементы больше выбранного элемента

    return quick_sort(less) + [n] + quick_sort(more)
    # Возвращаем левую отсортированную часть опорный элемент и правую отсортированную часть
