

def is_non_neg_float(s):
    s = float(s)
    return (bool(s > 0.0))  
    
def get_non_neg_float(p):
    while is_non_neg_float(p) != True:
        p = input("Please enter a non-negative value in centimetres: ")
        is_non_neg_float(p)
    else:    
        return float(p)
    



def calculateArea():
    width = input ("What is the width you would like to enter in centimetres?")
    width = get_non_neg_float(width)
    
    
    height = input ("What is the height you would like to enter in centimetres?")
    height = get_non_neg_float(height)
    
    area = width * height
    print ("The calulated area = ", area, "cm squared!")

print("Welcome to the area calculator!")
print("The system will ask you to enter a chosen width and height in centimetres")
print("to calculate an area from the two values")

calculateArea()

















"""  while (height < 0):
        print ("Please enter a postive height in centremetres: ")
        height = input()
        height = float(width)
    return height"""
