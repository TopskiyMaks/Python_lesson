# 3. Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486, то надо
# вывести число 6843.

reverse_numb = ''


# ---Цикл---
def reverse(a):
    reverse_num = ''
    while a != 0:
        numb = a % 10  # Получаем крайнее правое число
        a = a // 10  # Убираем крайнее правое число
        reverse_num += str(numb)
    print(reverse_num)


# ---Рекурсия---
def reverse_2(a):
    global reverse_numb
    if a == 0:
        return print(reverse_numb)
    numb = a % 10  # Получаем крайнее правое число
    reverse_numb += str(numb)
    return reverse_2(a // 10)


if __name__ == '__main__':
    A = int(input('Введите натуральное число:\n'))
    reverse(A)
    reverse_2(A)
