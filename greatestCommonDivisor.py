i = 0

print("Welcome to the greatest common divisor program!!!")
print("Please enter two numbers to find their greatest common divisor")
n1 = input("Please enter your first number: ")
n1 = int(n1)
n2 = input("Please enter your second number: ")
n2 = int(n2)

if n1<n2:
    for i in range(n1, 0, -1):
        if (n1 % i == 0) and (n2 % i == 0):
            print("The greatest common divisor is: ", i)
            break
        else:
            continue

elif n2<n1:
    for i in range(n2, 0, -1):
        if (n1 % i == 0) and (n2 % i == 0):
            print("The greatest common divisor is: ", i)
            break
        else:
            continue
else:
    for i in range(n2, 0, -1):
        if (n1 % i == 0) and (n2 % i == 0):
            print("The greatest common divisor is: ", i)
            break
        else:
            continue
