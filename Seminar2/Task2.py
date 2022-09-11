# 2.Найти сумму элементов массива, лежащих между
# максимальным и минимальным по значению элементами


A = [4, 5, 8, 1, 2, 6]
sum = 0
poz_min = 0
poz_max = 0
i = 1
size = len(A)
while i < size:
    if A[i] > A[poz_max]:
        poz_max = i
    elif A[i] < A[poz_min]:
        poz_min = i
    i += 1
print(poz_min, poz_max)
if poz_max > poz_min:
    for i in range(poz_min+1, poz_max):
        sum = sum + A[i]
elif poz_max < poz_min:
    for i in range(poz_max+1, poz_min):
        sum = sum + A[i]
else:
    sum = 0
print(A, sum)
