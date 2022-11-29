# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

from functools import lru_cache


@lru_cache()
def fibonacci(num: int):
    print(f"Считаю {num} число Фибоначчи")
    if num == 0:
        return 0
    if num in [-1, 1, 2]:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


fib_num = int(input("Введите позицию числа Фибоначчи: "))
fib_list = list()
i = -fib_num
while i <= fib_num:
    fib_list.append(fibonacci(i))
    i +=1
print(fib_list)
