# 5.Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


list_numbers = [3,14,159,265,35,8,97]    # 3,1415926535897
half_list = (len(list_numbers)//2 +1)
multiplication_result = list(map(lambda i: list_numbers[i] * list_numbers[len(list_numbers) - i - 1], range(half_list)))
print(multiplication_result)

