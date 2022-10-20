# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# arr = list(map(int, input('Введите числа через пробел: ').split()))
# print(arr)
# sum = 0
# print('[ ', end='')
# for i in range(0,len(arr)):
#     if i % 2 != 0:
#         print(arr[i], end=' ')
#         sum += arr[i]
# print(']')
# print(sum)



# Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# arr = list(map(int, input('Введите числа через пробел: ').split()))
# arr2 = []
# print(arr, end=' => ')
# n = len(arr)
# for i in range(0, len(arr)):
#     if i < len(arr) / 2:
#         prod = arr[i] * arr[n - 1]
#         n -= 1
#         i += 1
#         arr2.append(prod)
# print(arr2)



# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт
# разницу между максимальным и минимальным
# значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# arr = list(map(float, input('Введите числа через пробел: ').split()))
# print(arr, end=' => ')
# max = 0
# min = 1
# for i in range(0,len(arr)):
#     if arr[i] % 1 > max:
#         max = arr[i] % 1
#     elif arr[i] % 1 < min and arr[i] % 1 != 0:
#         min = arr[i] % 1
# dif = round(max - min, 2)
# print(dif)

# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('Введите число: '))
# print(num, end=' -> ')
# l1 = []
# a = len(l1) - 1
# while num != 0 :
#     if num % 2 == 0:
#         n = 0
#         l1.append(n)
#     elif num % 2 != 0:
#         n = 1
#         l1.append(n)
#     num = num // 2
# for i in range(0, len(l1) ):
#     l1[i] = l1[a]
#     a -= 1
#     print(l1[i], end=' ')



# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%
# 9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%
# BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:
# text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%
# D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%
# D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%
# B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%
# D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%
# D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%
# BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%
# B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%
# D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%
# D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%
# D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%
# 82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%
# D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%
# A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

# def fib(num):
#     fib_num = []
#     f1, f2 = 0, 1
#     for i in range(num):
#         f1, f2 = f2, f1 + f2
#         fib_num.append(f1)
#     f1, f2 = 1, 0
#     for i in range ( num + 1 ):
#         f1, f2 = f2, f1 - f2
#         fib_num.insert(0, f1)
#     return fib_num
#
# num = int(input('Введите число: '))
# print(fib(num))