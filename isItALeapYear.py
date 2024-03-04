my_year = input ("Please enter a year ")
my_year = int(my_year)

if ((my_year % 4 == 0) & (my_year % 100 != 0)) or (my_year % 400):
    print("The entered year is a leap year")

else :
    print ("The year is not a leap year")
    
