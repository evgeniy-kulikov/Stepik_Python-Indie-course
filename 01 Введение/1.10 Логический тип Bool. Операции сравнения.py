# 1.10 Логический тип Bool. Операции сравнения
""""""

# Доказательство треугольника
s = list(map(int, input().split()))
print(sum(s) > max(s) + min(s))


# Доказательство правильного треугольника
a, b, c = map(int, input().split())
print(a == b == c)


# Доказательство равнобедренного треугольника
s = list(map(int, input().split()))
s.remove(max(s))
print(s[0] == s[1])


# Доказательство прямоугольного треугольника
s = list(map(int, input().split()))
num_max = s.pop(s.index(max(s)))
print(num_max ** 2 ==  (s[0] ** 2 + s[1] ** 2))

# Варианты
s = sorted(list(map(int, input().split())))
print(s[2] ** 2 == s[0] ** 2 + s[1] ** 2)

a, b, c = map(lambda x: int(x) ** 2, input().split())
print(c == a + b or b == a + c or a == b + c)


"""
Input:  
Output: 
"""