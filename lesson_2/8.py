# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
COUNT = 0


# ---Цикл---
def cycle(n, b):
    count = 0
    for i in range(1, n + 1):
        m = int(input(f"Число {str(i)}: "))
        while m > 0:
            if m % 10 == b:
                count += 1
            m = m // 10
    print("Было введено %d цифр %d" % (count, b))


# ---Рекурсия---
def req(n, b):
    global COUNT
    if n == 0:
        return print(f"Было введено {COUNT} цифр {b}")
    m = int(input(f"Число: "))
    while m > 0:
        if m % 10 == b:
            COUNT += 1
        m = m // 10

    return req(n-1, b)


if __name__ == '__main__':
    print('-----Цикл-----')
    N = int(input("Сколько будет чисел?\n"))
    B = int(input("Какую цифру считать?\n"))
    cycle(N, B)
    print('---Рекурсия---')
    N = int(input("Сколько будет чисел?\n"))
    B = int(input("Какую цифру считать?\n"))
    req(N, B)
