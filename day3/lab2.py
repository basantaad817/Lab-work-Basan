# WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 

sub1 = int(input("Enter the marks of sub1 \t"))
sub2 = int(input("Enter the marks of sub2 \t"))
sub3 = int(input("Enter the marks of sub3 \t"))
sub4 = int(input("Enter the marks of sub4 \t"))


total = sub1 + sub2 + sub3 + sub4

if total>400:
    print("sorry, you entered invalid marks")
else:
    percentage = (total*100)/400
    print("Your total marks is ",total)
    print("Your percentage is ",percentage)
    if percentage>70:
        print("You got distinction ")
    elif percentage > 60 and percentage<70:
        print("you got first division")
    elif percentage >40  and percentage<60:
        print("you got first division")
    else:
        print("sorry, you are fail")