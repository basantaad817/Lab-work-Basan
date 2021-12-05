# Given a positive real number, print its fractional part. 

import math

a = float(input("Enter the number \t"))

b,c = math.modf(a)

print("the first part is ",c )
print("the second part is ",b )