# 4. Написать программу, которая генерирует в указанных пользователем границах:
# - случайное целое число;
# - случайное вещественное число;
# - случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на
# экран любой символ алфавита от 'a' до 'f' включительно.

from random import random

A, B = input('Введите числовые границы через пробел:\n').split(' ')
A, B = int(A), int(B)
NUM = int(random() * (B - A + 1)) + A
print(NUM)

A, B = input('Введите числовые границы через пробел:\n').split(' ')
A, B = float(A), float(B)
NUM = random() * (B - A) + A
print(round(NUM, 3))

A, B = input('Введите буквенные границы через пробел:\n').split(' ')
A, B = ord(A), ord(B)
LETTER = int(random() * (B - A + 1)) + A
NUM = B - A - 1  # Кол-во букв между буквами
print(chr(LETTER))
print(f'Кол-во букв между буквами {chr(A).upper()} и {chr(B).upper()}: {abs(NUM)}')
