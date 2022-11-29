import random


class Ticket:

    def __init__(self, labels, description):
        self.ticketID = random.randint(1111, 9999)
        self.labels = labels
        self.description = description

    # Setters
    def setTicketID(self, ticketIDinput):
        self.ticketID = ticketIDinput

    def setLabels(self, labelsInput):
        self.labels = labelsInput

    def setDescription(self, descriptionInput):
        self.description = descriptionInput

    # Getters

    def getTicketID(self):
        print(self.ticketID)

    def getLabels(self):
        print(self.labels)

    def getDescription(self):
        print(self.description)


def createticket():
    # user here is asked for the name of the file/ticket
    ticketTitle = input("Please enter the ticket title: ")

    userlabels = input("Please enter the labels for the new ticket: ")
    ticketDescription = input("Describe the problem: ")
    # Ticket object that will be put in a file
    newTicket = Ticket(userlabels, ticketDescription)

    f = open(f"{ticketTitle}.txt", 'w')
    f.write(newTicket.labels + "\n")
    f.close()

    f = open(f"{ticketTitle}.txt", 'a')
    f.write(newTicket.description)
    f.close()


class TicketFunctions:

    def showalltickets
