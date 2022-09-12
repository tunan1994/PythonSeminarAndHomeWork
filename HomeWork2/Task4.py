# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime
# (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time
def random(max_number, min_number):

    t_data = '%.9f' % time.time()
    time.sleep(0.00001)
    interval = max_number - min_number
    razrad = len(str(interval)) * -1
    smech = int(t_data[razrad:])

    while smech > interval:
        smech = int(smech / 2)

    rnd = min_number + smech
    return rnd
print(random(100, 10))