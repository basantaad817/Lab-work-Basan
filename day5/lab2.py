# Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)

opt= str(input("Press c to convert celsius and f to convert fahrenheit"))
converted =0
if opt =='c':
    celsius = int(input("Enter temperature in celsius"))
    converted = (celsius*1.8)+32
    print(converted)
else:
    fahren = int(input("enter temperature in fahrenheit"))
    converted = (fahren -32)/1.8
    print(converted)