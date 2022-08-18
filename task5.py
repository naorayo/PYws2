""" Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
"""

str1 = str(input('Введите первую строку: '))
str2 = str(input('Введите вторую строку: '))

#Поиск вхождений одной строки в другую
def count_overlapping_substrings(string, subseq):
	count = 0
	i = -1
	while True:
		i = string.find(subseq, i+1)
		if i == -1:
			return count
		count += 1
print(count_overlapping_substrings(str1, str2))