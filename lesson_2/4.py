# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
# клавиатуры.

SUMS = 0


# ---Цикл---
def sum_nums(n):
    sums = 0
    num = 1
    for i in range(n):
        sums += num
        num = -(num/2)
    print(f'Сумма {n} элементов ряда: "1 -0.5 0.25 -0.125 ..." равна: {sums}')


# ---Рекурсия---
def sum_nums_2(n, num):  # num - элемент последовательности
    global SUMS
    if n == 0:
        return print(f'Сумма элементов ряда: "1 -0.5 0.25 -0.125 ..." равна: {SUMS}')
    SUMS += num
    return sum_nums_2(n-1, -(num/2))


if __name__ == '__main__':
    N = int(input('Введите кол-во элементов ряда:\n'))
    sum_nums(N)
    sum_nums_2(N, 1)
