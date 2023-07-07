# 7.13 Замыкания в Python. Closure Python
""""""

def main_func():
    def inner_func():
        print('hello my friend')

    inner_func()


b = main_func()
print(b)
# hello my friend
# None



# Для замыкания  не хватает только добавления локальных переменных в тело внешней функции
# При этом переменная name не исчезнет после завершения
def main_func():
    name = 'Ivan'
    def inner_func():
        print('hello my friend', name)

    return inner_func

b = main_func()
print(b)
# <function main_func.<locals>.inner_func at 0x000002D0F8D23E20>
b()  # hello my friend Ivan



def main_func(name):
    def inner_func():
        print('hello my friend', name)

    return inner_func

b = main_func('Tom')
b()  # hello my friend Tom
c = main_func('Kate')
c()  # hello my friend Kate
b()  # hello my friend Tom


def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

stream_1 = counter()
stream_2 = counter()
print(stream_1())  # 1
stream_1()
print(stream_1())  # 3
print(stream_2())  # 1
print(stream_1())  # 4
print(stream_1())  # 5
print(stream_2())  # 2



def adder(a):
    def inner(b):
        return a + b
    return inner


a2 = adder(2)
print(a2(5))  # 7
print(a2(10))  # 12


# Несколько функций в замыкании
def create_counter():
    count = 0

    def increment(value: int = 1):
        nonlocal count
        count += value
        return count

    def decrement(value: int = 1):
        nonlocal count
        count -= value
        return count

    return increment, decrement


inc_1, dec_1 = create_counter()
print(inc_1())  # 1 (увеличиваем на 1)
print(inc_1(2))  # 3 (увеличиваем на 2)
print(inc_1(3))  # 6 (увеличиваем на 3)
print(dec_1())  # 5 (уменьшаем на 1)
print(dec_1())  # 4 (уменьшаем на 1)


# Создаем новый объект замыкания с другим счетчиком
inc_2, dec_2 = create_counter()
print(inc_2(10))  # 10 (увеличиваем на 10)
print(dec_2(5))  # 5 (уменьшаем на 5)
print(inc_2(100))  # 105 (увеличиваем на 100)
print(inc_2(50))  # 155 (увеличиваем на 50)
print(dec_2())  # 154 (уменьшаем на 1)



#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Создать функцию-замыкание create_accumulator, 
она должна накапливать(суммировать) в себе все значения, 
которые ей будут переданы, при создании сумма должна быть равна нулю.

summator_1 = create_accumulator()
print(summator_1(1)) # 1
print(summator_1(5)) # 6
print(summator_1(2)) # 8

summator_2 = create_accumulator()
print(summator_2(3)) # 3
print(summator_2(4)) # 7

При каждом вызове должна возвращаться накопленная сумма, которая хранится в замыкании.
Обратите внимание, что объекты из примера summator_1 и summator_2 хранят и накапливают свои собственные суммы.
"""
def create_accumulator():
    total = 0
    def get_sum(n):
        nonlocal total
        total += n
        return total
    return get_sum

# summator_1 = create_accumulator()
# print(summator_1)  # <function create_accumulator.<locals>.get_sum at 0x0000019905EBEEF0>
# print(summator_1(1))  # 1
# print(summator_1(5))  # 6
# print(summator_1(2))  # 8
# print('- ' * 20)
# summator_2 = create_accumulator()
# print(summator_2(3)) # 3
# print(summator_2(4)) # 7


# 02
"""
Усовершенствуем функцию-замыкание create_accumulator, 
чтобы она могла начинать суммировать, начиная с определенного значения. 
Это значение мы ей будем передавать, но оно является необязательным. 

summator_1 = create_accumulator(100)
print(summator_1(1)) # 101
print(summator_1(5)) # 106
print(summator_1(2)) # 108

summator_2 = create_accumulator()
print(summator_2(3)) # 3
print(summator_2(4)) # 7

Во втором примере мы не передали значение и значит сумма по умолчанию должна считаться с нуля.
Обратите внимание, что объекты из примера summator_1 и summator_2 хранят и накапливают свои собственные суммы.
"""

def create_accumulator(total=0):

    def get_sum(n):
        nonlocal total
        total += n
        return total
    return get_sum

# summator_1 = create_accumulator(100)
# print(summator_1(1))  # 101
# print(summator_1(5))  # 106
# print(summator_1(2))  # 108
# print('- ' * 20)
# summator_2 = create_accumulator()
# print(summator_2(3)) # 3
# print(summator_2(4)) # 7


# 03
"""
Создать функцию multiply, которая принимает один аргумент. 
Функция должна запомнить это значение, 
и вернуть результат умножения этого числа с переданным вновь значением (см. примеры)

f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5)) #10
print("Умножение 2 на 15 =", f_2(15)) #30
f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5)) #15
print("Умножение 3 на 15 =", f_3(15)) #45
"""

def multiply(num_1):

    def get_mult(num_2):
        return num_1 * num_2
    return get_mult


f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5))  # 10
print("Умножение 2 на 15 =", f_2(15))  # 30
print('- ' * 20)
f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5))  # 15
print("Умножение 3 на 15 =", f_3(15))  # 45


# 04
"""
Создать функцию-замыкание create_dict, 
она должна сохранять в себе все значения, которые ей будут переданы причем в виде словаря. 
Ключами данного словаря должны быть натуральные числа, равные номеру вызова данной функции.

f_1 = create_dict()
print(f_1('hello')) # f_1 возвращает {1: 'hello'}
print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict() # создаем новое замыкание в f_2
print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}
"""

def create_dict():
    key = 0
    d = dict()

    def inner(val):
        nonlocal key
        key += 1
        d[key] = val
        return d

    return inner

f_1 = create_dict()
print(f_1('hello'))  # f_1 возвращает {1: 'hello'}
print(f_1(100))  # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3]))  # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict()  # создаем новое замыкание в f_2
print(f_2('PoweR'))  # f_2 возвращает {1: 'PoweR'}



