k = 1
total = 0

print("The program will now print the sum of squares of the first 50 counting numbers. ")

for k in range(1,51):
    print (k," x ",k, " = ", k*k)
    total = total + (k*k)

print ("The total sum of squares for the first 50 counting numbers is: ", total)
