# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

import random
from decimal import Decimal, ROUND_FLOOR


def generate_list(elements_num):
    res_list = list()
    list_elem = 0
    for i in range(elements_num):
        list_elem = Decimal(str(random.uniform(1, 10)))
        res_list.append(float(list_elem.quantize(Decimal('1.00'),ROUND_FLOOR)))
    return res_list


def list_min_max(elem_list):
    min_val = Decimal(str(elem_list[1]))
    max_val = Decimal(str(elem_list[0]))
    if len(elem_list) == 2:
        return max(elem_list) % 1, min(elem_list) % 1
    for i in range(1, len(elem_list)):
        if elem_list[i] < min_val:
            min_val = Decimal(str(elem_list[i]))
        elif elem_list[i] > max_val:
            max_val = Decimal(str(elem_list[i]))
    return max_val % 1, min_val % 1


def max_min_difference(max_min_list):
    return max_min_list[0] - max_min_list[1]

count = int(input("Введите количество элементов списка: "))
my_list = generate_list(count)
print(f"Полученный список: {my_list}")
difference = Decimal(str(max_min_difference(list_min_max(my_list))))
print(f"Разность дробных частей максимально и минимального элементов = {float(difference.quantize(Decimal('1.00'), ROUND_FLOOR))}")