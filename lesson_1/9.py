# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

NUM_1 = int(input('Введите 3 разных числа\n'))
NUM_2 = int(input())
NUM_3 = int(input())

if NUM_2 < NUM_1 < NUM_3 or NUM_3 < NUM_1 < NUM_2:
    print('Среднее число:', NUM_1)
elif NUM_1 < NUM_2 < NUM_3 or NUM_3 < NUM_2 < NUM_1:
    print('Среднее число:', NUM_2)
else:
    print('Среднее число:', NUM_3)
