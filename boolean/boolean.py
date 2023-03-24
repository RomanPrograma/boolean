first_number = int(input("suggest a number 1   "))
second_number = int(input("suggest a number 2   "))
third_number = int(input("suggest a number 3   "))
value = int(input("1-maximum of three \n2-minimum of three \n3-arithmetic mean of three \n"))
if value ==1:
    if first_number > second_number > third_number:
        print(first_number)
    elif second_number > third_number > first_number:
        print(second_number)
    elif third_number > second_number > first_number:
        print(third_number)
elif value ==2:
    if first_number < second_number < third_number:
        print(first_number)
    elif second_number < first_number < third_number:
        print(second_number)
    elif third_number < first_number < second_number:
        print(third_number)
elif value ==3:
    print((first_number + second_number + third_number) / 3)
else:
    print("err")