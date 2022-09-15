import datetime, math

def random(_min: int, _max: int) -> int:

    '''
    Генерация случайного числа
    params:
    min - начало диапазона
    max - конец диапазона
    '''
    d = _max - _min  # 9
    ms = datetime.datetime.today().microsecond / (10 ** 6)
    # print(f'{ms=}')
    return _min + math.ceil(d * ms)

print(random(1,10))


list1 = [1, 2, 3, 5, 8, 15, 23, 38]

def f(x):
    return x**2

list2=[(i, f(i)) for i in list1 if i%2==0]
print(list2)
