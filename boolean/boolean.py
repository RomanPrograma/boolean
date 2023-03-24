
first_number = int(input("suggest a number 1   "))
second_number = int(input("suggest a number 2   "))
value = int(input('\n 1-sum \n 2-difference \n 3-arithmetic mean \n 4-product \n '))
if value ==1:
	print(first_number + second_number)
elif value ==2:
	print(first_number - second_number)
elif value ==3:
	print((first_number + second_number)/2)
elif value ==4:
	print(first_number * second_number)
else :
	print("error, choose true value")
