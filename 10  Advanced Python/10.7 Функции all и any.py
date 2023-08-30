# 10.7 Функции all и any
""""""

"""
Функция all

all(iterable)
    Return True if bool(x) is True for all values x in the iterable.   
    If the iterable is empty, return True.
    
Функция all() принимает итерабельную последовательность и возвращает True , 
когда все элементы в этой последовательности правдивы. 
Если хотя бы один элемент пустой, вернется False
"""
b = ['hi', '', 'world']
print(all(b))  # False

numbers = [1, 2, 3, 4, 5]
print(all(numbers))  # True

numbers = [1, 2, 3, 4, 0]
print(all(numbers))  # False


"""
Функция any

any(iterable)
    Return True if bool(x) is True for any x in the iterable.    
    If the iterable is empty, return False.
    
Функция any() принимает на вход итерабельную последовательность и возвращает True, 
если хотя бы один из элементов коллекции будет непустым. 
Если все элементы пустые, вернется False
"""

print(any(['', '', '']))  # False
print(any([0, 0, 0, 0]))  # False
print(any([False, False, True]))  # True

#
#  *  *  *   Задачи   *  *  *
#


# 01
"""
Программе на вход поступают слова, разделенные пробелом. 
Проверить, во всех ли словах есть английская буква A вне зависимости от регистра. 
В качестве ответа вывести True или False
"""
# s = ['chase', 'enlarge', 'referee', 'cup', 'offense']
s = input().lower().split()
res = ['a' in el for el in s]
print(all(res))

# Короче
print(all('a' in el for el in input().lower().split()))

# Вариант
s = input().split()
res = [set('Aa') & set(word) for word in s]
print(all(res))


# 02
"""
На вход будут поступать слова, разделенные пробелом. 
Программа должна вывести True , если встретилось хотя бы одно слово, заканчивающееся на ought. 
В противном случае нужно вывести False.
Регистр букв не имеет значения, 
значит интересующиеся нас  слова могут заканчиваться как на ought, так и например на OUGHT

Input:  food forethought muscle stadium
Output: True
"""
s = input().lower().split()
res = ['ought' in el[-5:] for el in s]
print(any(res))

# Вариант
print(any((word.endswith('ought') for word in input().lower().split())))
