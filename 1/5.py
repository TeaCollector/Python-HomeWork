# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

x1 = int(input('x1 = '))
y1 = int(input('y1= '))
x2 = int(input('x2 = '))
y2 = int(input('y2= '))
length = (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5
print(f'Расстояние между двумя токами равно: {round(length,2)}')