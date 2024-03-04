my_number = input("Please enter a number ")
my_number = int(my_number)

if (my_number % 2 == 0) & (my_number > 5):
    print ("The number is divisible by 2 and greater than 5")

elif (my_number % 2 == 0) or (my_number > 5):
    print ("The number is either divisible by 2 or greater than 5")

else:
    print ("The number is neither divisible 2 nor greater than 5")
