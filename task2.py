# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Определяем факториал в цикле
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
num = int(input("Введите число: "))


# Составляем список из факториалов
list = []
for e in range(1, num + 1):
    list.append(fact(e))

print(f"Произведения чисел от 1 до {num}:  {list}")