# Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.

num1 = int(input("Enter num1 \t"))
num2 = int(input("Enter num2 \t"))
num3 = int(input("Enter num3 \t"))

if num1 ==num2 or num2 ==num3 or num3 ==num1:
    print("you have type two number same")
else:
    print("The sum of given number = ",sum= num1 +num2 +num2)