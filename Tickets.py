import random
import os


class Ticket:

    def __init__(self, labels, description):
        self.ticketID = random.randint(100000, 999999)
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
        return self.ticketID

    def get_labels(self):
        return self.labels

    def get_description(self):
        return self.description


class TicketInterface:
    ticket = Ticket("Null", "Description of the ticket")

    # setters for interface
    def set_ticket_id(self, ticket_id_input):
        self.ticket.set_ticket_id(ticket_id_input)

    def set_labels(self, labels_input):
        self.ticket.set_labels(labels_input)

    def set_description(self, description_input):
        self.ticket.set_description(description_input)

    # getters for interface
    def get_ticket_id(self):
        return self.ticket.get_ticket_id()

    def get_labels(self):
        self.ticket.get_labels()

    def get_description(self):
        self.ticket.get_description()


# All bellow methods are methods that will be used to control the files and folders for the tickets

# Method bellow checks the amount of tickets of an employee directory
def check_ticket_amount(employee):
    # Ticket path
    dir_path = f"{os.getcwd()}\\{employee}"

    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count


# Method that can be used to show all ticket text files within an employee directory
def show_tickets_by_employee(employee_num):
    try:
        for x in os.listdir(f"{os.getcwd()}\\Employee{employee_num}"):
            if x.endswith(".txt"):
                print(x)
    except FileNotFoundError as error:
        print(error)
        print("That employee could not be found, please try again")


# The bellow method will count how many employee folders exist
def count_of_employees():
    i = 0
    # counts directories with the name employee
    for root, dirs, files in os.walk(os.getcwd()):
        i += root.count('Employee')
    return i


# This will go through all employee directories and return the file names
def show_all_tickets():
    for i in range(count_of_employees()):
        show_tickets_by_employee(f"{i + 1}")


# This methods will go through to the ticket and print it out, you would just need the ticket name
# The folder of employee1 and employee 2 need to also be in the working directory
def display_specific_ticket(ticket):
    try:
        path = os.getcwd()
        # Here this part will search through the files and find the file with the name that is stored in ticket
        for root, directory, files in os.walk(path):
            if f"{ticket}.txt" in files:
                print(path)
                with open(f"{root}\\{ticket}.txt", "r") as f:
                    lines = f.readlines()
                    # Here the readlines() method will return an array
                    # For better user readability the bellow format is used
                    print(f"{lines[0]}{lines[1]}{lines[2]}")

    except FileNotFoundError as error:
        print(error)
        print("The ticket could not be found, check the spelling and try again")


# Ticket creation a storing inside of a file--------------------------------------------------------------
def creating_ticket_file(ticket_title, new_ticket, employee):
    # This method here is going to be used by the create_ticket() method bellow
    # as such the code was put in this method to make the create_ticket() method more readable
    # This method will take the ticket object and create a new text file and write the object in the file
    dir_path = f"{os.getcwd()}\\{employee}"

    f = open(f"{dir_path}\\{ticket_title}.txt", 'a')
    f.write(f"TicketID: {new_ticket.ticketID}")

    f.write(f"Labels: {new_ticket.labels}")

    f.write(f"Description: {new_ticket.description}")

    f.close()

def check_if_ticket_exists(ticket_name):
    for i in range(count_of_employees()):
        if os.path.isfile(f"Employee{i + 1}\\{ticket_name}.txt"):
            return True
            
# Creates text file of ticket depending on which employee has more tickets
def create_ticket():
    # user here is asked for the name of the file/ticket
    ticket_title = input("Please enter the ticket title: ")

    user_labels = input("Please enter the labels for the new ticket: ")
    ticket_description = input("Describe the problem: ")

    # Ticket object that will be written in a file
    new_ticket = Ticket(user_labels, ticket_description)

    # checking the amount of tickets each employee has
    employee1tickets = check_ticket_amount("employee1")
    employee2tickets = check_ticket_amount("employee2")

    if employee1tickets > employee2tickets:
        creating_ticket_file(ticket_title, new_ticket, "Employee2")
    else:
        creating_ticket_file(ticket_title, new_ticket, "Employee1")


# modifying the ticket -----------------------------------------------------
def modify_ticket(ticket):
    for root, directory, files in os.walk(os.getcwd()):
        if f"{ticket}.txt" in files:
            user_input = int(input("1: Change ticket name\n"
                                   "2: Change ticket labels\n"
                                   "3: Change ticket description\n"
                                   "Please select an option: "))
            if user_input == 1:
                new_name = input("Please enter the new ticket name: ")
                os.rename(f"{root}\\{ticket}.txt", f"{root}\\{new_name}.txt")
                print("Ticket has been renamed")

            elif user_input == 2:
                new_labels = input("Please enter new ticket labels: ")
                with open(f"{root}\\{ticket}.txt", "r+") as f:
                    lines = f.readlines()
                    lines[1] = f"Labels: {new_labels}"
                    print("Labels have been changed")

            elif user_input == 3:
                new_desc = input("Please enter new ticket description: ")
                with open(f"{root}\\{ticket}.txt", "w+") as f:
                    lines = f.readlines()
                    print (lines)
                    new_ticket = TicketInterface(lines[1], lines[2])
                    new_ticket.set_description(new_desc)

                    f.write(new_ticket.get_ticket_id())
                    f.write(new_ticket.get_labels())
                    f.write(new_ticket.get_description())

                    print("Description has been changed")
            else:
                print("Something went wrong, please try again")


# deletes ticket that is inputted by the user using the ticket name----------------------------------------------
def delete_ticket(ticket):
    try:
        path = os.getcwd()
        # Here this part will search through the files and find the file with the name that is stored in ticket
        for root, directory, files in os.walk(path):
            if f"{ticket}.txt" in files:
                user_choice = input(f"The ticket you will delete is{files}\n"
                                    f"are you sure you want to delete this ticket? "
                                    f"(input y for yes or n for no):")
                if user_choice.lower() == 'y':
                    os.remove(f"{root}\\{ticket}.txt")
                    print("The ticket has been successfully removed")
                elif user_choice.lower() == 'n':
                    print("Ticket has not been removed")
                else:
                    print("Something went wrong, please try again")

    except (FileNotFoundError, ValueError) as error:
        print(error)
        print("The ticket could not be found, check the spelling and try again")
