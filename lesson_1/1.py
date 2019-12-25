# Найти сумму и произведение цифр трехзначного числа, которое вводит
# пользователь.

# A = input('Введите трехзначное число:\n')
# SUM = 0
# MULTI = 1
# for i in list(A):
#     SUM += int(i)
#     MULTI *= int(i)
# print(f'Сумма чисел: {SUM}\n'
#       f'Произведение чисел: {MULTI}')

A = int(input('Введите трехзначное число:\n'))
SUM = 0
MULTI = 1
while True:
    numb = A % 10  # Получаем крайнее правое число
    A = A // 10  # Убираем крайнее правое число
    SUM += int(numb)
    MULTI *= int(numb)
    if A == 0:
        break
print(f'Сумма чисел: {SUM}\n'
      f'Произведение чисел: {MULTI}')