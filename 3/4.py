# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

i = int(input('Input decimal number and I will convert it to binary: '))

string = ''
while i != 0:
    left = i % 2
    string = str(left) + string 
    i //= 2
print(f'This is a binary number: {string}')