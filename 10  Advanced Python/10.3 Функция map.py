# 10.3 Функция map Python
""""""

"""
class map(object)
   map(func, *iterables) --> map object
 
Функция map используется для применения функции к каждому элементу итерируемого объекта (например, списка или словаря). 
Результатом будет итератор map object.
"""
ls = [-1, 2, -3, 4, -5]
rez = list(map(abs, ls))
print(rez)  # [1, 2, 3, 4, 5]


"""
можно передавать в map:
1 Встроенные функции (только имя функции, без указания круглых скобок и без передачи аргументов)
2 Пользовательские функции (только имя функции, без указания круглых скобок и без передачи аргументов)
3 Методы объектов
"""
a = ['hello', 'hi', 'good morning']
b = list(map(str.upper, a))  # вызываем метод upper у объекта str
print(b)  # ['HELLO', 'HI', 'GOOD MORNING']

"""
4 Анонимные функции. 
Для них мы должны указать, что функция принимает аргументы (минимум один аргумент (например: lambda x:))
"""
list_strings = ['hello', 'hi', 'good morning']
b = list(map(lambda x: x+'!', list_strings))
print(b)  # ['hello!', 'hi!', 'good morning!']


# Использование нескольких последовательностей
"""
class map(object)
   map(func, *iterables) --> map object
   
функция map может принимать произвольное количество последовательностей. 
В таком случае будут браться по порядку элементы стоящие на одинаковых местах из всех коллекций 
и по очереди передаваться на вход функции func. 
Количество параметров функции func должно совпадать с количеством последовательностей.
"""
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
print(list(result))  # [12, 15, 18]
#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Имеется список numbers, состоящий из целых чисел. 
Преобразовать каждый элемент списка numbers в строку и сохранить полученный результат в новый список strings. 
Для преобразования используйте map
В качестве ответа выведите переменную strings
"""
numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150, -458, -372, 450, 141, -626, -168, -383, 389, -184, 609,
           221, 311, 526, 254, -631, -174, -555, -338, 226, 695, -16, 333, 12, -600, -258, -383, -101, 121, 40, 278,
           118, -462, -671, 78, -69, -568, -228, -445, -47, -565]

strings = list(map(str, numbers))
print(strings)


# 02
"""
Имеется список numbers, состоящий из целых чисел. 
Увеличить каждый элемент списка numbers втрое и сохранить полученный результат в новый список increase_3. 
Для преобразования используйте функцию map

В качестве ответа выведите переменную increase_3
"""
numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150, -458, -372, 450, 141, -626, -168, -383, 389, -184, 609,
           221, 311, 526, 254, -631, -174, -555, -338, 226, 695, -16, 333, 12, -600, -258, -383, -101, 121, 40, 278,
           118, -462, -671, 78, -69, -568, -228, -445, -47, -565]

increase_3 = list(map(lambda el: el * 3, numbers))
print(increase_3)


# 03
"""
Напишите программу, которая возводит в квадрат и в куб каждое число из списка numbers 
пользуясь при этом функциями map и lambda.
В результате должно получится два отдельных списка: 
в одном квадраты, в другом кубы. Их необходимо вывести на экран.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = list(map(lambda el: el ** 2, numbers))
numbers_3 = list(map(lambda el: el ** 3, numbers))
print(numbers_2)
print(numbers_3)


# 04
"""
Задачка про RGB (https://stepik.org/lesson/818712/step/9?thread=solutions&unit=822093)
Задание:
https://stepik.org/lesson/372107/step/6?unit=359661
"""
def from_hex_to_rgb(color: str) -> tuple:
    red = color[1:3]
    green = color[3:5]
    blue = color[5:]
    return int(red, 16), int(green, 16), int(blue, 16)


colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
          '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
          '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
          '#7CFC00', '#7FFF00', '#ADFF2F']

for red, green, blue in map(from_hex_to_rgb, colors):
    print(f"Red={red}, Green={green}, Blue={blue}")


# 05
"""
На вход программе поступают английские буквы через пробел в верхнем или маленьком регистре.
Сформировать список кортежей. Каждый элемент кортежа будет состоять из двух значений: 
берется соответствующая буква сперва в верхнем регистре, а затем в нижнем (см. примеры ниже)
Выведите на экран полученный список кортежей.
Input:  M e S s I
Output: [('M', 'm'), ('E', 'e'), ('S', 's'), ('S', 's'), ('I', 'i')]
"""
s_in = input().lower().split()
s_out = list(map(lambda el: (el.upper(), el), s_in))

print(s_out)


# 06
"""
https://stepik.org/lesson/372107/step/8?unit=359661

Input:  [('Monica', 'Waters'), ('Juan', 'Lee'), ('Donna', 'Walker')]
Output: ['Monica Waters', 'Juan Lee', 'Donna Walker']
"""
names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez'),
         ('Shawn', 'Gutierrez'), ('Gary', 'Ross'), ('Melanie', 'Warren'),
         ('Drew', 'May'), ('Jennifer', 'Carroll'), ('Ann', 'Lynn'), ('Ralph', 'Vazquez'),
         ('Brittany', 'Erickson'), ('Mark', 'Montoya'), ('Randall', 'Hicks'),
         ('Tyler', 'Miller'), ('Bryan', 'Brown'), ('Joshua', 'Sawyer'),
         ('Sarah', 'Phillips'), ('Donna', 'Davenport'), ('Rebekah', 'Johnson'),
         ('Andrew', 'Reynolds'), ('April', 'Turner'), ('Amanda', 'Ryan'), ('Jennifer', 'Poole'),
         ('Jonathan', 'Lane'), ('Laura', 'Stone'), ('Sara', 'Brown'), ('Alexander', 'Johnson'),
         ('Emily', 'Phillips'), ('Tyler', 'Smith'), ('Victor', 'Kelly'), ('Audrey', 'Thomas'),
         ('Melissa', 'Green'), ('Bethany', 'Holt'), ('Christopher', 'Kerr'), ('Gabrielle', 'Black'),
         ('Jennifer', 'Wade'), ('Douglas', 'Horton'), ('Steven', 'Welch'),
         ('Terri', 'Thompson'), ('Cassandra', 'Nelson'), ('Andrew', 'Jones'),
         ('James', 'Schultz'), ('Richard', 'Castillo'), ('Shaun', 'Logan'),
         ('Danielle', 'Lane'), ('Mark', 'Anderson'), ('Charles', 'Shaw'),
         ('Derrick', 'Grant'), ('Tracy', 'Pierce'), ('Robert', 'Washington')]

# new_names = list(map(lambda el: str(el[0]) + ' ' + str(el[1]), names))
new_names = list(map(lambda el: f'{str(el[0])} {str(el[1])}', names))
print(new_names)


# 07
"""
https://stepik.org/lesson/372107/step/9?unit=359661
Имеется список словарей persons. На основании списка persons отобрать информацию о номерах телефона 
и сложить их в отдельный список phones. Номера в списке phones должны располагаться в том же порядке, 
в котором расположены их владельцы в списке persons.
"""
persons = [
    {
        'birthday': '1983-10-25',
        'job': 'Field seismologist',
        'name': 'Andrew Hernandez',
        'phone': '680-436-8521x3468'
    },
    {
        'birthday': '1993-10-03',
        'job': 'Pathologist',
        'name': 'Paul Harmon',
        'phone': '602.518.4130'
    },
    {
        'birthday': '2002-06-11',
        'job': 'Designer, multimedia',
        'name': 'Gregory Flores',
        'phone': '691-498-5303x079'
    },
    {
        'birthday': '2006-11-28',
        'job': 'Print production planner',
        'name': 'Jodi Garcia',
        'phone': '(471)195-7189'},
    {
        'birthday': '2019-12-05',
        'job': 'Warehouse manager',
        'name': 'Elizabeth Cannon',
        'phone': '001-098-434-5950x276'
    },
    {
        'birthday': '1984-06-12',
        'job': 'Visual merchandiser',
        'name': 'Troy Lucas',
        'phone': '+1-018-070-2288x18433'
    },
    {
        'birthday': '1993-09-14',
        'job': 'International aid/development worker',
        'name': 'Laurie Sandoval',
        'phone': '2930693269'
    },
    {
        'birthday': '1999-05-25',
        'job': 'Editor, film/video',
        'name': 'Jack Clark',
        'phone': '8643048473'
    },
    {
        'birthday': '1985-09-11',
        'job': 'Magazine journalist',
        'name': 'Kimberly Johnson',
        'phone': '+1-583-428-7663'
    },
    {
        'birthday': '1990-10-07',
        'job': 'Museum/gallery curator',
        'name': 'Austin Liu PhD',
        'phone': '714-879-5250'
    }
]

phones = list(map(lambda el: el.get('phone'), persons))
print(phones)


# 09
"""
https://stepik.org/lesson/372107/step/11?unit=359661
x ** 2 - x * y * w + w ** 4
"""
list_x = [25, 48, 23, 13, -18, -10, -3, 16, 2, -12, 20, -14, 14, 45, 41, 6, 11, 15, 22,
          -14, -11, 41, 15, 48, 47, 41, -8, 1, 4, 1, 40, 27, -11, -2, -14, -15, 35, 4,
          49, 4, 5, 13, 50, 35, -3, 3, 30, -11, 7, 12]

list_y = [-9, 17, 41, 47, -5, -10, -5, 13, 31, -11, 37, 9, 46, 27, -1, 36, 32, 23, -12,
          38, 8, 9, 17, 16, 29, -4, 4, 2, 1, 46, 6, 49, -16, 21, -19, -10, 15, -13, 20,
          13, -18, 21, -17, 21, 10, 5, 38, -1, 18, 22]

list_w = [9, -26, 3, 21, 48, -14, 43, -4, -16, 16, 41, 43, -27, -9, 10, -10, 4, -2, 1,
          7, 30, -29, 11, 17, 31, 31, -26, 38, 38, -17, 35, 17, 35, 10, -25, 42, -30,
          -10, -20, 20, 15, 0, 29, -30, -21, -13, -27, -21, -18, -26]

rez = list(map(lambda x, y, w: x ** 2 - x * y * w + w ** 4, list_x, list_y, list_w))
print(rez)
