# 1. Напишите программу, которая принимает
#  на вход число N и выдаёт последовательность
# из N членов в виде списка
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

N = int(input('Введите число = '))

print(f"Для N={N} -> ", end='')
for i in range(0, N-1):
    print((-3)**i, end=", ")
else:
    print((-3)**(N-1))
