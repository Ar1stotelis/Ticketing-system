import glob
import random
import os


class Ticket:

    def __init__(self, labels, description):
        self.ticketID = random.randint(1111, 9999)
        self.labels = labels
        self.description = description

    # Setters
    def set_ticket_id(self, ticket_id_input):
        self.ticketID = ticket_id_input

    def set_labels(self, labels_input):
        self.labels = labels_input

    def set_description(self, description_input):
        self.description = description_input

    # Getters

    def get_ticket_id(self):
        print(self.ticketID)

    def get_labels(self):
        print(self.labels)

    def get_description(self):
        print(self.description)


# Method bellow checks the amount of tickets of an employee directory
def check_ticket_amount(employee):
    # Ticket path
    dir_path = f"{os.getcwd()}\\{employee}"

    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count


# The bellow method will count how many employee folders exist
def count_of_employees():
    i = 0

    for root, dirs, files in os.walk(os.getcwd()):
        i += root.count('Employee')
    return i


def creating_ticket_file(ticket_title, new_ticket, employee):
    # This method here is going to be used by create ticket multiple time
    # as such the code was put in this method to make the create_ticket method more readable
    dir_path = f"{os.getcwd()}\\{employee}"

    f = open(f"{dir_path}\\Ticket {ticket_title}.txt", 'w')
    f.write(f"TicketID: {new_ticket.ticketID} \n")
    f.close()

    f = open(f"{dir_path}\\Ticket {ticket_title}.txt", 'a')
    f.write(f"Description: {new_ticket.description} \n")
    f.close()

    f = open(f"{dir_path}\\Ticket {ticket_title}.txt", 'a')
    f.write(new_ticket.description)
    f.close()


def create_ticket():
    # user here is asked for the name of the file/ticket
    ticket_title = input("Please enter the ticket title: ")

    user_labels = input("Please enter the labels for the new ticket: ")
    ticket_description = input("Describe the problem: ")
    # Ticket object that will be put in a file
    new_ticket = Ticket(user_labels, ticket_description)
    # checking the amount of tickets each employee has
    employee1tickets = check_ticket_amount("employee1")
    employee2tickets = check_ticket_amount("employee2")

    if employee1tickets > employee2tickets:
        creating_ticket_file(ticket_title, new_ticket, "Employee2")
    elif employee2tickets > employee1tickets:
        creating_ticket_file(ticket_title, new_ticket, "Employee1")
    else:
        creating_ticket_file(ticket_title, new_ticket, "Employee1")


# Method that can be used to show all ticket text files within an employee directory
def show_tickets(employee):
    path_str = os.path.basename(" ".join(glob.glob(f"{employee}\\Ticket*.txt")))
    tickets = os.path.basename(path_str)

    print(tickets)


# This will go through all employee directories and return the file names
def show_all_tickets():
    for i in range(count_of_employees()):
        show_tickets(f"Employee{i + 1}")


def display_ticket(ticket):
    path_str = ""
    for i in range(count_of_employees()):
        path_str = " ".join(glob.glob(f"Employee{i + 1}\\{ticket}"))
        break

    print(path_str)

    with open(path_str, "r") as f:
        lines = f.readlines()
        print(str(lines) + '\n')


