# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
# сумму его цифр.
SUM_1 = 0
SUM_2 = 0


# ---Цикл---
def sum_num(a, b):
    num_1 = a
    num_2 = b
    sum_1 = 0
    sum_2 = 0
    while a != 0:
        numb = a % 10  # Получаем крайнее правое число
        a = a // 10  # Убираем крайнее правое число
        sum_1 += numb
    while b != 0:
        numb = b % 10  # Получаем крайнее правое число
        b = b // 10  # Убираем крайнее правое число
        sum_2 += numb
    if sum_1 > sum_2:
        print(f'Число {num_1}, Сумма {sum_1}')
    elif sum_1 == sum_2:
        print(f'Суммы равны {sum_1}, {sum_2}')
    else:
        print(f'Число {num_2}, Сумма {sum_2}')


# ---Рекурсия---
def sum_num_2(a, b, num_1, num_2):
    global SUM_1, SUM_2
    numb_1 = a % 10  # Получаем крайнее правое число
    numb_2 = b % 10  # Получаем крайнее правое число
    SUM_1 += numb_1
    SUM_2 += numb_2

    if a == 0 and b == 0:
        if SUM_1 > SUM_2:
            return print(f'Число {num_1}, Сумма {SUM_1}')
        elif SUM_1 == SUM_2:
            return print(f'Суммы равны {SUM_1}, {SUM_2}')
        else:
            return print(f'Число {num_2}, Сумма {SUM_2}')
    return sum_num_2(a // 10, b // 10, num_1, num_2)


if __name__ == '__main__':
    A = int(input('Введите натуральное число:\n'))
    B = int(input('Введите натуральное число:\n'))
    print('-----Цикл-----')
    sum_num(A, B)
    print('---Рекурсия---')
    sum_num_2(A, B, A, B)
