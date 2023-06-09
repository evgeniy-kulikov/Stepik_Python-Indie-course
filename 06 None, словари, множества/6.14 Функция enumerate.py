# 6.14 Функция enumerate
""""""

"""
Функция enumerate помогает обойти итерируемые коллекции 
с возможностью одновременно получать индекс элемента и его значение.
Функция enumerate возвращает итератор, который можно легко преобразовать например к списку.
"""
a = [10, 20, 30, 40]
print(list(enumerate(a)))  # [(0, 10), (1, 20), (2, 30), (3, 40)]

for index, value in enumerate(a):
    print(index, value)
"""
0 10
1 20
2 30
3 40
"""

#  Функция по умолчанию считает индексы с нуля, но можно при помощи параметра start задать начальное значение отсчета
for index, value in enumerate(a, start=10):
    print(index, value)
"""
10 10
11 20
12 30
13 40
"""



#
#  *  *  *   Задачи   *  *  *
#


# 1
"""
https://stepik.org/lesson/766214/step/3?unit=768547
на основании создать список кортежей words_with_position, 
каждый элемент-кортеж должен содержать два значения: само слово и его порядковый номер в списке words
Input:  words = ['variation', 'random', 'electronics', 'competence', 'collapse']
Output: words_with_position = [('variation', 1),
                               ('random', 2), 
                               ('electronics', 3), 
                               ('competence', 4), 
                               ('collapse', 5)]
"""
words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
         'drop', 'produce', 'acquisition', 'cheap', 'strength',
         'master', 'perception', 'noise', 'strange', 'am']

res = [(el[1], el[0]) for el in enumerate(words, start=1)]
print(res)

# Оригинальное решение
res = [el[::-1] for el in enumerate(words, start=1)]
print(res)

# Короче
res = [(b, a) for a, b in enumerate(words, 1)]
print(res)


# 2
"""
https://stepik.org/lesson/766214/step/4?unit=768547
Дан кортеж english_words
При помощи enumerate обойдите слова этой коллекции и для каждого элемента выведите строку вида:
Word № {number} = {word}
Например, для кортежа english_words = ('hi', 'World') ответ был бы таким:
Word № 1 = hi
Word № 2 = World
"""
english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')

for num, word in enumerate(english_words, 1):
    print(f'Word № {num} = {word}')


# 3
"""
https://stepik.org/lesson/766214/step/5?unit=768547
Алгоритм Луна
Упрощенная версия алгоритма Луна выглядит так:
- Цифры проверяемой последовательности нумеруются справа налево.
- Цифры, оказавшиеся на нечётных местах, остаются без изменений.
- Цифры, стоящие на чётных местах, умножаются на 2.
- Если в результате такого умножения возникает число больше 9, оно уменьшается на значение 9
- Все полученные в результате преобразования 16 цифр складываются. Если сумма кратна 10, то исходные данные верны.

Input:  3942682966937054
Output: True

Input:  2553514623369426
Output: False
"""
# card = [(0, 3), (1, 9), (2, 4), (3, 2), (4, 6), (5, 8), (6, 2), (7, 9), (8, 6), (9, 6), (10, 9), (11, 3), (12, 7),
#         (13, 0), (14, 5), (15, 4)]

card = list(enumerate(map(int, input())))

odd, even = 0, 0
for i, v in card:
    if i % 2 == 0:
        v *= 2
        if v > 9:
            v -= 9
            even += v
        else:
            even += v
    else:
        odd += v

print((odd + even) % 10 == 0)


# Хорошее решение
card = [int(i) for i in input()]
for i in range(0, len(card), 2):
    card[i] *= 2
    if card[i] > 9:
        card[i] -= 9
print(sum(card) % 10 == 0)
