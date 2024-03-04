import random

class bookInformation():
    title = ''
    author = ''
    year_published = 0
    ISBN = ''

    def __init__(self, title = '', author = '', year_published = 0):
        self.title = title
        self.author = author
        self.year_published = year_published

    def generateISBN(self):
        self.ISBN = random.randint(1000000000000,9999999999999)
                 
    def updateTitle (self, title):
        self.title = title

    def updateAuthor (self, author):
        self.author = author

    def updateYearPublished(self, year_published):
        self.year_published = year_published

    def printDetails(self):
        print ("Book Details:")
        print ("Title: ", self.title)
        print ("Author: ", self.author)
        print ("ISBN: ", self.ISBN)

book1 = bookInformation('To Kill a Mockingbird', 'Harper Lee', 1960)
book1.generateISBN()
book1.printDetails()

book2 = bookInformation('The Hobbit', 'J.R.R. Tolkien', 1937)
book2.generateISBN()
book2.printDetails()

book3 = bookInformation('Blood Sisters', 'Vanessa Lillie', 2023)
book3.generateISBN()
book3.printDetails()
