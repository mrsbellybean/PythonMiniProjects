import random

systemNumber = random.randint(0,101)
print (systemNumber)


for x in range (50):

    userNumber = input("Please guess the number that the system has generated... ")
    userNumber =int(userNumber)
    
    if userNumber < systemNumber:
        print("Too low, guess again... ")
    elif userNumber > systemNumber:
        print("Too high! guess again... ")
    else:
        print("Congratulations, you guessed it correctl ")
        break
