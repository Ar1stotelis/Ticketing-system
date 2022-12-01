#class for the manager
class Heisenberg:
    name='MangerName'
    surname= 'ManagerSurname'
    

    def __init__(self, name, surname):
        self.name= name
        self.surname= surname
        
# +++SETTERS+++
    
    def SetName(self, newName):
        self.name = newName

    def SetSurname(self, newSurname):
        self.surname = newSurname   

# +++GETTERS+++
    def GetName(self):
        return self.name

    def GetSurname(self):
        return self.surname



#class for heisenberg {HeisenbergInterface}
class Manager:
    Manager = Manager("EmployName", "ManagerSurname")
    
    def SetName(self, nameInput):
        self.employ.SetName(nameInput)
    
    def SetSurname(self, SurnameInput):
        self.Manager.SetSurname(surnameInput)

    

    
    def GetName(self):
        return self.Manager.Getname()

    def GetSurname(self):
        return self.Manager.Surname()



    
