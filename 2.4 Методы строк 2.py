# 2.4 Методы строк 2
""""""
"""
Метод split()
Метод .split  имеет следующий шаблон вызова:
S.split(sep=None, maxsplit=-1)
Метод .split выполняет разбиение исходной строки S на подстроки по разделителю sep 
и возвращает их в виде списка. 
По умолчанию разделитель  "sep"  равен пробелу.
Если параметр "sep" не указан, то последовательные пробелы объединяются вместе 
и вообще исключаются из разбиений. 
А если строка состоит только из пробелов или является пустой, 
то результатом разделения по пробелу будет пустой список
Также можно передать вторым параметром "maxsplit" - 
какое максимальное количество разбиений вы хотите выполнить

w='ivanov ivan ivanovich'
print(w.split())                    ['ivanov', 'ivan', 'ivanovich']
print(len(w.split()))               3
print('a b C d e'.split())          ['a', 'b', 'C', 'd', 'e']
print('1, 2, 3, 4, 5'.split(', '))      ['1', '2', '3', '4', '5']
print('a->b->C->->d->e'.split('->'))    ['a', 'b', 'C', '', 'd', 'e']
print('1      4      5'.split())        ['1', '4', '5']
print('   a  b   c   '.split())         ['a', 'b', 'c']
print('    '.split())                   []
print('wwwww'.split('w'))               ['', '', '', '', '', '']





Метод join()
Метод .join является противоположностью метода .split. 
При помощи него вы можете разбитую строку вновь собрать в одно целое.
Метод .join  имеет следующий шаблон вызова:
S.join(iterable)  "iterable" - итерабельные объекты: строки, списки и т.д.

s = 'ivanov ivan ivanovich'
print('*'.join(s))          ivanov*ivan*ivanovich

words = ['London', 'is', 'the', 'capital', 'of', 'GB']
print(','.join(words))      London,is,the,capital,of,GB



Метод startswith
Метод .startswith  имеет следующий шаблон вызова:
S.startswith(prefix[, start[, end]])
Данный метод возвращает True 
если строка S начинается с последовательности символов prefix (префикса) 
и False в противном случае.  
При передаче параметра "start" проверка начнется именно с этой позиции. 
Если передать значение  "end", проверка закончится в этой позиции.
s = 'Мила Кунис'
print(s.startswith('Мила'))     True
print(s.startswith('Бред'))     False
print(s.startswith('Мила', 1))      False
print(s.startswith('ила', 1))       True
print(s.startswith('ил', 1, 2))     False
print(s.startswith('ил', 1, 3))     True


Метод endswith
Метод endswith() имеет следующий шаблон вызова:
S.endswith(prefix[, start[, end]])
Данный метод возвращает True 
если строка S заканчивается последовательностью символов prefix (префикса) 
и False в противном случае.  
При передаче параметра "start" проверка начнется именно с этой позиции. 
Если передать значение  "end", проверка закончится в этой позиции.

s = 'Мила Кунис'
print(s.endswith('Кунис'))          True
print(s.endswith('Бред'))           False
print(s.endswith('нис', 10))        False
print(s.endswith('нис', 7))         True
print(s.endswith('нис', -3))        True
print(s.endswith('ис', 8, 10))      True

*   *   *   *   *   *   *   *   Группа методов is   *   *   *   *   *   *   *   *   *   *   *   

Эти методы объединяет одно: они выполняют проверку и результат будет либо  True, либо False

Метод .islower  имеет следующий шаблон вызова:
S.islower()
Данный метод возвращает True , если строка S не пустая 
и состоит только из алфавитных строчных(нижний регистр) букв. 
Если в строке имеется хотя бы одна заглавная буква, будет возвращено False. 
Все символы цифр или знак пунктуации игнорируются в проверках.


Метод isupper
Метод .isupper  имеет следующий шаблон вызова:
S.isupper()
Данный метод возвращает True , если строка S не пустая 
и состоит только из алфавитных заглавных(верхний регистр) букв. 
Если в строке имеется хотя бы одна строчная буква, будет возвращено False. 
Все символы цифр или знак пунктуации игнорируются в проверках.


Метод isdigit
Метод .isdigit  имеет следующий шаблон вызова:
S.isdigit()
Данный метод возвращает True , если строка S не пустая 
и состоит только из десятичных цифр и символов, 
которые так же относятся к цифрам. 
В случае, если встретится другой символ, вернется False


Метод isalpha
Метод .isalpha  имеет следующий шаблон вызова:
S.isalpha()
Данный метод возвращает True , если строка S не пустая и состоит только из букв.


Метод isalnum
Метод .isalnum  имеет следующий шаблон вызова:
S.isalnum()
Данный метод возвращает True , если строка S не пустая 
и состоит только из букв и цифр. 
Если в строке имеется хотя бы один не буквенный 
и не числовой символ, то будет возвращено False:


Метод istitle
Метод .istitle  имеет следующий шаблон вызова:
S.istitle()
Данный метод возвращает True , 
если строка S не пустая и является строкой заголовков: 
каждое новое слово начинается с заглавной буквы


Метод ljust
Метод .ljust  имеет следующий шаблон вызова:
S.ljust(width[, fillchar])
Метод  .ljust принимает один обязательный параметр width - ширину строки 
и один необязательный параметр fillchar - знак заполнителя (по умолчанию пробел). 
Возвращает новую строку, в которой исходная строка S 
дополнена справа символами fillchar до указанной длины width. 
Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений:


Метод rjust
Метод .rjust  имеет следующий шаблон вызова:
S.rjust(width[, fillchar])
Метод .rjust принимает один обязательный параметр width - ширину строки 
и один необязательный параметр fillchar - знак заполнителя (по умолчанию пробел). 
Возвращает новую строку, в которой исходная строка S 
дополнена слева символами fillchar до указанной длины width. 
Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений:


Метод center
Метод .center  имеет следующий шаблон вызова:
S.center(width[, fillchar])
Метод .center принимает один обязательный параметр width - ширину строки 
и один необязательный параметр fillchar - знак заполнителя (по умолчанию пробел). 
Возвращает новую строку длины width, в которой исходная строка S находится в центре, 
а справа и слева от нее находятся символы fillchar . 
Если параметр width меньше длины строки, 
то будет возвращена исходная строка без изменений. 
d = 'qwerty'
print(d.center(10))         "  qwerty  "
print(d.center(12, '!'))    !!!qwerty!!!
print(d.center(13, '?'))    ????qwerty???
print(d.center(5, '!'))     qwerty



Метод zfill
Метод .zfill  имеет следующий шаблон вызова:
S.zfill(width)
Метод .zfill возвращает новую строку, 
в которой исходная строка S дополнена нулями слева так, 
чтобы длина новой строки стала равна width.
d = '123'
print(d.zfill(5))           00123
print(d.zfill(6))           000123
print(d.zfill(2))           123
print(d.zfill(3))           123
print('0.123'.zfill(6))     00.123
"""



"""
Программа получает на вход фразу. Посчитать из скольких слов состоит данная фраза.
Input:     Hello my friend
Output:    3 
"""
s = input()
cnt = len(s.split())
print(cnt)

"""
Напишите программу, которая проверяет 
начинается ли введенная фраза строкой mam вне зависимости от регистра букв
Вывести True, если введенная строка начинается с mam, 
во всех остальных случаях нужно вывести False
Input:     mAma
Output:    True 
"""
s = input().lower()
rez = s.startswith("mam")
print(rez)


"""
Программа получает на вход две строки, "s" и "postfix". 
Напишите программу, которая проверяет 
заканчивается ли введенная фраза "s" строкой "postfix".
Нужно вывести True, если введенная строка s заканчивается строкой postfix , 
во всех остальных случаях нужно вывести False. Регистр букв нужно учитывать
Input:  Egs and Bakery
        kery
Output: True 
"""
s, postfix = input(), input()
rez = s.endswith(postfix)
print(rez)

"""
Программа получает на вход три строки, "s" , "prefix" и "postfix". 
Напишите программу, которая проверяет, 
чтобы введенная фраза "s" одновременно начиналась со строки "prefix" 
и заканчивалась строкой "postfix" 
Нужно вывести True, если введенная строка s заканчивается строкой "prefix" 
и заканчивается строкой "postfix", 
во всех остальных случаях нужно вывести False. Регистр букв нужно учитывать
Input:  TRanSlate russian to english
        TRa
        lish
Output: True 
"""
s, prefix, postfix = input(), input(), input()
rez = s.startswith(prefix) and s.endswith(postfix)
print(rez)
