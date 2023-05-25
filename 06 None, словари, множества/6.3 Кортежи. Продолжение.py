#  6.3 Кортежи. Продолжение
""""""

# Индексация кортежей
a = (1, 'hi', 3, 54, False, 6)
print(a[1])  # hi
print(a[4])  # False
print(a[-1])  # 6


# Срезы индексов у кортежей
a = (1, 'hi', 3, 54, False, 6, 'the', True)
print(a[1:4])  # ('hi', 3, 54)
print(a[::-1])  # (True, 'the', 6, False, 54, 3, 'hi', 1)


# Неизменяемость кортежей
"""
При попытке изменить значение у кортежа по его индексу возникнет ошибка
Но если внутри кортежа имеется изменяемый объект (к примеру список), то на элементы изменяемого объекта можно влиять
"""
a = (1, 2, [10, 20], 3)
a[2].append(30)
print(a)  # (1, 2, [10, 20, 30], 3)

a[2][0] = 'hello'
print(a)  # (1, 2, ['hello', 20, 30], 3)


""" Как вносить изменения в кортеж """
# использование срезов и сцеплений (неприятный вариант)
a = (1, 'hi', 3, 54, False, 6, 'the', True)
print(a)  # (1, 'hi', 3, 54, False, 6, 'the', True)

# хотим изменить индекс 2 на значение 100 и в конец добавить значение 321
a = a[:2] + (100, ) + a[3:] + (321, )
print(a)  # (1, 'hi', 100, 54, False, 6, 'the', True, 321)


# преобразовать к списку ➔ изменение элемента ➔ преобразование в кортеж (приятный вариант):
a = (1, 'hi', 3, 54, False, 6, 'the', True)
print(a)
# хотим изменить индекс 2 на значение 100  и в конец добавить значение 999
a = list(a)
a[2] = 100
a.append(321)
a = tuple(a)
print(a)  # (1, 'hi', 100, 54, False, 6, 'the', True, 321)


"""
Методы кортежей

только два метода index и count
Метод index() - показывает первый слева индекс элемента, если он присутствует в кортеже
Метод count() выполняет подсчёт количества вхождений данного элемента в кортеж
"""
a = (1, 2, 3, 54, 8, 6, 2, 7)
print(a.index(54))  # 3
print(a.count(54))  # 1
print(a.count(100))  # 0


#  *  *  *   Задачи   *  *  *


# https://stepik.org/lesson/767366/step/5?unit=769760
# print(my_tuple[44])
# print(my_tuple[-9])


# https://stepik.org/lesson/767366/step/6?unit=769760
# slice_5_10 = my_tuple[5:11]
# slice_from_20 = my_tuple[20:]
# slice_to_35 = my_tuple[:35]
#
# print(slice_5_10)
# print(slice_from_20)
# print(slice_to_35)


# https://stepik.org/lesson/767366/step/7?unit=769760
# print(my_tuple[::-1])


# https://stepik.org/lesson/767366/step/8?unit=769760
# print(my_tuple.count(50))


# https://stepik.org/lesson/767366/step/11?unit=769760
words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
               'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
               'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')

for el in range(len(words_tuple)):
    print(f'Длина слова {words_tuple[el]} = {len(words_tuple[el])}')


# https://stepik.org/lesson/767366/step/12?thread=solutions&unit=769760
my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518,
            -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696,
            993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407,
            -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66,
            -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917,
            32, 422, -895, 198, 284, 472, -986, -964, -73, 29)


lst = [el for el in list(my_tuple) if el % 2 != 0]
res = sum(lst) / len(lst)
print(res)  # -18.0

