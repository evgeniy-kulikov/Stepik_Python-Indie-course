#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.
"""

def file_read(file_name: str) -> None:
    with open(file_name, mode='r', encoding='utf-8') as my_file:
        print(my_file.read())

def file_read(file_name: str) -> None:
    my_file = open(file_name, mode='r', encoding='utf-8')
    print(my_file.read())
    my_file.close()


file_read('my_file.txt')


# 02
"""
Напишите функцию file_n_lines, которая печатает первые n-строка файла. 
Функция file_n_lines принимает на вход название файла и количество строк для прочтения.
"""

def file_n_lines(file_name: str, n: int) -> None:
    my_file = open(file_name, mode='r', encoding='utf-8')
    row = my_file.readlines()
    for el in range(n):
        print(row[el][0:-1])
    my_file.close()


# 03
"""
Напишите функцию file_n_lines, которая печатает первые n-строка файла. 
Функция file_n_lines принимает на вход название файла и количество строк для прочтения.
"""
def file_n_lines(file_name: str, n: int) -> None:
    with open(file_name, encoding='utf-8') as row:
        for _ in range(n):
            print(row.readline().strip())


file_n_lines('my_file.txt', 3)



# 04
"""
Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.
Функция должна создать файл с название "range_<number>.txt" 
и наполнить его целыми числами от 1 до n включительно, 
причем каждое число записывается  в отдельной строке
"""
def create_file_with_numbers(n: int) -> None:
    with open(f'range_{n}.txt', mode='a') as my_file:
        for el in range(1, n + 1):
            my_file.write(f'{el}\n')

create_file_with_numbers(5)


# Вариант
def create_file_with_numbers(n):
    with open(f'range_{n}.txt', mode='w', encoding='utf-8') as my_file:
        my_file.write('\n'.join(map(str, range(1, n + 1))))

create_file_with_numbers(5)


# 05
"""
Напишите функцию longest_word_in_file, 
которая принимает имя файла и внутри его содержимого находит самое длинное слово 
и возвращает его в качестве ответа. 
В случае,  если есть несколько слов с максимальной длиной, 
нужно вернуть слово, которое встречается последнее в тексте.
При этом слова в тексте отделяются друг от друга пробелами, 
любые другие знаки пунктуации необходимо исключить.
"""
# возможные знаки пунктуации можно получить из модуля string
from string import punctuation

def remove_punctuation(word):
    for pn in punctuation:
        if pn in word:
            word = word.replace(pn, '')
    return word


def longest_word_in_file(file_name) -> None:
    rez = ''
    with open(file_name, mode='r', encoding='utf=8') as txt_file:
        file_in = txt_file.read()
        rows = file_in.split()

    for row in rows:
        clear_word = remove_punctuation(row)
        if len(clear_word) >= len(rez):
            rez = clear_word

    return rez


# longest_word_in_file('my_file.txt')


# 06
"""
В файле numbers.txt записаны натуральные числа. 
Найти:
количество трехзначных чисел;
сумму двухзначных чисел
В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов. 
Сперва количество, потом сумма
"""

with open('numbers.txt', mode='r', encoding='utf=8') as txt_file:
    cnt, sum_num = 0, 0
    file_in = txt_file.read()
    ls = [el for el in file_in.split()]
    for el in ls:
        if len(el) == 3:
            cnt += 1
        elif len(el) == 2:
            sum_num += int(el)
    print(f'{cnt},{sum_num}')  # 9041,46947

