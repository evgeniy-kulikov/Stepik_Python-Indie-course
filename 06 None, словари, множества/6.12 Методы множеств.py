# 6.12 Методы множеств
""""""

# Метод .copy() копирует элементы оригинального множества в новое множество.
a = {1, 2, 3}
print(a, id(a))  # {1, 2, 3} 139744643915712
b = a.copy()
print(b, id(b))  # {1, 2, 3} 139744642237824

"""
Методы для удаления элементов из множества
"""
# Метод .clear() очищает все множество от его элементов
a = {1, 2, 3}
a.clear()  # set()


# Метод .remove() позволяет удалить элемент из множества.
# Если указать элемент, который отсутствует в множестве, возникнет ошибка KeyError
a = {1, 2, 3}
a.remove(2)  # {1, 3}


# Метод .discard() позволяет удалить элемент из множества,
# но в отличие от метода remove() не возникнет ошибки при попытке удалить несуществующий элемент
a = {1, 2, 3}
a.discard(5)  # {1, 2, 3}
a.discard(2)  # {1, 3}
print(a)

# Метод .pop()  вернет произвольный элемент из множества, а затем удалит его
a = {1, 2, 3}
b = a.pop()  # b = 1      a = {2, 3}


"""
Методы для добавления элементов в множество
"""
# Метод .add() позволяет добавить новый элемент в множество
# В метод .add() передается только одно значение и оно обязательно должно быть неизменяемым типом данных
a = {1, 2, 3}
a.add(5)  # {1, 2, 3, 5}


# Метод .update() позволяет добавить сразу несколько элементов
set_str = {'a', 'b', 'c'}
set_num = {1, 2, 3}
set_str.update(set_num)  # set_str = {'b', 1, 2, 'a', 'c', 3}


# Метод .union()
"""
Метод .union() позволяет выполнить операцию объединения. 
Метод .union() может принимать произвольное количество любых объектов, 
поддерживающих итерацию по своим элементам. 
Это могут быть списки, кортежи, другое множество и т.д. 
Дублирующие элементы последовательностей игнорируются. 
Результатом вызова метода .union() будет новое множество, или, другими словами, 
новый объект множества. Метод не изменяет значения того множества, у которого метод вызывался
"""
set_str = {'car', 'soup', 'bus'}
set_num = {1, 2, 3}
new_set = set_str.union(set_num)  # {1, 2, 3, 'car', 'soup', 'bus'}

new_set = set_str | set_num  # {1, 2, 3, 'car', 'soup', 'bus'}

my_list = ['a', 'b', 'c']
new_set_2 = set_num.union(my_list)  # {'b', 1, 2, 3, 'a', 'c'}


# Метод intersection
"""
Метод .intersection() позволяет выполнить операцию пересечения. 
Метод .intersection() может принимать произвольное количество любых объектов, 
поддерживающих итерацию по своим элементам. 
Результатом вызова метода .intersection() будет новое множество куда войдут только те элементы, 
которые встречаются во всех коллекциях. Старые объекты никак не изменятся в процессе работы этого метода
"""
set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup'}
new_set = set_a.intersection(set_b)  # {'soup', 'bus'}

new_set = set_a & set_b  # {'soup', 'bus'}

new_set_2 = set_a.intersection(('hello', 'car'), ['car', 'soup'])  # {'car'}


# Метод .intersection_update()
"""
Метод .intersection_update() позволяет выполнить операцию пересечения. 
Метод .intersection_update() может принимать произвольное количество любых объектов, 
поддерживающих итерацию по своим элементам. 
Результатом вызова метода .intersection_update() будет не создание нового множества, 
а изменение существующего. Присваивать ничего не нужно, 
автоматически после вызова изменится множество, у которого данный метод был вызван. 
При попытке сохранить результат вызова этого метода  в переменную, в ней сохранится значение None
"""
set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup'}
set_a.intersection_update(set_b)
print(set_a)  # {'bus', 'soup'}


# Метод .difference()
"""
Метод .difference() позволяет выполнить операцию «разность множеств». 
Метод .difference() может принимать произвольное количество любых объектов, 
поддерживающих итерацию по своим элементам. 
Результатом вызова метода .difference() будет новое множество 
куда войдут только элементы из операции разности множеств. 
Старые объекты никак не изменятся в процессе работы этого метода
"""
set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup'}

res_1 = set_a.difference(set_b)  # {'car'}
res_2 = set_b.difference(set_a)  # set()

res_1 = set_a - set_b  # {'car'}
res_2 = set_b - set_a  # set()


# Метод difference_update
"""
Метод .difference_update() позволяет выполнить операцию «разность множеств». 
Метод .difference_update() может принимать произвольное количество любых объектов, 
поддерживающих итерацию по своим элементам. 
Результатом вызова метода .difference_update() будет не создание нового множества, 
а изменение существующего. Присваивать ничего не нужно, автоматически после вызова изменится множество, 
у которого данный метод был вызван. 
При попытке сохранить результат вызова этого метода  в переменную, в ней сохранится значение None
"""
set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup', 'bro', 'lol'}

set_a.difference_update(set_b)
print(set_a)  # {'car'}

set_b.difference_update(set_a)
print(set_b)  # {'bus', 'soup', 'bro', 'lol'}


# Метод symmetric_difference
"""
Метод .symmetric_difference() позволяет выполнить операцию «симметрическая разность». 
Метод .symmetric_difference() может принимать только один объект, 
поддерживающих итерацию по своим элементам. 
Результатом вызова метода .symmetric_difference() будет новое множество 
куда войдут только элементы из операции разности множеств. 
Старые объекты никак не изменятся в процессе работы этого метода
"""
set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup'}

res = set_a.symmetric_difference(set_b)

print(set_a)  # {'car', 'soup', 'bus'}
print(set_b)  # {'soup', 'bus'}
print(res)  # {'car'}


# Метод symmetric_difference_update
"""
Метод .symmetric_difference_update() позволяет выполнить операцию «симметрическая разность». 
Метод .symmetric_difference_update() может принимать произвольное количество любых объектов, 
поддерживающих итерацию по своим элементам. 
Результатом вызова метода .symmetric_difference_update() будет не создание нового множества, а изменение существующего. 
Присваивать ничего не нужно, автоматически после вызова изменится множество, у которого данный метод был вызван. 
При попытке сохранить результат вызова этого метода  в переменную, в ней сохранится значение None
"""
set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup', 'bro', 'lol'}

set_a.symmetric_difference_update(set_b)
print(set_a)  # {'lol', 'car', 'bro'}

set_b.symmetric_difference_update(set_a)
print(set_b)  # {'soup', 'bus', 'car'}



#
#  *  *  *   Задачи   *  *  *
#


# 1
my_set = {'government', 'control', 'winter', 'few', 'generation',
          'service', 'national', 'tradition', 'government'}
a = {'concert', 'brown', 'jacket', 'value'}
my_set.update(a)

# Вариант
my_set.update(['concert', 'brown', 'jacket', 'value'])
my_set |= {'concert', 'brown', 'jacket', 'value'}

# 2
# https://stepik.org/lesson/296966/step/4?unit=278694
my_set.discard('government')
my_set.discard('national')
my_set.discard('tease')

# Вариант 1
my_set -= {'government', 'national', 'tease'}
# Вариант 2
a = {'government', 'national', 'tease'}
my_set = my_set ^ a
my_set.difference_update(a)


# 3
# https://stepik.org/lesson/296966/step/5?unit=278694
my_set.discard('noble')
my_set.discard('offend')
my_set.discard('error')
my_set.discard('eagle')
my_set.discard('sail')

# Вариант 1
my_set.difference_update(('noble', 'offend', 'error', 'eagle', 'sail'))
my_set -= {'noble', 'offend', 'error','eagle', 'sail'}


# 4
"""
Программе будут поступать на вход N списков, содержащих целые числа
Определить сколько всего встречалось различных чисел во всех этих списках
Input:  2
        1 2 3 2 1 4
        1 1 2 2 2
Output: 4
"""
n = int(input())
a = set()

for el in range(n):
    a.update(set(list(map(int, input().split()))))
print(len(a))

# Вариант
a = {el for _ in range(int(input())) for el in list(map(int, input().split()))}
print(len(a))


# 5
"""
Программа получает на вход последовательность фраз, указанных через запятую.
Для каждой фразы выведите слово ДА (в отдельной строке), 
если эта фраза ранее встречалось в последовательности или НЕТ, если не встречалось.
Символы во фразах нужно рассматривать без учета регистра,
Input:  Hello world,hi dude,hello world,qwerty
Output: НЕТ
        НЕТ
        ДА
        НЕТ
"""
# ls = ['hello world', 'hi dude', 'hello world', 'qwerty']
ls = input().lower().split(',')
res = set()
for el in ls:
    if el not in res:
        res.add(el)
        print('НЕТ')
    else:
        print('ДА')
print(res)

# Вариант через списки
res = []
for el in ls:
    if el not in res:
        res += [el]
        print('НЕТ')
    else:
        print('ДА')


# 6
"""
Даны два списка чисел.
Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
Input:  1 3 2 5
        4 3 2 6
Output: 2 3
"""
ls1, ls2 = (map(int, input().split()) for _ in range(2))
ls3 = set(ls1).intersection(set(ls2))
sorted(list(ls3))

print(*ls3)

# Вариант
ls1 = set(map(int, input().split()))
ls2 = set(map(int, input().split()))
ls3 = list(ls1 & ls2)
print(*sorted(ls3))


# 7
"""
Даны два списка чисел. Выведите все числа в порядке возрастания, 
которые входят в первый список, но при этом отсутствуют во втором. 
Input:  1 3 2 5
        4 3 2 6
Output: 1 5
"""
num1, num2 = (list(map(int, input().split())) for _ in range(2))
new_set = set(num1).difference(set(num2))
sorted(list(new_set))
print(*new_set)

# Вариант
ls1 = set(map(int, input().split()))
ls2 = set(map(int, input().split()))
ls3 = list(ls1 - ls2)
print(*sorted(ls3))


# 8
"""
Напишите программу, которая выводит все цифры, 
встречающиеся в символьной строке (может содержать цифры, пробелы и латинские буквы) больше одного раза.
Программа должна вывести в одну строчку в порядке возрастания все цифры, 
встречающиеся во входной строке больше одного раза. 
Если таких цифр нет, нужно вывести слово 'NO'.
Input:  abc12cd34ef35
Output: 3
"""
# ls = [1, 2, 3, 4, 3, 5]
ls = [int(el) for el in input() if el.isdigit()]
res = set([el for el in ls if ls.count(el) > 1])
sorted(list(res))

print(*sorted(res) if res else ['NO'])

# if len(res):
#     print(*res)
# else:
#     print('NO')


# 9
"""
Напишите программу, которая удаляет из строки все повторяющиеся символы, при этом регистр букв необходимо учитывать.
Input:  hello_world!
Output: helo_wrd!
"""
st_in = input()
st_set = set(st_in)

for el in st_in:
    if el in st_set:
        print(el, end='')
        st_set.remove(el)


# Без множества
st_in = input()
st_set = ''
for el in st_in:
    if el not in st_set:
        st_set += el
print(st_set)
