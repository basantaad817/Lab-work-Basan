# Take username and password from user and check it again for the three times whether the user has entered the right username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials for consecutive 3 times and if the limit exceeds than print "Attempt finished".


for a in range(3):
    user_name = str(input("Enter username \t"))
    password = int(input("Enter password \t"))

    if user_name=='basan' and password==1234:
        print("You are logged in")
        break
else:
    print("sorry, try again")