import re
'''
#Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.

expression = input('Что вычислить?')
print(eval(expression))
'''



s = 'My heart in the Highland'

s2 = re.sub(r'\s+', '\n', s)
print(s2)