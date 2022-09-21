# 1 - Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


n = int(input('Введите число N: '))
def list_prime_number(n):
    numbers = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            numbers.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        numbers.append(n)
    return numbers
print(list_prime_number(n))