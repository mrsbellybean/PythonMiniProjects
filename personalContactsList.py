class personalContactList():
    title = ''
    name = ''
    email = ''
    telephone = ''

    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def createContact(self, title, name, email, telephone): 
        self.title = title
        self.name = name
        self.email = email
        self.telephone = telephone

    def updateTitle(self, title):
        self.title = title

    def updateName(self, name):
        self.name = name

    def updateEmail(self, email):
        self.email = email

    def updateTelephone(self, telephone):
        self.telephone = telephone

    def printContact(self):
        print ("Contact Details:")
        print ("Title: ", self.title)
        print ("Name: ", self.name)
        print ("Email: ", self.email)
        print ("Telephone: ", self.telephone)

contact1 = personalContactList('Joe', 'joethom1@gmail.com')
contact1.updateTitle('Mr')
contact1.updateTelephone('123456789')
contact1.printContact()

