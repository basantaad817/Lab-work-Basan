# apple evenly distribute

apple= int(input("enter number of apples\t"))
student= int(input("enter number of students\t"))

no_of_apple = apple//student
basket = apple%student

print("Each students get ", no_of_apple, "apples")
print("there are ", basket, " apples in the basket")