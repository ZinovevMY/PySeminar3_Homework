# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

import random

def generate_list(elements_num):
    res_list = list()
    for i in range(elements_num):
        res_list.append(random.randint(-10, 10))
    return res_list

def sum_of_elements(values_list):
    summ = 0
    for i in range(1, len(values_list), 2):
        summ += values_list[i]
    return summ

val_count = int(input("Введите количество элементов списка: "))
my_list = generate_list(val_count)
print(f"Список элементов: {my_list}")
print(f"Сумма нечетных элементов списка = {sum_of_elements(my_list)}")