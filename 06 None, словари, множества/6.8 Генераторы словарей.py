# 6.8 Генераторы словарей
""""""

"""
Общий вид генератора словарей:
{ ключ: значение for <переменная> in <последовательность>}
"""
a = {i: i ** 2 for i in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


a = {word: len(word) for word in ['hi', 'hello', 'www']}
# {'hi': 2, 'hello': 5, 'www': 3}


data = {
    'ИлоН МаСк': '126',
    'бернар АрнО': '150',
    'БиЛл ГеЙтС': '124',
}
new_data = {key.title(): int(value) for key, value in data.items()}
# {'Илон Маск': 126, 'Бернар Арно': 150, 'Билл Гейтс': 124}


users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [3, 'username', '1234'],
    [51, 'qwerty', '1234']
]

new_users = {user[0]: user for user in users}
# {0: [0, 'Bob', 'password'], 1: [1, 'code', 'python'], 3: [3, 'username', '1234'], 51: [51, 'qwerty', '1234']}

new_users[51]  # [51, 'qwerty', '1234']


#
#  *  *  *   Задачи   *  *  *
#


# 1
"""
https://stepik.org/lesson/545393/step/2?unit=538968
Напишите программу для создания нового словаря, которая извлекает указанные ключи из приведенного ниже словаря.
Сами значения ключей, которые нужно извлечь, поступают на вход программе в виде одной строки разделенные пробелом
Input:  password phone_number social_insurance_number
Output: {'password': 'SyUpfo1ljm', 'phone_number': '+674 424.561.2776', 'social_insurance_number': '637316241'}
"""
user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
    "employment": {
        "title": "Central Hospitality Liaison",
        "key_skill": "Organisation"
    },
    "subscription": {
        "plan": "Essential",
        "status": "Idle",
        "payment_method": "Debit card",
        "term": "Annual"
    }
}
# keys = ['subscription', 'uid', 'date_of_birth', 'first_name']

keys = input().split()
d = {key: user[key] for key in keys}  # ключи в словаре расположены точно как в 'keys'
# d = {key: value for key, value in user.items() if key in keys}  # нет точного расположения ключей
print(d)


# 2
"""
https://stepik.org/lesson/545393/step/3?unit=538968
Имеется вложенный список people, в котором хранятся имена и телефоны. 
Создать словарь при помощи генератора словарей, 
в котором в качестве ключей будут храниться номера телефонов, 
а значениями будут имена владельцев.
"""
# from pprint import pprint
people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]

phone_book = {el[1]: el[0] for el in people}
# pprint(phone_book)
