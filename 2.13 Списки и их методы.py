# 2.13 Списки и их методы
""""""

"""
**********************************************************************
Метод append
**********************************************************************

L.append(x)
Метод .append обязательно принимает одно значение x 
и добавляет его в качестве нового элемента  в конец списка L. 
Следовательно размер списка увеличивается на одно значение. 
Никакого присвоения в переменную, как в случае со строками, здесь не требуется.
a = [34, 23, 12, 28, 9, 15]
print(a)  # [34, 23, 12, 28, 9, 15]
a.append(1)
print(a)  # [34, 23, 12, 28, 9, 15, 1]

Если вы сделаете присвоение в переменную, то потеряете все значения, которые у вас были в списке.
a = [34, 23, 12, 28, 9, 15]
print(a)  # [34, 23, 12, 28, 9, 15]
a = a.append(1)
print(a)  # None

Метод .append принимает только одно значение: 
это может быть строка, число или даже список, но ни в коем случае больше одного элемента.
a = [34, 23, 12, 28, 9, 15]
print(a)
a.append(1, 2 , 3)
print(a) # ОШИБКА!!! TypeError: list.append() takes exactly one argument (3 given)


**********************************************************************
Метод clear
**********************************************************************
Метод .clear не принимает никаких аргументов и делает список L пустым, удаляет все его элементы.
a = [34, 23, 12, 28, 9, 15]
print(a)  # [34, 23, 12, 28, 9, 15]
a.clear()
print(a)  # [] 


**********************************************************************
Метод copy
**********************************************************************
Метод .copy не принимает аргументов, делает копию списка:
создается совершенно новый объект в памяти, он тоже является списком 
и будет состоять из таких же элементов как и оригинальный список, 
но у нового списка будет другой идентификатор.
Копию списка также можно получить через полный срез.
a = [34, 23, 12, 28, 9, 15]
b = a.copy()
print(a)  # [34, 23, 12, 28, 9, 15]
print(b)  # [34, 23, 12, 28, 9, 15]

a[0] = 3
print(a)  # [3, 23, 12, 28, 9, 15]
print(b)  # [34, 23, 12, 28, 9, 15]

Метод .copy делает поверхностную копию, это значит он не делает копию вложенных списков, если они есть. 
При поверхностном копировании не создаются копии у вложенных объектов, 
поэтому изменения в одной переменной будут влиять и на другие.
a = [34, 23, [12, 28, 9], 15]
b = a.copy()
print(a)  # [34, 23, [12, 28, 9], 15]
print(b)  # [34, 23, [12, 28, 9], 15]

a[0] = 3
a[2][1] = 100
print(a)  # [3, 23, [12, 100, 9], 15]
print(b)  # [34, 23, [12, 100, 9], 15]
Если вы хотите выполнить полную копию, включая все вложенные списки,  вам необходимо делать глубокую копию.


**********************************************************************
Метод count
**********************************************************************
Принимает обязательно один аргумент. 
При помощи метода .count можно посчитать сколько раз встретилось в списке переданное значение.
a = [34, 23, 12, 28, 9, 15, 23, 2, 23]
print(f'23 встречается {a.count(23)} раз')  # 23 встречается 3 раз
print(f'12 встречается {a.count(12)} раз')  # 12 встречается 1 раз
print(f'24 встречается {a.count(24)} раз')  # 24 встречается 0 раз


**********************************************************************
Метод extend
**********************************************************************
L.extend(iterable)
Метод .extend принимает обязательно один аргумент - итерабельную последовательность. 
Итерабельня последовательность состоит из нескольких элементов, 
поэтому списки и строки являются такой последовательностью. 
При помощи метода .extend можно добавить сразу все элементы из итерируемой последовательности в конец списка L. 
Значит метод .extend позволяет добавлять много элементов за один раз, вот его отличие от метода .append
a = [34, 23, 12, 28, 9, 15]
print(a)  # [34, 23, 12, 28, 9, 15]
a.extend([23, 12])
print(a)  # [34, 23, 12, 28, 9, 15, 23, 12]
a.extend('hello')
print(a)  # [34, 23, 12, 28, 9, 15, 23, 12, 'h', 'e', 'l', 'l', 'o']
В метод .extend можно передать список или строку, но нельзя передать число. Получите ошибку



**********************************************************************
Метод index
**********************************************************************
L.index(x, [start [, end]])
Метод .index находит переданный элемент x в списке L и возвращает его индекс. 
Если в списке находится несколько элементов,  равных значению x, 
то будет возвращен индекс первого из них. 
Если список не содержит переданный элемент x, будет вызвано исключение ValueError.  
У метода есть необязательные параметры start и end :
*    Если задан индекс start то первое вхождение значения x будет искаться начиная с индекса start.
*    Если заданы индексы start и end, то первое вхождение значения x 
     будет искаться начиная с индекса start и перед индексом end.  
     Индекс start включается, а индекс end не включается

a = [34, 23, 12, 28, 23, 2, 23]
print(a.index(23))          # 1
print(a.index(12))          # 2
print(a.index(23, 1))       # 1
print(a.index(23, 2))       # 4
print(a.index(23, 2, 5))    # 1



**********************************************************************
Метод insert
**********************************************************************
Метод  .insert имеет следующий формат:

L.insert(index, value)
Метод .insert выполняет вставку нового значения в список на определенную позицию. 
Метод .insert должен принимать два значения: 
index  - индекс куда вставляем новое значение и 
value - что нужно ставить, то есть само значение.

a = [34, 23, 12, 28, 23]
a.insert(1, 99)
print(a)  # [34, 99, 23, 12, 28, 23]



**********************************************************************
Метод pop
**********************************************************************
У него следующий формат вызова:

L.pop([index])	
Метод .pop возвращает значение элемента с индексом index, а также удаляет его из списка L. 
По сути метод выполняет изъятие из списка элемента, стоящего на позиции index
Необязательный аргумент - индекс index по умолчанию равен -1. 
Так что по умолчанию эта операция производит действие с последним элементом последовательности. 
Вы можете передать значение индекса для изъятия элемента
Результат метода .pop можно сохранить в переменную или сразу распечатать на экран.
a = [34, 23, 12, 28, 23]

a.pop()
print(a)  # [34, 23, 12, 28]

b = a.pop()
print(b)  # 28
print(a)  # [34, 23, 12]

print(a.pop())  # 12
print(a)  # [34, 23]

print(a.pop(0))  # 34
print(a)  # [23]

Метод .pop вызывает IndexError, когда передать несуществующий индекс или попытаться извлечь элемент из пустого списка.



**********************************************************************
Метод remove
**********************************************************************
Метод .remove имеет следующий формат:

L.remove(x)
Слово remove переводится как «удалить», но этот метод, в отличие от метода .pop, удаляет по значению. 
Вы должны обязательно передать одно значение x. 
Метод .remove производит удаление первого элемента, значение которого равно x из списка L. 
Длина списка уменьшается на единицу, элементы, стоящие справа от удаленного, смещаются влево на одну позицию.
Если в списке L есть несколько элементов равных значению x, удалиться только первый найденный слева элемент. 
За один вызов метода удаляется один элемент, если нужно удалить несколько элементов, 
нужно несколько раз вызвать метод  .remove
a = [34, 23, 12, 28, 23, 34]
a.remove(34)
print(a)  # [23, 12, 28, 23, 34]
a.remove(34)
print(a)  # [23, 12, 28, 23]

Метод .remove вызывает ValueError, когда значение x не найдено в списке L



**********************************************************************
Метод reverse
**********************************************************************
Метод .reverse имеет следующий формат:

L.reverse()
Метод .reverse  не требует никаких аргументов и выполняет разворот списка - 
располагает элементы в противоположном порядке. 
При повторном вызове список вернётся в изначальное положение.
a = [34, 23, 12, 28, 23]
a.reverse()
print(a)  # [23, 28, 12, 23, 34]
a.reverse()
print(a)  # [34, 23, 12, 28, 23]



**********************************************************************
Метод sort
**********************************************************************
Cамый, наверное, популярный метод списков - это .sort. Он выполняет сортировку. Имеет следующий формат:
L.sort(key=None, reverse=False)
Если не передать никаких аргументов, то по умолчанию сортировка будет выполнена по возрастанию. 
После этого можете вызвать метод .reverse. Список отсортируется по убыванию. 
Если вы сразу хотите его отсортировать по убыванию, 
то вы можете вызвать метод .sort и в нём внутри скобок дополнительно прописать reverse=True.

a = [34, 23, 12, 28, 23]
a.sort()
print(a)  # [12, 23, 23, 28, 34]
a.reverse()
print(a)  # [34, 28, 23, 23, 12]

b = [34, 23, 12, 28, 23]
b.sort(reverse=True)
print(b)  # [34, 28, 23, 23, 12]
"""

# ******************   TASKS   ****************************
"""
Метод pop
В вашем распоряжении список numbers. 
Ваша задача выполнить действия из списка строго в том же порядке, а именно:
удалить элемент, стоящий на последней позиции;
удалить элемент, стоящий на 0-й позиции;
удалить элемент, стоящий на 12-й позиции;
удалить элемент, стоящий на 7-й позиции;
В качестве ответа необходимо вывести на первой строке измененный список numbers, 
а на второй - сумму значений удаленных элементов
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# pop_el = [numbers.pop(), numbers.pop(0), numbers.pop(12), numbers.pop(7)]
pop_el = [numbers.pop(el) for el in [-1, 0, 12, 7]]
print(numbers)
print(sum(pop_el))
# [181, -139, 448, -20, -917, 32, 422, 198, 284, 472, -986, -989]
# -2044

"""
В вашем распоряжении список numbers.
Ваша задача удалить из этого списка числа 3, 5, 7 и 9
"""
numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3,
           -986, -964, -989, 29]
[numbers.remove(el) for el in [3, 5, 7, 9]]
print(numbers)


"""
В вашем распоряжении список numbers. Ваша задача отсортировать список numbers в порядке убывания 
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.sort(reverse=True)
print(numbers)

"""
Программа получает на вход список из целых чисел. 
Ваша задача преобразовать его таким образом, чтобы элементы расположились в обратном порядке. 
Input:  8 11 43 54 43
Output: [43, 54, 43, 11, 8]
"""
lst = list(map(int, input().split()))
lst.reverse()
print(lst)

"""
Программа получает на вход список из целых чисел. 
Подсчитайте сколько раз в нем присутствует число 999
"""
lst = list(map(int, input().split()))
rez = lst.count(999)
print(rez)


"""
В вашем распоряжении список numbers. 
Ваша задача скопировать все содержимое списка numbers в новую переменную copy_numbers
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
copy_numbers = numbers.copy()
print(copy_numbers)

"""
Вводится два слова через пробел. Ваша задача преобразовать данную фразу таким образом, 
чтобы все буквы стали заглавными и между буквами в каждом слове появились дефисы.
Input:  Бросай курить
Output: Б-Р-О-С-А-Й К-У-Р-И-Т-Ь
"""
ls_in = input().upper()
ls_out = ['-'.join(el) for el in ls_in.split()]
print(*ls_out)

# Варианты 1
ls_in = input().upper().split()
print("-".join(ls_in[0]), "-".join(ls_in[1]))

# Варианты 2
ls_in = input().upper()
ls_out = '-'.join(ls_in).replace('- -',' ')
print(ls_out)

# Варианты 3
ls_in=input().upper().split()
b=ls_in[0].replace("","-")
c=ls_in[1].replace("","-")
print(b[1:-1], c[1:-1])


"""
Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека
Вам необходимо вывести фамилию и инициалы, как в примерах ниже:
Input:  Марина Денисовна Климова
Output: Климова М.Д.
"""
ls_in = input()
ls_out = ls_in.split()
print(f'{ls_out[2]} {ls_out[0][:1]}.{ls_out[1][:1]}.')

"""
Напишите программу, которая выводит слова введённой строки 
(части, разделённые символами пустого пространства) в столбик. 
Нужно обойтись только методами split и join у строк, 
в программе должен быть всего один вызов print.
Input:  Буря мглою небо кроет
Output: Буря
        мглою
        небо
        кроет
"""
ls_in = input()
ls_out = ls_in.split()
[print(el) for el in ls_out]

# Варианты 1
ls_in = input().split()
print(*ls_in, sep='\n')

# Варианты 2
ls_in = input().split()
ls_out = '\n'.join(ls_in)
print(ls_out)
