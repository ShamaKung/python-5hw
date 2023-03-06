import re

'''
#Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.

expression = input('Что вычислить?')
print(eval(expression))
'''

'''
s = 'My heart in the Highland'

s2 = re.sub(r'\s+', '\n', s)
print(s2)

'''

'''
def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))
'''


def summa(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a



print(summa(2, 2))