import random

lotteryNumber1 = random.randint(1,5)
lotteryNumber2 = random.randint(1,5)
lotteryNumber3 = random.randint(1,5)

print("Welcome to the lottery!")
print ("Lottery number was :", lotteryNumber1, lotteryNumber2, lotteryNumber3)
print ("Please enter three digits: ")
userNumber1 = int(input("First number: "))
userNumber2 = int(input("Second number: "))
userNumber3 = int(input("Third number: "))

print ("Lottery number was :", lotteryNumber1, lotteryNumber2, lotteryNumber3)

#Single number win
print ("Lottery number was :", lotteryNumber1, lotteryNumber2, lotteryNumber3)
if (userNumber1 == lotteryNumber1) or (userNumber1 == lotteryNumber2) or (userNumber1 == lotteryNumber3):
    print("You have won £1000! ")
elif (userNumber2 == lotteryNumber1) or (userNumber2 == lotteryNumber2) or (userNumber2 == lotteryNumber3):
    print("You have won £1000! ")
elif (userNumber3 == lotteryNumber1) or (userNumber3 == lotteryNumber2) or (userNumber3 == lotteryNumber3):
    print("You have won £1000! ")

else:
    print("You lost :( ")



#Double number win
if ((userNumber1 == lotteryNumber1) or (userNumber1 == lotteryNumber2) or (userNumber1 == lotteryNumber3)) and ((userNumber2 == lotteryNumber1) or (userNumber2 == lotteryNumber2) or (userNumber2 == lotteryNumber3)):
    print("You have won £5000! ")
    if (userNumber1 == lotteryNumber1) and (userNumber2 == lotteryNumber2):
        print("You got the first two digits in the correct order, you have won £10,000! ")
    else:
        print("Wah")
        
elif ((userNumber1 == lotteryNumber1) or (userNumber1 == lotteryNumber2) or (userNumber1 == lotteryNumber3)) and ((userNumber3 == lotteryNumber1) or (userNumber3 == lotteryNumber2) or (userNumber3 == lotteryNumber3)):
    print("You have won £5000! ")
elif ((userNumber2 == lotteryNumber1) or (userNumber2 == lotteryNumber2) or (userNumber2 == lotteryNumber3)) and ((userNumber3 == lotteryNumber1) or (userNumber3 == lotteryNumber2) or (userNumber3 == lotteryNumber3)):
    print("You have won £5000! ")
    if (userNumber2 == lotteryNumber2) or (userNumber3 == lotteryNumber3):
        print("You got the second two digits in the correct order, you have won £10,000! ")
    else:
        print("Wah")
else:
    print("Sorry you didn't get a double digit win :( ")

    
#Triple number win
if ((userNumber1 == lotteryNumber1) or (userNumber1 == lotteryNumber2) or (userNumber1 == lotteryNumber3)) and ((userNumber2 == lotteryNumber1) or (userNumber2 == lotteryNumber2) or (userNumber2 == lotteryNumber3)) and ((userNumber3 == lotteryNumber1) or (userNumber3 == lotteryNumber2) or (userNumber3 == lotteryNumber3)):
    print("You have won £10,000! ")
    if (userNumber1 == lotteryNumber1) and (userNumber2 == lotteryNumber2) and (userNumber3 == lotteryNumber3):
        print("You got them all in the right order, you won £20,000!!!!!!!! Woop woop!!!!!!! ")
    else:
        print("Not in the exact order though! ")
        
else:
    print("Sorry you didn't get a triple digit win :( ")




    
