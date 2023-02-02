# 1.7 Функция print()
"""
Программа принимает на вход строку - разделитель, вам необходимо распечатать числа от 1 до 5,
выводя между ними введенный разделитель
Input:  $
Output: 1$2$3$4$5
"""
s = input()
print(*range(1, 6), sep=s)

# var
s = input()
print(*[el for el in range(1,6)], sep=s)

s = input()
print(1, 2, 3, 4, 5, sep=s)


"""
Что будет напечатано в результате выполнения данной программы?
"""
print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')
# Гвидо*Ван*Россум-Основатель_Питона!

