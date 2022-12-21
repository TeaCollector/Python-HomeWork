# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]


length = int(input('Input length of the array: '))
lst1 = []
for i in range(-length, length + 1):
    lst1.append(i)
print(lst1)

lst2 = [1,4,5,2,3]
multi = 1
for i in lst2:
    multi *= lst1[i]
print(multi)






