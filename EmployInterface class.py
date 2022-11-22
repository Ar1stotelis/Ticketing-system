#class EmployInterface
class EmployInterface:
    employ = Employ("EmployName", "EmployIdentifier", "EmployPhoneNumber", "EmployEmail", 0)
    
    def SetName(self, nameInput):
        self.employ.SetName(nameInput)
        
    def SetIdentifier(self, identifierInput):
        self.employ.SetIdentifier(identifierInput)

    def SetPhoneNumber(self, phoneNumberInput):
        self.employ.SetPhoneNumber((phoneNumberInput))

    def SetEmail(self, emailInput):
        self.employ.SetEmail(emailInput)

    def SetNumberOfTickets(self, numberOfTicketsInput):
        self.employ.SetNumberOfTickets(numberOfTicketsInput)

    #Getters -----

    def GetName(self):
        return self.employ.Getname()

    def GetIdentifier(self):
        return self.employ.GetIdentifier()

    def GetPhoneNumber(self):
        return self.employ.GetPhoneNumber()

    def GetEmail(self):
        return self.employ.GetEmail()

    def GetNumberOfTickets(self):
        return self.employ.GetNumberOfTickets()

    def To_String(self):
        return self.employ.To_String()
