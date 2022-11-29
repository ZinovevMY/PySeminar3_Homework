# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def decimal2bin(number):
    res = ""
    if number == 0:
        res = "00"
        return res
    if number == 1:
        res = "01"
        return res
    while number > 0:
        res = str(number % 2) + res
        number = number // 2
    return res


number = int(input("Введите число: "))
bin_num = decimal2bin(number=number)
print(f" Число {number} в двоичном коде выглядит как {bin_num}")
