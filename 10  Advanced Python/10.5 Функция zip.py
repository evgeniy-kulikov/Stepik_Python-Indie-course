# 10.5 Функция zip
""""""

"""
class zip(object)
 |  zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.
 |  
 |     >>> list(zip('abcdefg', range(3), range(4)))
 |     [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
 
 
параметр strict появился начиная с версии 3.10
Он позволяет вызывать исключение в случае, если у одной из последовательностей элементы закончатся раньше чем у других. 
Параметр strict будет следить за соблюдением равенства длин переданных последовательностей. 
Если длина различается, получается ValueError 
"""

words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300, 400, 500]
result_zip = list(zip(words, numbers))
# [('approach', 100), ('monstrous', 200), ('mobile', 300), ('voucher', 400), ('solid', 500)]


# Функция zip и неограниченное количество аргументов

words = ['approach', 'monstrous', 'mobile', 'voucher', 'solid']
numbers = [100, 200, 300, 400, 500]
s = 'NaSA'

res_zip = list(zip(words, numbers, s))
# [('approach', 100, 'N'), ('monstrous', 200, 'a'), ('mobile', 300, 'S'), ('voucher', 400, 'A')]

# Распаковка значений при обходе объекта zip
for item in zip(words, numbers, s):
    print(item)
"""
('approach', 100, 'N')
('monstrous', 200, 'a')
('mobile', 300, 'S')
('voucher', 400, 'A')
"""


#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Создать словарь result, в котором пара ключ-значение берется из значений списков, 
стоящих на одинаковых индексах. В качестве ответа выведите словарь result
"""
keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = {k: v for k, v in zip(keys, values)}
print(result)

# Короче
result = dict(zip(keys, values))
print(result)


# 02
"""
https://stepik.org/lesson/372109/step/11?unit=359663
создаем пару 5: 'Anfisa'
должен получится словарь employees_data
"""
employees = [
    'Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin',
    'Leonti', 'Daniil', 'Mishka', 'Lidochka',
    'Terenti', 'Vladik', 'Svetka', 'Maks', 'Yura', 'Sergei'
]

identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]

employees_data = dict(zip(sorted(identifiers), sorted(employees)))

print(employees_data)
# {5: 'Anfisa', 17: 'Daniil', 20: 'Innokentiy', 32: 'Leonti', 37: 'Lidochka', 43: 'Maks', 48: 'Mishka',
# 56: 'Pankratiy', 62: 'Sergei', 76: 'Svetka', 77: 'Terenti', 81: 'Veniamin', 85: 'Vladik', 88: 'Yaroslava', 96: 'Yura'}


# 03
"""
https://stepik.org/lesson/372109/step/12?unit=359663
"""
# длинное решение
def zip_with_function(ls: list, func) -> list:
    rez = []
    for el in list(zip(*ls)):
        rez.append(func(*el))
    return rez

# Хорошее решение
def zip_with_function(ls, func):
    return [func(*args) for args in zip(*ls)]

# Короче
def zip_with_function(ls, func):
    return list(map(func, *ls))



def combine_strings(a: str, b: str) -> str:
    return a + b

def get_sum_two_numbers(a: int, b: int) -> int:
    return a + b

def get_sum_three_numbers(a: int, b: int, c: int) -> int:
    return a + b + c


assert zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers) == [4, 7, 12]
assert zip_with_function([[10, 20], [30, 0]], get_sum_two_numbers) == [40, 20]
assert zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers) == [10, 15, 20]
assert zip_with_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]], get_sum_three_numbers) == [12, 15, 18]
assert zip_with_function([["a", "b"], ["1", "2"]], combine_strings) == ['a1', 'b2']

