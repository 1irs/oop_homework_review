"""Дано: массив целых чисел.
Найти и вывести на консоль самый минимальный элемент, а также их количество.

Например:
1. Для массива
array = [6, 7, 8, 3, 5, 7]

Вывод на консоль:
3 1

2. Для массива
array = [10, 11, 8, 15, 8, 22]

Вывод на консоль:
8 2

Может пригодится
Оператор for позволяет перебрать все элементы массива по очереди.
"""

from typing import List

array = [10, 11, 8, 15, 8, 22]  # [6, 7, 8, 3, 5, 7] or [10, 11, 8, 15, 8, 22]


def arr_minimum(array_1: List[int]) -> int:
    i: int = 0
    temp: int = 9999
    while i < len(array_1) - 1:
        if array_1[i] > array_1[i + 1]:
            if temp > array_1[i + 1]:
                temp = array_1[i + 1]
            i += 1
        else:
            i += 1
    if array_1[0] > temp:
        return temp
    else:
        return array_1[0]


# first_arr = [10, 11, 15, 15, 5, 22, 99999999]
# second_arr = [10, 11, -5, 15, 8, 22]

# print(arr_minimum(first_arr) + arr_minimum(second_arr))


def arr_num_counter(array_2: List[int]) -> int:
    n_counter: int = 0
    for x in array_2:
        if x == arr_minimum(array_2):
            n_counter += 1
    return n_counter


print(arr_minimum(array), arr_num_counter(array))
