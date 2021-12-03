# find BMI of a person where take mass and height as input from the user

# BMI=mass in kg / (height in m)2

mass= int(input("Enter the mass of body in kg\t"))
height = int(input("Enter the height of body in meter\t"))

bmi= mass/(height *height)

print("The body mass index of given data is ",bmi, "kg/m\u00b2")