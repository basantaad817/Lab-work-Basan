# convert second into days, hours mins

second=int(input("Enter the seconds you want to convert"))

day= second/86400
hour = second/(24*60)
minute = second/24
 
print("day = ",day)
print("hour = ",hour)
print("minute = ",minute)