# 1 - Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


def list_prime_number(n):
    numbers = []
    d = 2
    while n>1:
        if n % d == 0:
            numbers.append(d)
            while n%d==0:
                n/=d
        else:
            d += 1
    return numbers
x = list_prime_number(int(input('Введите число: ')))
print(x)