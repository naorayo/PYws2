def fact(n):    											# Определяем факториал в цикле
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Введите число: "))

list = []													# Составляем список из факториалов
for e in range(1, num + 1):
    list.append(fact(e))

print(f"Произведения чисел от 1 до {num}:  {list}")