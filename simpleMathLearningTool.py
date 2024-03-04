import random
number1 = random.randint(1,9)
number2 = random.randint(1,9)

print ("What is ", number1, " + ", number2, "? ")
studentAnswer = input()
studentAnswer = int(studentAnswer)

if studentAnswer == (number1 + number2):
    print ("Your answer is correct!!")

else:
    print ("Your answer is incorrect.");
    
