# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random as rand

l = int(input('Введите длину списка: '))
ls = [rand.randint(1,50) for i in range(l)]
sum = 0
for i in range(1, l, 2):                     
    sum += ls[i]
print(ls)
print(f'Сумма чисел на нечетных позициях равна: {sum}')




# Не много отличное решение: 

# l = int(input('Введите длину списка: '))
# ls = [rand.randint(1,50) for i in range(l)]

# new_ls = ls[1:l:2] # срез!
# sum_nefw_ls = sum(new_ls)
# print(ls)
# print(new_ls)
# print(f'Сумма чисел на нечетных позициях равна: {sum_nefw_ls }')
