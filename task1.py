""" Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
"""


""" Вычисление суммы цифр в числе. Каждый элемент введенного числа
	(кроме десятичного разделителя) преобразовывается в int и
	складывается с предыдущим значением.
"""
def addi(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = float(input("Введите число: "))
print(f"Сумма цифр = {addi(num)}")