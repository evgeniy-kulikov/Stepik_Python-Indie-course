# 7.4 Docstring и аннотации
""""""


"""
help(print)
print.__doc__

Контекстное меню:
Выделяем функцию, а далее сочетание клавиш Ctrl + Q
"""

def summ_num(a, b):
    """Сумма двух чисел"""
    return a + b

help(summ_num)
# summ_num(a, b)
#     Сумма двух чисел

print(summ_num.__doc__)  # Сумма двух чисел



"""
Встроенный модуль typing позволяет создавать аннотации в более сложных случаях, 
например если вы хотите проаннотировать переменную сразу несколькими типами 
или указать аннотацию для элементов списка.

Модуль typing широко применялся вплоть до версии python3.9 пока не появился стандарт PEP 585. 
До версии python3.9 модуль typing был единственным способом проаннотировать объекта способами, указанными ниже
"""
# Optional
# При помощи объекта Optional мы можем разрешить хранить в одной переменной не только указанный тип,
# но и значение None

from typing import Optional

num: Optional[int] = None
word: Optional[str] = None
# Обязательно после Optional тип указывается в квадратных скобках [ ]


# Union
# C помощью этого объекта можно указывать сразу несколько типов данных, которые могут быть приняты.
from typing import Union

param: Union[int, float, str] = 3

# Union полезна в версиях python до 3.9,
# поскольку в этой версии появилась короткая запись данной функции через вертикальную черту:

param: int | float | str


# Аннотация элементов списков и множеств
"""
Для того, чтобы указать, что переменная содержит список 
можно использовать тип list в качестве аннотации. 
Однако если хочется конкретизировать, из каких элементы состоит список, 
то для этого можно воспользоваться typing.List. 
Аналогично тому, как мы указывали тип опциональной(Optional) переменной, 
мы указываем тип элементов кортежа в квадратных скобках.
"""
from typing import List

words: List[str] = ["hello", "world"]

# Аналогичным образом можно проаннотировать множества, причем как изменяемые так и неизменяемые

from typing import Set, FrozenSet

words: Set[str] = {"hello", "world"}
numbers: FrozenSet[int] = frozenset([1, 2, 2, 1])


# Аннотация элементов кортежа
"""
Кортежи в отличие от списков часто используются для разнотипных элементов. 
Синтаксис похож с одним отличием: в квадратных скобках указывается тип каждого элемента кортежа по отдельности
"""
from typing import Tuple

words: Tuple[str, int] = ("hello", 300)


"""
Если же планируется использовать кортеж аналогично списку: 
хранить неизвестное количество однотипных элементов, можно воспользоваться многоточием (...).
"""
from typing import Tuple

words: Tuple[str, ...] = ("hello", "world", '!')


# Аннотация словарей
"""
Чтобы добавить аннотации типа словарю,  используете тип Dict, 
в которым следует тип ключа и тип значения следующим образом:

from typing import Dict
Dict[key_type, value_type]
"""
from typing import Dict
person: Dict[str, str] = { "first_name": "John", "last_name": "Doe"}


# более сложный пример
"""
Здесь функция foo принимает один аргумент bar, он должен являться словарем, 
у которого ключи могут быть либо строкой либо целым числом, 
а значения могут быть либо пустыми (тип None) , либо строкой 
"""
from typing import Dict, Optional, Union

def foo(bar: Dict[Union[str, int], Optional[str]]) -> bool:
   return True


def foo(bar: Dict[str | int, Optional[str]]) -> bool:
   return True



#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
https://stepik.org/lesson/611485/step/12?unit=606807
Напишите функцию first_repeated_word, которая принимает строку, состоящую из нескольких слов, 
слова разделяются между собой пробелом. 
Функция должна найти первое повторяющееся слово и вернуть его в качестве результата.
(!!! но не первое слово у которого дальше будет повтор !!!) 
Если передана строка, в которой все слова различны, то вернуть None
Input:  "ab ca bc ca ab bc"
Output: "ca"
"""

def first_repeated_word(st: str) -> str:
    """
    Находит первый дубль в строке
    """
    ls = []
    for el in st.split():
        if el in ls:
            return el
        else:
            ls.append(el)
    # return None

# print(first_repeated_word("1 2 3 2")) # 2
# print(first_repeated_word("1 2 3 4")) # None
# print(first_repeated_word("ab ca bc ca ab bc"))


# 02
"""
https://stepik.org/lesson/611485/step/15?unit=606807
Напишите функцию shift_letter , которая принимает два аргумента:
letter одна английская буква в нижнем регистре
shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift.
Функция shift_letter  должна вернуть новый символ.
Сдвиг может быть цикличным в пределах от a до z. 
Ниже примеры:
shift_letter('b', 2)=> 'd'
shift_letter('d', 1) => 'e'
shift_letter('z', 1) => 'a'
shift_letter('d', -2) => 'b'
shift_letter('d', 26) => 'd'
shift_letter('b', -3) => 'y'
"""

def shift_letter(letter: str, shift: int) -> str:
    """
    Функция сдвигает символ letter на shift позиций
    """
    return chr((ord(letter) - 97 + shift) % 26 + 97)

# print(shift_letter('b', -3))  # 'y'
# print(shift_letter('d', 26))  # 'd'
# print(shift_letter('d', -26)) # 'd'


# 03
"""
Шифр цезаря
https://stepik.org/lesson/611485/step/16?unit=606807
Напишите функцию shift_letter , которая принимает два аргумента:
letter одна английская буква в нижнем регистре
shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift.
Функция shift_letter  должна вернуть новый символ.
Сдвиг может быть цикличным в пределах от a до z. 
Ниже примеры:
caesar_cipher('leave out all the rest', -1) => 'kdzud nts zkk sgd qdrs'
caesar_cipher('one more light', 3) => 'rqh pruh oljkw'
"""

def shift_letter(letter: str, shift: int) -> str:
    """
    Функция сдвигает символ letter на shift позиций
    """
    return chr((ord(letter) - 97 + shift) % 26 + 97)


def caesar_cipher(s: str, shift: int) -> str:
    """Шифр цезаря"""
    res = ''
    for el in s:
        if el.isalpha():
            res += shift_letter(el, shift)
        else:
            res += el
    return res

# print(caesar_cipher('leave out all the rest', -1))

