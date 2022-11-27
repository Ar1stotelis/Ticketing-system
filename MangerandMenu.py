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



    
    
#MENU main programm

While True:

    print(' =================================')
    print('       CHOOSE AN OPTION \n')
    print('(type the first number of your choice')
    print(' =====================================')



    try:
        choice= input(' 1. CREATE A TICKET \n 2. STATUS OF THE TICKET \n ')
        choice= int(choice)
    except:
        print(' \n \n error, give me a numeric input please. \n')

    break

While True:
    
    match choice:
        case "1":
            #call the selected function
        case "2":
            #embedded condition in order to identify if the user has opened a ticket before
            while True:
                print(' ===================================')
                print('       STATUS OF YOUR TICKET \n')
                print('(type the first number of your choice')
                print('=====================================')

                try:
                    choice= input(' 1. MODIFY TICKET \n 2. DELETE TICKET \n ')
                    choice= int(choice)
                except:
                    print(' \n \n error, give me a numeric input please. \n')

                break


            
            #menu to choose if the user wants to modify the ticket or delete it
