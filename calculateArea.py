
def getWidth():
    width = input ("What is the width you would like to enter in centimetres?")
    width = float(width)
    while (width < 0):
        print ("Please enter a postive width in centremetres: ")
        width = input()
        width = float(width)
    return width

def getHeight():
    height = input ("What is the height you would like to enter in centimetres?")
    height = float(height)
    while (height < 0):
        print ("Please enter a postive height in centremetres: ")
        height = input()
        height = float(width)
    return height

def calculateArea():
    width = getWidth()
    height = getHeight()
    area = width * height
    print ("The calulated area = ", area, "cm squared!")

print("Welcome to the area calculator! The system will ask you to enter a chosen width and height in centimetres")
print("to calculate an area from the two values")

calculateArea()
