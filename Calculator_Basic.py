num1 = input("Enter First Number:")

num2 = input("Enter Second Number:")
oper = int(input("Select Operation: \n 1: ADD \n 2: SUBSTRACT \n 3: MULTIPLY \n 4: DIVIDE \n"))


if(oper == 1):
    result = float(num1) + float(num2)
    print("Sum of Both Numbers is:", result)

elif(oper == 2):
    result = float(num1) - float(num2)
    print("Substraction of Both Numbers is:", result)

elif(oper == 3):
    result = float(num1) * float(num2)
    print("Multiplication of Both Numbers is:", result)
elif(oper == 4):
    result = float(num1) / float(num2)
    print("Division of Both Numbers is:", result)

else:
    print("Enter correct input:")
'''result = int(num1)+int(num2)

print("Your Answer is:", result)
'''
