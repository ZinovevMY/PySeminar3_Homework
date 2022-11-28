# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random


def generate_list(elements_num):
    res_list = list()
    for i in range(elements_num):
        res_list.append(random.randint(-10, 10))
    return res_list


def product_elements(elem_list):
    res_list = list()
    step_count = len(my_list) / 2
    if step_count % 2 != 0:
        step_count += 1
    for i in range(int(step_count)):
        res_list.append(my_list[i] * my_list[-1 - i])
    return res_list


count = int(input("Введите количество элементов списка: "))
my_list = generate_list(count)

print(f"Исходный список элементов: {my_list}")
print(f"Произведение элементов списка: {product_elements(my_list)}")
