# Ask user to enter age, gender ( M or F ) and then using following rules print their place of service. if employee is female, then she will work only in urban areas.if employee is a male and age is in between 20 to 40 then he may work in anywhere if employee is male and age is in between 40 t0 60 then he will work in urban areas only.And any other input of age should print "ERROR".

age = int(input("Enter your age \t"))
gender = str(input("Type m for male and f for female"))

if gender == 'f':
    print("she will work in urban area")
elif gender == 'm' and age >20 and age<40:
    print("He can work anywhere")
elif gender == 'm' and age >40 and age<60:
    print("He will work in urban areas only")
else:
    print("error bhayo !!")
