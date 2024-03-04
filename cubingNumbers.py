k = 1
total = 0

print("The program will now print the sum of cubes of the first n counting numbers. ")
#Promt the user to enter a value to print the sum of cubes up to
n = input("Please enter a value for n: ")
n = int(n)


for k in range(1,(n+1)):
    print (k," x ",k, " x ", k, " = ", k*k*k)
    total = total + (k*k*k)
    if total >= 100:
        break           #Breaks the code if the total is greater than 100

print ("The total sum of cubes for the first 50 counting numbers is: ", total)
