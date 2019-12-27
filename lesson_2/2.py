# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).

EVEN_NUMS = 0
ODD_NUMS = 0


# ---Цикл---
def counting_cycle(a):
    even_nums = 0
    odd_nums = 0
    while a != 0:
        numb = a % 10  # Получаем крайнее правое число
        a = a // 10  # Убираем крайнее правое число
        if numb % 2 == 0:
            even_nums += 1
        else:
            odd_nums += 1
    print(f'Кол-во четных чисел: {even_nums}\n'
          f'Кол-во нечетных чисел: {odd_nums}')


# ---Рекурсия---
def counting_req(a):
    global EVEN_NUMS, ODD_NUMS
    if a == 0:
        return print(f'Кол-во четных чисел: {EVEN_NUMS}\n'
                     f'Кол-во нечетных чисел: {ODD_NUMS}')
    numb = a % 10
    if numb % 2 == 0:
        EVEN_NUMS += 1
    else:
        ODD_NUMS += 1
    return counting_req(a // 10)


if __name__ == '__main__':
    A = int(input('Введите натуральное число:\n'))
    counting_cycle(A)
    counting_req(A)
