#Needs a ticket member variable and the appropriate methods

#Employ class
class Employee:
    name = "EmployName"
    identifier = "EmployIdentifier"
    phoneNumber = "EmployPhoneNumber"
    email = "EmployEmail"
    numberOfTickets = 0

    def __init__(self, name, identifier, phoneNumber, email, numberOfTickets):
        self.name = name
        self.identifier = identifier
        self.phoneNumber = phoneNumber
        self.email = email
        self.numberOfTickets = numberOfTickets

    #Setters -----

    def SetName(self, nameInput):
        self.name = nameInput

    def SetIdentifier(self, identifierInput):
        self.identifier = identifierInput

    def SetPhoneNumber(self, phoneNumberInput):
        self.phoneNumber = phoneNumberInput

    def SetEmail(self, emailInput):
        self.email = emailInput

    def SetNumberOfTickets(self, numberOfTicketsInput):
        self.numberOfTickets = numberOfTicketsInput

    #Getters -----

    def GetName(self):
        return self.name

    def GetIdentifier(self):
        return self.identifier

    def GetPhoneNumber(self):
        return self.phoneNumber

    def GetEmail(self):
        return self.email

    def GetNumberOfTickets(self):
        return self.numberOfTickets

    def To_String(self):
        return f"Name : {self.name}\nIdentifier : {self.identifier}\nPhone number : {self.phoneNumber}\nEmail : {self.email}\nNumber of Tickets : {self.numberOfTickets}\n"

