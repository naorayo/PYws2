from math import pi
from math import e

numlist = []
count = 1
need_num = int(input('Введи количество элементов в списке: '))
while count <= need_num:
	seq = round((count**2 - e**2 - pi**3 + count**3 ), 2)
	numlist.append(seq)
	count += 1
print(numlist)