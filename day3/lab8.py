# sum of digit

number = int(input("Enter a number"))

sum = 0
for digit in str(number):
    sum += int(digit)
print("The sum  of number is ", sum)