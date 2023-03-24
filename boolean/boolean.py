number_of_meters = int(input("number_of_meters   "))
value = float(input("1-convert to miles \n2-convert to inches \n3-convert to yards \n"))
if value ==1:
    print(number_of_meters*0.000621371)
elif value ==2:
    print(number_of_meters*39.370)
elif value ==3:
    print(number_of_meters*39.370)
else:
    print("err")