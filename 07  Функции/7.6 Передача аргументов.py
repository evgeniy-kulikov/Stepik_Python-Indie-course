# 7.6 Передача аргументов. Сопоставление аргументов по имени и позиции
""""""

"""
в локальной и в глобальной области видимости переменные имеют одинаковые идентификаторы, 
значит они ссылаются на одни и те же объекты.
"""
def f(a, b):
    print(id(a), id(b), 'local')  # 140202535240528 140202535241488 local

c = 20
d = 50
print(id(c), id(d), 'global')  # 140202535240528 140202535241488 global
f(c, d)

"""
Изменение локальных переменных никак не меняет глобальные.
"""
def f(a, b):
    a = 100
    b = 200
    print(id(a), id(b), 'local')  # 139753282997584 139753283000784 local


c = 20
d = 50
print(id(c), id(d), 'global')  # 139753282995024 139753282995984 global
f(c, d)


"""
Но если есть ссылка на изменяемый объект, то можно косвенным образом изменить содержимое
"""


def f(a, b):
    print(id(a), id(b), 'local')  # 140252444166192 140252445851584 local
    a = 100
    b[1] = 'hi'
    print(id(a), id(b), 'local after')  # 140252444551368 140252445851584 local after


c = 'hello'
d = [1, 2, 4, 5]

print(id(c), id(d), 'global')  # 140252444166192 140252445851584 global

f(c, d)
print(c, d, 'global')  # hello [1, 'hi', 4, 5] global

"""
Чтобы избежать возможности изменения списка в вызов функции достаточно передавать копию списка, 
которую можно сделать при помощи полного среза. У вызова этой функции будет следующий вид:
f(c, d[:])
"""


""""""
# Варианты передачи аргументов функции

# 1 - Позиционный
"""
Указать название функции и передать напрямую три значения. 
В таком случае они будут присваиваться в том же порядке, что и стоят
"""


def f(a, b, c):
    print(a, b, c)  # 1 5 7

f(1, 5, 7)


# 2 - По имени
"""
При вызове функции указывается имя переменной и необходимое ей значение.
В таком случае невозможно указать выдуманные имена параметра, 
т.е. вместо имени b, определенного в функции, мы не могли указать другое имя параметра
"""
def f(a, b, c):
    print(a, b, c)  # 5 20 15

f(b=20, c=15, a=5)


# 3-  Комбинированный вариант
"""
совмещает в себе передачу по позиции и по имени.
Важно учитывать то, что сначала указываются позиционные аргументы, а потом именованные. 
"""
def f(a, b, c):
    print(a, b, c)  # 2 20 10

f(2, c=10, b=20)  # Верно
f(2, a=10, b=20)  # Ошибка


# Типы параметров функции
"""
При создании функции можно указать, какие аргументы нужно передавать обязательно, а какие нет. 
Соответственно, функция может быть создана с:
- обязательными параметрами
- необязательными параметрами (параметрами со значением по умолчанию)
"""

# Обязательные параметры
"""
Обязательные параметры - определяют, какие аргументы нужно передать функции обязательно. 
При этом, их нужно передать ровно столько, 
сколько указано параметров функции (нельзя указать большее или меньшее количество)
"""
def add(a, b):
   return a + b

add(2, 8)  # 10

# Необязательные параметры (параметры со значением по умолчанию)
def add(a=2, b=8):
   return a + b

add()  # 10


def add(a, b=8):
   return a + b

add(2)  # 10


# параметры со значением по умолчанию нельзя ставить раньше позиционных
# def add(a=2, b):  # ОШИБКА!!!
#    return a + b


# Изменяемые объекты в качестве значений по умолчанию
"""
Следует запомнить, что лучше не использовать изменяемые объекты в качестве значений по умолчанию. 
Рассмотрим это на примере списка:
"""

def append_to_list(value, my_list):
    my_list.append(value)
    print(my_list)

append_to_list(5, [1])  # [1, 5]
append_to_list(5, [1])  # [1, 5]


# Изменение переменной а
def append_to_list(value, my_list):
    my_list.append(value)
    print(my_list)

a = [1, 2, 3]
append_to_list(4, a)  # [1, 2, 3, 4]
append_to_list(5, a)  # [1, 2, 3, 4, 5]
print(a)  # [1, 2, 3, 4, 5]


# А теперь посмотрим, что будет, если сделать список значением по умолчанию.
def append_to_list(value, my_list = []):
    my_list.append(value)
    print(my_list, id(my_list))

append_to_list(10)  # [10]          1886635067968
append_to_list(25)  # [10, 25]      1886635067968
append_to_list(37)  # [10, 25, 37]  1886635067968

"""
Проблема заключается в том, что в таком случае все значения будут внесены в один список, 
если необходимы разные списки, то нужно сделать следующим образом:
"""
def append_to_list(value, my_list = None):
    if my_list == None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))


append_to_list(10)  # [10]  2015072783936
append_to_list(25)  # [25]  2015072511808
append_to_list(37)  # [37]  2015072917440

append_to_list(10, [1])  # [1, 10] 1907577293376
append_to_list(25, [1])  # [1, 25] 1907577293376
append_to_list(37, [1])  # [1, 37] 1907577021248
append_to_list(55, [5])  # [5, 55] 1907577353344


# Со словарём необходимо действовать похожим образом
def append_to_dict(key, value, my_dict=None):
    if my_dict is None:
        my_dict = {}
    my_dict[key] = value
    print(my_dict, id(my_dict))

append_to_dict(10, 100)  # {10: 100} 3201702454464
append_to_dict(20, 200)  # {20: 200} 3201702454464
append_to_dict(50, 300)  # {50: 300} 3201702453120
append_to_dict(50, 300, {"a": 'abc'})  # {'a': 'abc', 50: 300} 3201702454400



#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Создать функцию replace, которая принимает три параметра:
обязательный строковый параметр text - текст, в котором необходимо выполнить замены;
обязательный строковый параметр old - строка поиска для замены;
необязательный строковый параметр new - значение замены для найденного значения old. 
По умолчанию равен пустой строке.
Функция replace должна возвращать новую строку, в которой все символы old были заменены на new. 
При замене регистр букв должен учитываться

Output:
replace('Нет', 'т') => 'Не'
replace('Bella Ciao', 'a') => 'Bell Cio'
replace('nobody; i myself farewell analysis', 'l', 'z') => 'nobody; i mysezf farewezz anazysis'
replace('commend me to my kind lord meaning', 'M', 'w') => 'commend me to my kind lord meaning'
"""
def replace(text: str, old: str, new='') -> str:
    res = ''
    for el in text:
        if el == old:
            res += new
        else:
            res += el
    return res


# Хорошее решение
def replace(text: str, old: str, new: str = ''):
    text = text.split(old)
    return new.join(text)


# Короче
def replace(text: str, old: str, new: str = ''):
    return text.replace(old, new)


# 02
"""
Создать функцию make_header, которая принимает обязательный параметр - 
строку, которую нужно обернуть в тег заголовка
необязательный числовой параметр - уровень заголовка, по умолчанию принимает значение 1.
Функция make_header должна возвращать переданную строку в обернутый тег заголовка определенного уровня
Output:
make_header('Нет') => '<h1>Нет</h1>'
make_header('Bella Ciao', 4) => '<h4>Bella Ciao</h4>'
make_header('Go little rock star', 6) => '<h6>Go little rock star</h6>'
make_header('Девальвации не будет. Твердо и четко') => '<h1>Девальвации не будет. Твердо и четко</h1>
"""

def make_header(text: str, l = 1) -> str:
    return f'<h{l}>{text}</h{l}>'


# 03
"""
Создать функцию create_matrix, которая принимает
необязательный числовой параметр size - размер квадратной матрицы, 
по умолчанию принимает значение 3;
необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше главной диагонали. 
По умолчанию равен 0;
необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся ниже главной диагонали. 
По умолчанию равен 0;
Функция create_matrix должна возвращать квадратную матрицу размером size х size, 
на диагонали которой располагаются числа от 1 до size. 
Все остальные элементы заполнены согласно параметрам up_fill и down_fill.

Output:
create_matrix() => [[1, 0, 0], 
                    [0, 2, 0], 
                    [0, 0, 3]]

create_matrix(4) => [[1, 0, 0, 0],
                     [0, 2, 0, 0],
                     [0, 0, 3, 0],
                     [0, 0, 0, 4]]

create_matrix(up_fill=7) => [[1, 7, 7],
                             [0, 2, 7],
                             [0, 0, 3]]

create_matrix(up_fill=7, down_fill=9) => [[1, 7, 7],
                                          [9, 2, 7],
                                          [9, 9, 3]]

create_matrix(size=4, up_fill=7, down_fill=9) => [[1, 7, 7, 7],
                                                  [9, 2, 7, 7],
                                                  [9, 9, 3, 7],
                                                  [9, 9, 9, 4]]
"""


def create_matrix(size=3, up_fill=0, down_fill=0):
    matrix = [[0] * size for _ in range(size)]

    for row in range(size):
        for col in range(size):
            if row > col:
                matrix[row][col] = down_fill
            elif row == col:
                matrix[row][col] = row + 1
            else:
                matrix[row][col] = up_fill

    return matrix


# for el in create_matrix(down_fill=9, up_fill=7, size=4):
#     print(el)


# Без создания начальной матрицы, заполненной нулями.
def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    """Создание квадратной матрицы"""
    matrix = []
    for row in range(size):
        line = []
        for col in range(size):
            if row == col:
                line.append(row + 1)
            elif row < col:
                line.append(up_fill)
            else:
                line.append(down_fill)
        matrix.append(line)
    return matrix

# for el in create_matrix(down_fill=9, up_fill=7, size=4):
#     print(el)


# Решение как выше, но через генератор списков.
def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    matrix = [[row + 1 if row == col else up_fill if row < col else down_fill for col in range(size)]
              for row in range(size)]
    return matrix

# for el in create_matrix(down_fill=9, up_fill=7, size=4):
#     print(el)
