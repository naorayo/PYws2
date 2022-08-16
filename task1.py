inp_num = int(input("Введи число: "))

addi = 0
#multi = 1

while inp_num > 0:
	digit = inp_num % 10
	addi = addi + digit
	#multi = multi * digit
	inp_num //= 10

print("Сумма:", addi)
#print("Произведение:", multi)