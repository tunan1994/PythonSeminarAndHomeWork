# 2. Задайте два числа. Напишите программу, которая найдет НОК 
# (наименьшее общее кратное) этих двух чисел. 
# НОК - наименьшее общее кратное, которое делится и на первое, и на второе число. 

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def NOD(a,b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif a > b:
        return NOD(a%b, b)
    else:
        return NOD(b%a, a)


def NOK(a, b):
    return a*b / NOD(a, b)
print(int(NOK(a, b)))