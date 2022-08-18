# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


# Запрашиваем ввод числа и проверяем что введено число.
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Вводить необходимо числа!")
    return number


""" Вычисляем сумму цифр в числе. Каждый элемент введенного числа
	(кроме десятичного разделителя) преобразовываем в int и
	складываем с предыдущим значением.
"""


def addi(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = InputNumbers("Введите число: ")
print(f"Сумма цифр = {addi(num)}")