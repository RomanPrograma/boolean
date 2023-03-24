
first_number = int(input("suggest a number 1   "))
second_number = int(input("suggest a number 2   "))
third_number = int(input("suggest a number 3   "))
value = int(input('\n 1-sum  2-product \n '))
if value ==1:
	print(first_number + second_number + third_number)
elif value ==2:
	print(first_number * second_number * third_number)
else :
	print("error, choose true value")
