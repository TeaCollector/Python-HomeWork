# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

num = int(input('Input number: '))
i: int = 2
while i != num:
    if num % i == 0:
        break
    else:
        i += 1
print(f'Наименьший возможный делитель это число {i}')