# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input("Введите день недели и узнаем отдыхаем ли сегодня или нет: "))
if a > 0 and a < 8:
    if a > 0 and a < 6:
        print('Сегодня рабочий день.')
    else:
        print("Отдыхаем.")
else:
    print("Нет такого дня недели.")