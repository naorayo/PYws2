""" 1) Функция принимает на вход список (ввод пользователем).
	2) Введем переменную i, которая изменятся в цикле от 0 до
	"длина списка - 1".
	3) Введем переменную min_index и присвоим ей значение i.
	4) Введем внутренний цикл с переменной j, которая изменяется
	от i+1 до "длина списка".
	5) В цикле: если элемент с индексом [j] МЕНЬШЕ элемента с
	индексом [min_index], то принимаем min_index = j
	6) Меняем местами элементы с индексами [i] и [min_index]
"""


def selsort(numlist):
	for i in range(0, len(numlist) - 1):
		min_index = i
		for j in range (i+1, len(numlist)):
			if numlist[j] < numlist[min_index]:
				min_index = j
		numlist[i], numlist[min_index] = numlist[min_index], numlist[i]


numlist = input('Введи числа через пробел: ').split()
numlist = [int(x) for x in numlist]
print("До сортировки: ", numlist)
selsort(numlist)
print("После сортировки: ", numlist)