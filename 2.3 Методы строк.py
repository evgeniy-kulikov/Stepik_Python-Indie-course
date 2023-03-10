# 2.3 Методы строк
""""""
"""
s.upper()
Метод возвращает новую строку из строки S, превращает все буквы в заглавные. 
Если в строке будут присутствовать символы или цифры, то они останутся неизменными. 
Цифры и знаки пунктуации игнорируются.


s.lower()
Метод возвращает новую строку из строки S, превращает все буквы в строчные(нижний регистр). 
Если в строке будут присутствовать символы или цифры, то они останутся неизменными.


s.title()
Метод возвращает новую строку, в которой каждое слово исходной строки начинается с буквы в верхнем регистре, 
а все остальные буквы в нижнем. Цифры и знаки пунктуации игнорируются.


s.capitalize()
Метод возвращает новую строку, в которой только первый символ находится в верхнем регистре, 
а все остальные в нижнем. Цифры и знаки пунктуации игнорируются.


swapcase()
Метод превращает первую букву каждого слова в заглавную, а остальные буквы делает маленькими

"""


"""
На вход подается строка. Нужно отформатировать строку так, 
чтобы первые 3 и последние 3 символа были заглавными, а оставшиеся строчные.
Примечание:
Количество букв может быть различным, но гарантируется что их количество не меньше 6
Input:      прогРаммирОВАНИЕ
Output:     ПРОграммироваНИЕ
"""
s = input()
print(s[:3].upper() + s[3:-3].lower() + s[-3:].upper())


"""
На вход программе поступает строка, состоящая как из заглавных так из строчных букв. 
Нужно преобразовать строку так, чтобы первая буква у каждого слова стала маленькой, 
а остальные буквы превратились в заглавные. 
Символы пунктуации и цифры не нужно преобразовывать.
Input:      Every You Every Me
Output:     eVERY yOU eVERY mE
"""
s = input().title()
print(s.swapcase())


"""
На вход программе поступает строка, нужно подсчитать сколько раз в ней встречается латинская буква "e". 
При этом стоит учитывать как маленькие, так и заглавные буквы
Input:      Helen
Output:     2
"""
s = input().lower()
print(s.count("e"))


"""
На вход программе поступает строка, нужно вывести на экран индекс индекс первой латинской буквы  "a"
Если такого символа в введенной строке нет, выведите -1
Input:      banana
Output:     1

Input:      zoo
Output:     -1
"""
s = input()
print(s.find("a"))


"""
На вход программе поступает строка, нужно вывести на экран индекс последней найденной латинской буквы  "a"
Если такого символа в введенной строке нет, выведите -1
Input:      banana
Output:     5

Input:      zoo
Output:     -1
"""
s = input()
print(s.rfind("a"))


"""
Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.
Заменить все пробелы запятыми и вывести полученную строку.
Input:      Smells Like Teen Spirit
Output:     Smells,Like,Teen,Spirit
"""
s = input()
print(s.replace(" ", ","))


"""
На вход программе поступает строка (маленькие буквы), нужно удалить из нее все символы w и z
Input:      what's up?
Output:     hat's up?
"""
s = input()
print(s.replace("w", "").replace("z", ""))


"""
Программа должна делать следующее:
в заданной строке, которая состоит из прописных и строчных латинских букв, она:
* удаляет все гласные буквы,
* перед каждой согласной буквой ставит символ ".",
* все прописные согласные буквы заменяет на строчные.
Гласными буквами считаются буквы A, O, Y, E, U, I,  а согласными — все остальные.

На вход программе подается ровно одна строка,
она должна вернуть результат в виде одной строки, получившейся после обработки.
Input:      Codeforces
Output:     .c.d.f.r.c.s
"""
s = input().lower()
vowels = "aoyeui"
for _ in vowels:
    s = s.replace(_, '')
print("." + ".".join(list(s)))