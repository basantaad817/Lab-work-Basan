# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not. */

class_held = 100
class_attended = int(input("Enter the number of class held"))

attended_percent = (class_attended * 100)/class_held

if class_held < class_attended:
    print("Class held cant be less than class attended")
if attended_percent < 75:
    print("You can't attend the exam")
else:
    print("You can give exam")
