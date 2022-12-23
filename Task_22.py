# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

import random
import os
os.system('cls')


def create_array(x, start, end):
    a = []
    for i in range(0, x):
        random_numbers = random.randint(start, end+1)
        a.append(random_numbers)
    return a


n = int(input('Сколько элементов будет в первом наборе? '))
m = int(input('Сколько элементов будет во втором наборе? '))
array_start = int(input('С какого числа должны быть сформированы числа в каждом наборе (какое начало интервала)? '))
array_end = int(input('И до какого (каокой конец интервала)? '))

f_array = create_array(n, array_start, array_end)
print('Первый набор:', f_array)
s_array = create_array(m, array_start, array_end)
print('Первый набор:', s_array)
