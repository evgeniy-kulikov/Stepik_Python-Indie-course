# 9.2 Контекстный менеджер
""""""

# Создание менеджера контекста
with open('passwords.txt', 'w') as f:
    f.write('123')
    f.write('hello2')
print('end')
print(f)  # <_io.TextIOWrapper name='passwords.txt' mode='w' encoding='cp1251'>


# Функция os.scandir позволяет сканировать текущую папку и всё содержимое её помещается в entries.
import os
with os.scandir('.') as entries:  # текущая папка
# with os.scandir('..') as entries:  # папка уровнем выше
    for entry in entries:
        print(entry.name, '->', entry.stat().st_size, 'bytes')


#  *  *  *   Задачи   *  *  *

# 01
"""
Напишите функцию find_lines_len_more_6, 
которая принимает имя файла и находит количество строк, превышающее 6 символов. 
Не забывайте исключать знак переноса на новую строку, стоящий в конце строки.
Функция find_lines_len_more_6 должна возвращать найденное количество строк.
"""

def find_lines_len_more_6(file_name: str) -> int:
    cnt = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for el in file:
            if len(el.strip()) > 6:
                cnt += 1
    return cnt

# Короче
def find_lines_len_more_6(file_name: str) -> int:
    with open(file_name, encoding='utf-8') as file:
        return sum(len(el.strip()) > 6 for el in file)

rez = find_lines_len_more_6('my_file.txt')
print(rez)


# 02
"""
найти сколько уникальных слов используется в файле "lorem.txt", при этом регистр букв не нужно учитывать. 
Это значит, что слова Lorem и loRem являются эквивалентными.
Между словами в файле стоят только пробелы и переносы строк, других разделителей нет.

Например, если перед вами был бы такой текст:
Привет как дела
привет хорошо
то здесь четыре уникальных слова.
"""

def get_unique_words(file_name: str) -> int:
    with open(file_name, 'r', encoding='utf=8') as files:
        # read() - считываем весь файл
        # split() - удаляем пробелы и перенос строк. Получаем содержимое в виде списка
        ls = files.read().lower().split()
        # set(ls) - удаляем дубликаты
        rez = set(ls)
    return len(rez)

print(get_unique_words('lorem.txt'))


# 03
"""
Посчитать сколько раз встретилось каждое слово в файле lorem.txt. 
Создать словарь words, где ключом будет слово, а значением - количество раз появления этого слова в тексте. 

Регистр букв в словах учитывать не нужно. Значения ключа в словаре words записывайте в верхнем регистре
Между словами в файле стоят только пробелы и переносы строк, других разделителей нет.

Например, если перед вами был бы такой текст:
Привет как дела
привет хорошо
то словарь words выглядел бы так:
{'ПРИВЕТ': 2, 'КАК': 1, 'ДЕЛА': 1, 'ХОРОШО': 1}
"""
with open('lorem.txt', 'r', encoding='utf=8') as files:
    d = dict()
    for el in files.read().upper().split():
        if el in d:
            d[el] += 1
        else:
            d.setdefault(el, 1)
    print(d)

# print(get_dict_words('lorem.txt'))

# Короче
with open('lorem.txt', 'r', encoding='utf-8') as files:
    words = tuple(word for row in files for word in row.strip().upper().split())
    words = {el: words.count(el) for el in set(words)}
    print(words)


# words = {'LOREM': 3, 'IPSUM': 4, 'DOLOR': 2, 'SIT': 8, 'AMET': 8, 'CONSECTETUR': 2, 'ADIPISCING': 1, 'ELIT': 5,
# 'CRAS': 5, 'EUISMOD': 2, 'EX': 5, 'A': 6, 'ANTE': 5, 'SOLLICITUDIN': 3, 'GRAVIDA': 3, 'MASSA': 6, 'BIBENDUM': 3,
# 'PELLENTESQUE': 8, 'QUIS': 6, 'MI': 4, 'ULTRICIES': 3, 'PURUS': 3, 'PLACERAT': 3, 'ALIQUAM': 4, 'SAPIEN': 5,
# 'MORBI': 5, 'FRINGILLA': 5, 'VELIT': 3, 'AT': 10, 'LOBORTIS': 1, 'INTERDUM': 4, 'AUGUE': 4, 'FAUCIBUS': 3,
# 'NUNC': 6, 'ET': 6, 'ULLAMCORPER': 5, 'NISL': 2, 'VITAE': 5, 'RISUS': 3, 'FUSCE': 1, 'MAGNA': 4, 'JUSTO': 2,
# 'SUSCIPIT': 3, 'VEL': 6, 'CURSUS': 4, 'NON': 5, 'CONSEQUAT': 4, 'TEMPOR': 6, 'NULLA': 10, 'SED': 7, 'VULPUTATE': 5,
# 'METUS': 3, 'IACULIS': 3, 'EFFICITUR': 5, 'MAURIS': 6, 'SODALES': 3, 'DIAM': 4, 'CONGUE': 6, 'IN': 11, 'TORTOR': 4,
# 'TEMPUS': 3, 'ELEIFEND': 2, 'CURABITUR': 3, 'EU': 6, 'ENIM': 2, 'QUISQUE': 4, 'ERAT': 1, 'VOLUTPAT': 3,
# 'MALESUADA': 3, 'PULVINAR': 4, 'VESTIBULUM': 4, 'POSUERE': 3, 'LEO': 4, 'TURPIS': 3, 'CONVALLIS': 4,
# 'LIBERO': 4, 'SEMPER': 6, 'ELEMENTUM': 4, 'URNA': 3, 'FACILISI': 1, 'NEC': 1, 'NIBH': 5, 'MAECENAS': 4,
# 'LIGULA': 4, 'EGET': 5, 'DICTUM': 1, 'PHASELLUS': 4, 'PHARETRA': 1, 'SAGITTIS': 1, 'QUAM': 5, 'ETIAM': 2,
# 'EROS': 3, 'DONEC': 5, 'FELIS': 5, 'LECTUS': 1, 'VIVAMUS': 1, 'FINIBUS': 2, 'INTEGER': 1, 'PRETIUM': 1,
# 'NAM': 2, 'MOLLIS': 2, 'SCELERISQUE': 2, 'VIVERRA': 1, 'ARCU': 4, 'EST': 4, 'PRAESENT': 2, 'VEHICULA': 2,
# 'ACCUMSAN': 2, 'LAOREET': 3, 'RUTRUM': 4, 'DIGNISSIM': 3, 'AC': 9, 'DUIS': 3, 'LUCTUS': 2, 'HENDRERIT': 2,
# 'TINCIDUNT': 5, 'ID': 2, 'BLANDIT': 3, 'ALIQUET': 3, 'LACUS': 3, 'RHONCUS': 1, 'ODIO': 2, 'MAXIMUS': 1,
# 'COMMODO': 1, 'EGESTAS': 3, 'LACINIA': 3, 'UT': 4, 'MATTIS': 2, 'FACILISIS': 1, 'NISI': 2, 'NEQUE': 1,
# 'PORTTITOR': 1, 'VARIUS': 1, 'ULTRICES': 1, 'TELLUS': 1, 'HABITANT': 1, 'TRISTIQUE': 1, 'SENECTUS': 1,
# 'NETUS': 1, 'FAMES': 1, 'DAPIBUS': 1, 'MOLESTIE': 1, 'NULLAM': 1}


# 04
"""
Найти в файле words.txt все слова, заканчивающиеся на строку ЕЯ, и вывести их на экран. 
При этом нужно:
-    исключить дубли
-    привести все буквы к верхнему регистру
-    расположить слова в выводе в порядке двойной сортировки: 
        сперва отсортировать по возрастанию длины слова, 
        а при одинаковых значениях длины расположить по алфавиту.
"""

with open('words.txt', 'r', encoding='utf=8') as files:
    ls_in = list(set(files.read().upper().split()))
    ls_out = [el for el in ls_in if el[-2:] == 'ЕЯ']
    ls_out.sort(key=lambda w: (len(w), w))

    for world in ls_out:
        print(world)
