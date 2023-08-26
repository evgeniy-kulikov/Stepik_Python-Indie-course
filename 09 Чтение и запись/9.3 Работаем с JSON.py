# 9.3 Работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл
""""""


"""     Десериализация      """
# Из формата JSON в объект Python (процесс десериализации)
# load(f)  - десериализует JSON из f
# loads(s)  - десериализует s (экземпляр str, содержащий документ JSON) в объект Python
"""
Чтобы преобразовать в питоновский словарь необходимо импортировать встроенный модуль json. 
В нем имеется функция loads,  в которую необходимо передать строку формата JSON и она выполнит десериализацию, 
если это возможно. Результатом работы функции loads будет словарь. 
"""

import json
from pprint import pprint

str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod"
            }
        ]
    }
}
"""

data = json.loads(str_json)
pprint(type(data))  # <class 'dict'>
pprint(data)
"""
{'response': {'count': 32363,
              'items': [{'first_name': 'Sonya',
                         'id': 287350527,
                         'last_name': 'Kargina'},
                        {'first_name': 'Slava',
                         'id': 341523166,
                         'last_name': 'Kholod'}]}}
"""
print(data["response"])
# {'count': 32363, 'items': [{'id': 287350527, 'first_name': 'Sonya', 'last_name': 'Kargina'}, {'id': 341523166, 'first_name': 'Slava', 'last_name': 'Kholod'}]}

print(data["response"]["count"])
# 32363

print(data["response"]["items"])
# [{'id': 287350527, 'first_name': 'Sonya', 'last_name': 'Kargina'}, {'id': 341523166, 'first_name': 'Slava', 'last_name': 'Kholod'}]

print(type(data["response"]["items"]))
# <class 'dict'>

data = json.loads(str_json)
for item in data["response"]["items"]:
    pprint(item)
    print(type(item))

"""
{'first_name': 'Sonya', 'id': 287350527, 'last_name': 'Kargina'}
<class 'dict'>
{'first_name': 'Slava', 'id': 341523166, 'last_name': 'Kholod'}
<class 'dict'>
"""

# Значит мы можем обращаться к ключам этого словаря:
for item in data["response"]["items"]:
    print(item["first_name"], item["last_name"])
"""
Sonya Kargina
Slava Kholod
"""


""""""
"""     Сериализация      """
# Из объекта Python в формат JSON (процесс сериализации)
# Создать строку формата JSON
# dump(obj, f)  - сериализует obj как форматированный JSON поток в f
# dumps(obj)  - сериализует obj в строку JSON-формата

import json
from pprint import pprint

str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod"
            }
        ]
    }
}
"""

data = json.loads(str_json)

for item in data["response"]["items"]:
    del item["id"]  # Удалить ключ id
    item["likes"] = 25  # Добавить ключ likes

pprint(data["response"]["items"])
"""
[{'first_name': 'Sonya', 'last_name': 'Kargina', 'likes': 25},
 {'first_name': 'Slava', 'last_name': 'Kholod', 'likes': 25}]
"""

# Теперь измененный словарь сконвертировать в строку формата JSON.
# В этом нам поможет функция dumps из модуля json.

new_json = json.dumps(data)
print(new_json)
# {"response": {"count": 32363, "items": [{"first_name": "Sonya", "last_name": "Kargina", "likes": 25}, {"first_name": "Slava", "last_name": "Kholod", "likes": 25}]}}


json_indent = json.dumps(data, indent=2)
print(json_indent)
"""
{
  "response": {
    "count": 32363,
    "items": [
      {
        "first_name": "Sonya",
        "last_name": "Kargina",
        "likes": 25
      },
      {
        "first_name": "Slava",
        "last_name": "Kholod",
        "likes": 25
      }
    ]
  }
}
"""

#  Таблица соответствия преобразования объектов:
# В данной таблице преобразования работают в обе стороны.
"""
JSON    --->    Python
object  --->    dict
array   --->    list
string  --->    str
number (int)   --->    int
number (real)  --->    float
true    --->    True
false   --->    False
null    --->    None
"""

#  стоит учитывать, что не все объекты можно легко перевести.
import datetime
for item in data["response"]["items"]:
    item['a'] = None
    item['b'] = True
    # item['now'] = datetime.now()  # AttributeError: module 'datetime' has no attribute 'now'
    # Чтобы исправить эту ошибку необходимо преобразовать объект даты к одному из базовых типов, поддерживаемых JSON.
    # Одним из типов является строка.
    # item['now'] = datetime.now().strftime("%d/%m/%y")  # "now": "30/06/22"



"""
Часто JSON необходимо сохранять в виде файла.
Для этого в json есть метод dump, который принимает 2 аргумента: 
1 – объект, который хотите сохранить, 2 – название файла.
"""
with open("my.json", "w") as file:
    json.dump(data, file, indent=2)

# Загружаем данные из файла
with open("my.json", "r") as file:
    json.load(file)
print(data)
#  {'response': {'count': 32363, 'items': [{'first_name': 'Sonya', 'last_name': 'Kargina', 'likes': 25, 'a': None, 'b': True}, {'first_name': 'Slava', 'last_name': 'Kholod', 'likes': 25, 'a': None, 'b': True}]}}
print(type(data))  # <class 'dict'>


#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Выполнить сериализацию словаря (* см. ниже) и сохранить полученную json-строку в переменную json_data
В качестве ответа ваша программа должна вывести на экран значение переменной json_data

*)
from string import ascii_lowercase
print(ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
val_num = [el for el in range(1, len(ascii_lowercase) + 1)]
alphabet = {key: val for key, val in zip(ascii_lowercase, val_num)}
print(alphabet)
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
"""

from pprint import pprint
import json

alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
            'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
            'x': 24, 'y': 25, 'z': 26}

json_data = json.dumps(alphabet)
print(json_data)



# 02
"""
В файле "02_manager_sales.json" найти самого успешного менеджера по итоговой сумме продаж. 
В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.
"""
# Вариант автора
import json

max_sale = 0
max_name = ''
max_surname = ''

with open('02_manager_sales.json', encoding='utf-8') as manager:
    data = json.load(manager)
    # print(data)
    for el in data:
        # print(el)
        name = el['manager']['first_name']
        surname = el['manager']['last_name']
        manager_sale = 0

        for car in el['cars']:
            manager_sale += car['price']

        # print(name, surname, manager_sale)
        if manager_sale > max_sale:
            max_sale = manager_sale
            max_name = name
            max_surname = surname

    print(max_name, max_surname, max_sale)  # Sharity Devonside 103690


# Хорошее решение
import json

with open('02_manager_sales.json', 'r') as file_json:
    data = json.load(file_json)
a = []
for el in data:
    a.append((el['manager']['first_name'], el['manager']['last_name'],
              sum(manager_sale['price'] for manager_sale in el['cars'])))
print(a)

print(*sorted(a, key=lambda el: el[2], reverse=True)[0])
print(*sorted(a, key=lambda el: el[2])[-1])  # Вариант



# 03
"""
В файле "03_group_people.json" содержится информация о нескольких группах людей, 
при этом у каждой группы есть свой идентификатор. 

Найти идентификатор группы, в которой находится самое большое количество женщин, рожденных после 1977 года. 
В качестве ответа необходимо указать через пробел идентификатор найденной группы и сколько в ней было женщин, 
рожденных после 1977 года.
"""
import json

ls = []

with open('03_group_people.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for el in data:
        id_group = el['id_group']
        cnt_female = 0
        for people in el['people']:
            if people['gender'] == 'Female' and people['year'] > 1977:
                cnt_female += 1
        ls.append((id_group, cnt_female))
    print(ls)
    print(*sorted(ls, key=lambda el: el[1])[-1])


# Вариант автора
import json

max_group = None
max_female = 0

with open('03_group_people.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for el in data:
        id_group = el['id_group']
        cnt_female = 0
        for people in el['people']:
            if people['gender'] == 'Female' and people['year'] > 1977:
                cnt_female += 1
        if cnt_female > max_female:
            max_female = cnt_female
            max_group = id_group
    print(max_group, max_female)


# 04
"""
Необходимо раскодировать текст, находящийся в текстовом файле "04_Abracadabra.txt". 
Ключ для декодирования располагается в json-файле "04_Alphabet.json". 
В качестве ответа нужно просто отправить получившийся текст.  
Раскодировать нужно только лишь буквы, 
все остальные символы(цифры, знаки пунктуации и т.д.) необходимо выводить как есть.
"""
import json

with open('04_Abracadabra.txt', 'r', encoding='utf-8') as file_txt:
    txt_in = file_txt.read()

with open('04_Alphabet.json', 'r', encoding='utf-8') as file_json:
    d = json.load(file_json)

txt_out = ''
d_key = d.keys()

for word in txt_in:
    for el in word:
        if el in d_key:
            txt_out += d[el]
        else:
            txt_out += el

# print(txt_out)
"""
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# Хорошее решение
import json

with open('04_Abracadabra.txt', 'r', encoding='utf-8') as file_txt, open('04_Alphabet.json', 'r',
                                                                         encoding='utf-8') as file_json:
    d = json.load(file_json)
    txt_in = file_txt.read()
    for el in txt_in:
        print(d.get(el, el), end='')


# 05
"""
Переменная people содержит строку в формате JSON, в которой вы можете получить личные данные 100 человек.
Каждого человека представляет предмет (словарь) с ключами:

имя
страна
возраст

Распечатайте информацию о каждом человеке в соответствии с примером ниже. 
...
Melissa Crawford, Lebanon, 17
Paul Herrera, Kiribati, 17
Justin Galvan, Namibia, 19
Mary Estes, Montenegro, 19
Larry Bray, Brunei Darussalam, 21
...
<Имя>, <Страна>, <Возраст>
Распечатку необходимо отсортировать по возрасту, а при равенстве возраста необходимо расположить в алфавитном порядке
"""
people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, {"name": "Matthew King", "country": "Colombia", "age": 34}, {"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, {"name": "Sarah Contreras", "country": "Honduras", "age": 82}, {"name": "Danielle Williams", "country": "Togo", "age": 91}, {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, {"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, {"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, {"name": "Christina Fernandez", "country": "Burundi", "age": 71}, {"name": "Allen Norton", "country": "Montserrat", "age": 79}, {"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, {"name": "Brooke Boyd", "country": "Latvia", "age": 74}, {"name": "Jerry Morrow", "country": "San Marino", "age": 23}, {"name": "Danielle Bradshaw", "country": "Vietnam", "age": 64}, {"name": "Jerry Thompson", "country": "Belgium", "age": 30}, {"name": "Mark Jordan", "country": "Comoros", "age": 89}, {"name": "Joseph Berger", "country": "Cook Islands", "age": 94}, {"name": "Gina Brooks", "country": "Samoa", "age": 51}, {"name": "Walter Duran", "country": "Chad", "age": 67}, {"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, {"name": "Johnny Glover", "country": "Eritrea", "age": 72}, {"name": "Lindsay Moore", "country": "Liberia", "age": 53}, {"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, {"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, {"name": "Charles Thompson", "country": "Saudi Arabia", "age": 50}, {"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, {"name": "David Decker", "country": "South Africa", "age": 71}, {"name": "Christopher Perez", "country": "Cayman Islands", "age": 49}, {"name": "Debra Hall", "country": "Greece", "age": 13}, {"name": "John King", "country": "Bahamas", "age": 40}, {"name": "Justin Galvan", "country": "Namibia", "age": 19}, {"name": "Jacqueline Berger", "country": "Yemen", "age": 59}, {"name": "Shawn Robinson", "country": "Saint Pierre and Miquelon", "age": 32}, {"name": "Kristen Garcia", "country": "Portugal", "age": 48}, {"name": "Christopher Barry", "country": "French Polynesia", "age": 23}, {"name": "Alejandra Cook", "country": "Egypt", "age": 16}, {"name": "Jill Harrell", "country": "Comoros", "age": 49}, {"name": "Sara Zimmerman", "country": "Brazil", "age": 26}, {"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75}, {"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, {"name": "Larry Wong", "country": "New Caledonia", "age": 6}, {"name": "Brenda Acosta", "country": "Grenada", "age": 48}, {"name": "Latoya Terry", "country": "Saint Martin", "age": 41}, {"name": "Seth Luna", "country": "Sao Tome and Principe", "age": 59}, {"name": "Micheal Adams", "country": "Barbados", "age": 53}, {"name": "Susan Carroll", "country": "Somalia", "age": 64}, {"name": "Douglas Morris", "country": "Thailand", "age": 24}, {"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, {"name": "Kristin Johnson", "country": "Niue", "age": 71}, {"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, {"name": "Jared Smith", "country": "Colombia", "age": 46}, {"name": "Lauren Anderson", "country": "Christmas Island", "age": 46}, {"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, {"name": "Maria Edwards", "country": "Hungary", "age": 78}, {"name": "Anne Lee", "country": "United States of America", "age": 10}, {"name": "James Mckenzie", "country": "Uganda", "age": 43}, {"name": "Joshua Gallegos", "country": "United States Minor Outlying Islands", "age": 27}, {"name": "Paul Herrera", "country": "Kiribati", "age": 17}, {"name": "Veronica White", "country": "Gabon", "age": 88}, {"name": "Michael Hall", "country": "China", "age": 43}, {"name": "Sabrina Thompson", "country": "Chad", "age": 27}, {"name": "Jennifer Archer", "country": "Korea", "age": 45}, {"name": "Christina Simmons", "country": "Israel", "age": 80}, {"name": "Travis White", "country": "Central African Republic", "age": 31}, {"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, {"name": "Matthew Richards", "country": "Svalbard & Jan Mayen Islands", "age": 34}, {"name": "Stephen Curry", "country": "Finland", "age": 92}, {"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, {"name": "Mary Estes", "country": "Montenegro", "age": 19}, {"name": "Alex Scott", "country": "Christmas Island", "age": 67}, {"name": "John Andrews", "country": "Bahamas", "age": 68}, {"name": "Jonathan Willis", "country": "Saint Martin", "age": 23}, {"name": "Olivia Campos", "country": "Armenia", "age": 72}, {"name": "Diana Davis", "country": "Azerbaijan", "age": 54}, {"name": "Jack Cummings", "country": "Martinique", "age": 94}, {"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, {"name": "Maria Blake", "country": "Pitcairn Islands", "age": 91}, {"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, {"name": "John Terrell Jr.", "country": "India", "age": 50}, {"name": "Lindsay Wood", "country": "United Arab Emirates", "age": 72}, {"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, {"name": "Tanner Johnson", "country": "Congo", "age": 11}, {"name": "Michael Garcia", "country": "Liberia", "age": 45}, {"name": "Nicole Johnson", "country": "Barbados", "age": 54}, {"name": "William Lee", "country": "Lithuania", "age": 59}, {"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, {"name": "Sandra Freeman", "country": "Philippines", "age": 35}, {"name": "Latoya Maxwell", "country": "Sweden", "age": 12}, {"name": "Darius Blevins", "country": "Thailand", "age": 29}, {"name": "Teresa Newman", "country": "Jersey", "age": 6}, {"name": "Larry Bray", "country": "Brunei Darussalam", "age": 21}, {"name": "Adam Roberson", "country": "Jordan", "age": 71}, {"name": "Michael Gomez", "country": "Tajikistan", "age": 37}, {"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, {"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, {"name": "Kevin Wagner", "country": "Suriname", "age": 55}, {"name": "Peggy Bryant", "country": "Korea", "age": 36}, {"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]'
import json

ls_in = json.loads(people)

ls = [(el['name'], el['country'], el['age']) for el in ls_in]
ls_out = sorted(ls, key=lambda el: (el[2], el[0]))

for el in ls_out:
    print(f'{el[0]}, {el[1]}, {el[2]}')


# Вариант
import json

ls_in = json.loads(people)
ls_out = [tuple([el['age'], el['name'], el['country']]) for el in ls_in]

for el in sorted(ls_out):
    print(f'{el[1]}, {el[2]}, {el[0]}')


# 06
"""
Найти и исправить ошибки в оформлении  JSON строки
"""
import json

json_string = """
{
    "customers": [
        {
            "userid": 123456,
            "username": "Allie Hsu",
            "phone": ["000-001-0002", "000-002-0002"],
            "is_vip": true
        },
        {
            "userid": 223678,
            "username": "Donald Duck",
            "phone": null,
            "is_vip": false
        }
    ]
}
"""

data = json.loads(json_string)
print(data["customers"][0]["username"])

