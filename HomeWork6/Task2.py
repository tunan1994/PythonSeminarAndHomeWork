# 2.Найти сумму чисел списка стоящих на нечетной позиции


y = list(map(int,input("Введите числа через пробел: ").split()))
print(sum(list(filter(lambda x:y.index(x)%2,y))))

# print(sum(x[1::2]))

