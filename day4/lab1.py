# Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.

year = int(input("Enter the year \t"))

if year%400 ==0 or (year%4 ==0 and year%100 !=0):
    print("The given year is leap year")
else:
    print("It is not leap year")