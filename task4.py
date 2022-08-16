from random import randint
numlist = []
count = 1
need_num = int(input('Введи количество элементов в списке:'))
while count <= need_num:
	numlist.append(randint(-1000,1000))			#Генерируем последовательность из введенного количества элементов
	count += 1
print(numlist)