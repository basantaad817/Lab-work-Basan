# Write a Python program to construct the following pattern, using a nested for loop.

for i in range(6):
    print("* " * (i+1))
for w in range(6,0,-1):
    print("* " * (w-1))