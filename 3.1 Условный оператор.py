# 3.1 Условный оператор
""""""
"""
Оператор if

В простейшем варианте использование оператора if выглядит так:

if условие:
    блок команд 1
блок команд 2


2. Конструкция if-else
В состав оператора if может входить необязательный оператор else. 
Схема использования выглядит следующим образом:

if условие:
    блок команд 1
else:
    блок команд 2
блок команд 3
"""


"""
Моржевый оператор
начиная с версии python 3.8, появился Моржовый (walrus) оператор. 
Он дает возможность решить сразу две задачи: 
присвоить значение переменной и сразу получить это значение. 

print(see_walrus := 'Look at my walrus!')
# Look at my walrus!


if number := int(input('Введите число: ')) == 100:
  print('Соточка')
else:
  print('Не Соточка'
"""


# ******************   TASKS   ****************************

"""
На вход программе поступает одно слово.
Если это строка «Python», программа выводит ДА, 
в противном случае программа выводит НЕТ
Input:  Java
Output: НЕТ
"""
s = input()
if s == "Python":
    print("ДА")
else:
    print("НЕТ")

# Вариант 1
print('НДЕАТ'[input() == 'Python'::2])

# Вариант 2
print(['НЕТ', 'ДА'][input() == 'Python'])


"""
В РФ граждане платят подоходный налог в размере 13%.
Представьте теперь, что люди с доходом меньше 20000 рублей освобождены от уплаты налога. 
Напишите программу, которая получает на вход значение дохода и выводит на экран сумму, 
оставшуюся после уплаты налога в 13%. 
Если у человека зарплата меньше 20000р налог не удерживается.
Input:  30000
Output: 26100.0
"""
salary = int(input())
if salary > 20000:
    print(salary * 0.87)
else:
    print(salary)

# Вариант 1
salary = int(input())
print(salary if salary < 20000 else salary * 0.87)

# Вариант 2
salary = int(input())
print(salary * (0.87 + 0.13 * (salary < 20000)))


"""
Вводятся два целых числа, каждое в отдельной строке.
Ваша задача вывести наибольшее из данных чисел.
Примечание: используйте только условный оператор, функцией max пользоваться нельзя
Input:  8
        11
Output: 11
"""
a, b = int(input()), int(input())
if a > b:
    print(a)
else:
    print(b)

# Вариант 1
a, b = int(input()), int(input())
print((a, b)[a < b])


"""
Программа получает на вход три натуральных числа A, B и C через пробел. 
Вам необходимо вывести YES в том случае, если A + B = C и вывести NO в противном случае.
Input:  4 5 9
Output: YES
"""
a, b, c = map(int, input().split())
if a + b == c:
    print("YES")
else:
    print("NO")


# Вариант 1
a, b, c = map(int, input().split())
print('YES' if a + b == c else 'NO')

# Вариант 2
a, b, c = map(int, input().split())
print('NO' if a + b - c else 'YES')


"""
Программа получает на вход список из целых чисел, при этом гарантируется, 
что числа в списке повторяться не будут.
Ваша задача удалить из этого списка числа 3, 5, 7 и 9. 
Обратите внимание, что каждое из чисел 3, 5, 7 и 9. 
необязательно должно присутствовать в введенном списке.
Input:  1 2 3 4 5 6 7 8 9 10
Output: [1, 2, 4, 6, 8, 10]
"""
# 4 3 65 32 43 5 2
str_num = list(map(int, input().split()))
for el in str_num:
    if el in [3, 5, 7, 9]:
        str_num.remove(el)
print(str_num)

# Вариант 1
str_num = list(map(int, input().split()))
[str_num.remove(el) for el in [3, 5, 7, 9] if el in str_num]
print(str_num)



"""
На момент написания текста из РФ можно было вывозить не более 10000$. 
Пусть, сумму выше 10000 долларов таможня забирает себе и вам останется только 10000$.

Напишем такую программу, которая будет принимать целое положительное число - сумма в долларах. 
Если она не превышает 10000$, то выводим текст Сумма <значение> не превышает лимит, проходите
Если сумма превышает 10000$ выводим текст Ого! <значение>! Куда вам столько? Мы заберем <разница>
Нужно использовать Моржевый оператор

Input:  500
Output: Сумма 500 не превышает лимит, проходите

Input:  12000
Output: Ого! 12000! Куда вам столько? Мы заберем 2000
"""

if (number := int(input())) <= 10000:
  print(f'Сумма {number} не превышает лимит, проходите')
else:
  print(f'Ого! {number}! Куда вам столько? Мы заберем {abs(10000 - number)}')


"""
На вход вашей программе поступает фраза, 
если в ней присутствует слово walrus выводим текст
Нашли моржа, 
иначе выводим 
Никаких моржей тут нет.

Input:  Не потерять бы в серебре еёёёёё однууууууу заветнуууююююю
Output: Никаких моржей тут нет
"""

if "walrus" in (s := input()):
  print("Нашли моржа")
else:
  print("Никаких моржей тут нет")



"""
Программа принимает на вход два слова s и t. 
Если слово t является словом s, записанным наоборот, выведите YES, иначе выведите NO.
Слова состоят из маленьких латинских букв. Входные данные не содержат лишних пробелов. 
Слова непустые, и их длины не превосходят 100 символов.

Input:  avtor
        rotva
Output: YES
"""
if (s := input())[::-1] == (t := input()):
  print("YES")
else:
  print("NO")

# Вариант 1
print("YES" if (a := input()) == (s := ''.join(reversed(input()))) else "NO")


"""
Требуется написать программу, определяющую, является ли четырехзначное натуральное число N палиндромом, 
т.е. числом, которое одинаково читается слева направо и справа налево.
Программа получает на вход целое положительное четырехзначное число N  и должна вывести YES,  
если число N является палиндромом, и NO - если не палиндром.

Input:  4554
Output: YES
"""
if (s := input()) == (s[::-1]):
  print("YES")
else:
  print("NO")

"""
Даны три натуральных числа a, b, c записанные в отдельных строках. 
Ваша задача определить, существует ли треугольник с такими сторонами. 
Для этого вспоминаем теорему о существовании треугольника. 
Она утверждает, что треугольник существует, если сумма любых двух сторон больше оставшейся третьей.
Выведите строку YES, если условие теоремы выполняется, иначе выведите строку NO.

Input:  3
        4
        5
Output: YES
"""
a, b, c = int(input()), int(input()), int(input())
if (a + b) > c and (a + c) > b and (b + c) > a:
    print("YES")
else:
    print("NO")

# Вариант 1
s = [(int(input())) for _ in range(3)]
s.sort()
if s[2] < s[0] + s[1]:
    print('YES')
else:
    print('NO')

# Вариант 2
a, b, c = int(input()), int(input()), int(input())
if max(a, b, c) < ((a + b + c) - max(a, b, c)):
    print('YES')
else:
    print('NO')


"""
Счастливым билетом называют такой билет с шестизначным номером (иногда и с незначащими нулями), 
где сумма первых трех цифр равна сумме последних трех. 
Программа получает на вход одно целое число N и должна вывести «YES», 
если билет с номером N счастливый и «NO» в противном случае.
Примечание: Если разрядов не хватает (например 345), то нужно добавлять незначащие нули: 000345
Input:  385916
Output: YES
"""
# num = list(map(int, ''.join(input().zfill(6))))
num = [int(i) for i in input().zfill(6)]
if sum(num[:3]) == sum(num[-3:]):
    print('YES')
else:
    print('NO')


"""
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и 
выводит сообщение о том, являются ли эти клетки одного цвета. 
Столбцы на шахматной доске обозначаются английскими строчными буквами.
Пояснение: если принять соответствие  abcdefgh  >>> 12345678, то 
черные клетки имеют четную сумму координат, а белые - нечетную
Input:  a1
        b2
Output: YES
"""
cell_1, cell_2  = input(), input()
s = "_abcdefgh"
letter_1 = cell_1[0]
letter_2 = cell_2[0]
col_1 = s.find(letter_1)
col_2 = s.find(letter_2)
row_1 = int(cell_1[1])
row_2 = int(cell_2[1])

if (col_1 + row_1) % 2 == (col_2 + row_2) % 2:
    print('YES')
else:
    print('NO')


cell_1, cell_2 = input(), input()
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = ['1', '2', '3', '4', '5', '6', '7', '8']
if (col.index(cell_1[0]) + row.index(cell_1[1])) % 2 == (col.index(cell_2[0]) + row.index(cell_2[1])) % 2:
    print('YES')
else:
    print('NO')
