# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


# ---Цикл---
def symbols_cycle():
    for i in range(32, 128):
        print("%4d - %s" % (i, chr(i)))


# ---Рекурсия---
def symbols_req(i):
    while i <= 128:
        print("%4d - %s" % (i, chr(i)))
        return symbols_req(i+1)
    return


if __name__ == '__main__':
    symbols_cycle()
    symbols_req(32)