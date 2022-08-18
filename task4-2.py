from math import pi, e

numlist = []
count = 1
need_num = int(input('Введи количество элементов в списке: '))
while count <= need_num:
	seq = round((count**2 - e**2 - pi**3 + count**3), 2)
#	seq = 2 * count - 1
	numlist.append(seq)
	count += 1
print(numlist)