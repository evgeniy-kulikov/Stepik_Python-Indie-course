# 2.1 Строки и операции над ними


"""
Программа принимает на вход три символа через пробел в одну строку.
Необходимо вывести код каждого символа при помощи функции ord в определенном формате.
Input: q w e
Output:
Simvol code q is 113.
Simvol code w is 119.
Simvol code e is 101.
"""

s = list(map(str, input().split()))
for _ in s:
    print(f"Simvol code {_} is {ord(_)}.")
