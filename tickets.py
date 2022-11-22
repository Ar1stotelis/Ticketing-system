
class ticket:

    def __init__(self,ticketID,labels,description):
        self.ticketID = ticketID
        self.labels = labels
        self.description =description

    #Setters
    def setTicketID(self, ticketIDinput):
        self.ticketID = ticketIDinput

    def setLabels(self, labelsInput):
        self.labels = labelsInput

    def setDescription(self, descriptionInput):
        self.description = descriptionInput

    #Getters

    def getTicketID(self):
        print (self.ticketID)

    def getLabels(self):
       print (self.labels)

    def getDescription(self):
        print (self.description)