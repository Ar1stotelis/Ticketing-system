import random
from labels import *


class Ticket:

    def __init__(self, ticket_labels, description):
        self.ticket_ID = random.randint(100000, 999999)
        self.labels = ticket_labels
        self.description = description

    # Setters
    def set_ticket_id(self, ticket_id_input):
        self.ticket_ID = ticket_id_input

    def set_labels(self, labels_input):
        self.labels = labels_input

    def set_description(self, description_input):
        self.description = description_input

    # Getters

    def get_ticket_id(self):
        return self.ticket_ID

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
                # Printing ticket, as can be seen the ticket would require all lines to be filled
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
    f.write(f"TicketID: {new_ticket.ticket_ID}\n")

    f.write(f"Labels: {new_ticket.labels}\n")

    f.write(f"Description: {new_ticket.description}\n")
    f.close()


def check_if_ticket_exists(ticket_name):
    for i in range(count_of_employees()):
        if os.path.isfile(f"Employee{i + 1}\\{ticket_name}.txt"):
            return True


# Creates text file of ticket depending on which employee has more tickets
def create_ticket():
    # user here is asked for the name of the file/ticket
    ticket_title = input("Please enter the ticket title: ")
    if check_if_ticket_exists(ticket_title):
        print("Name already exists, try again")
    elif ticket_title == "" or ticket_title == " " * len(ticket_title):
        print("Ticket title is required, try again")
    else:
        user_labels = ""
        labels_arr = load_data()
        num = 1
        # Printing labels for user to be able to see which number corresponds to which label
        for i in labels_arr:
            print(f"Enter {num} to put the label: {i}")
            num += 1

        user_input = int(input("Please input a number to select label or 0 to exit menu when finished: "))
        while user_input != 0:
            if user_input != 0:
                user_labels += f"{labels_arr[user_input - 1]}, "
                print(user_labels)
            user_input = int(input("Please input a number to select label or 0 to exit menu when finished: "))

        ticket_description = input("Describe the problem: ")
        if ticket_description == "" or ticket_description == " "* len(ticket_description):
            print("A description is required, please try again")
        else:
            # This needs to be this far into the if statements as to make sure that a
            # test file will not be created unless the fields are filled properly
            # Ticket object that will be written in a file
            new_ticket = Ticket(user_labels, ticket_description)
            # Giving employee with the least tickets the new ticket
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


def print_ticket_menu_manager():
    print(
        f"\n============================\n"
        f"1: Create a new ticket\n"
        f"2: See all tickets\n"
        f"3: Display ticket\n"
        f"4: Show all tickets of one employee\n"
        f"5: Modify ticket\n"
        f"6: Delete ticket\n"
        f"7: Label menu\n"
        f"0: close the menu"
        f"\n============================\n")


def ticket_menu_for_manager():
    print_ticket_menu_manager()
    user_input = int(input("Please enter your choice: "))
    while user_input != 0:
        try:
            if user_input == 1:
                create_ticket()

            elif user_input == 2:
                show_all_tickets()

            elif user_input == 3:
                ticket_to_display = input("Please type the name of the ticket you wish to see: ")
                display_specific_ticket(ticket_to_display)

            elif user_input == 4:
                employee_num = input("Please enter 1 for employee 1 or 2 for employee 2: ")
                show_tickets_by_employee(employee_num)

            elif user_input == 5:
                ticket_name = input("Please enter the name of the ticket to be modified: ")
                modify_ticket(ticket_name)

            elif user_input == 6:
                ticket_name = input("Please enter the name of the ticket to be deleted: ")
                delete_ticket(ticket_name)

            elif user_input == 7:
                if os.path.isfile("labels.pkl"):
                    labels_arr = load_data()
                    label_menu(labels_arr)
                else:
                    labels_arr = ["IT"]
                    label_menu(labels_arr)

            else:
                print("Non valid option")

            print_ticket_menu_manager()
            user_input = int(input("Please enter your choice: "))
        except ValueError as error:
            print(error)
            print("An error has occurred, please try again")


def print_ticket_menu_employee():
    print(
        f"\n============================\n"
        f"1: Create a new ticket\n"
        f"2: See all tickets\n"
        f"3: Display ticket\n"
        f"4: Delete ticket\n"
        f"0: close the menu"
        f"\n============================\n")


def ticket_menu_for_employee():
    print_ticket_menu_employee()
    user_input = int(input("Please enter your choice: "))
    while user_input != 0:
        try:
            if user_input == 1:
                create_ticket()

            elif user_input == 2:
                show_all_tickets()

            elif user_input == 3:
                ticket_to_display = input("Please type the name of the ticket you wish to see: ")
                display_specific_ticket(ticket_to_display)

            elif user_input == 4:
                ticket_name = input("Please enter the name of the ticket to be deleted: ")
                delete_ticket(ticket_name)

            else:
                print("Non valid option")

            print_ticket_menu_employee()
            user_input = int(input("Please enter your choice: "))
        except ValueError as error:
            print(error)
            print("An error has occurred, please try again")


def print_ticket_menu_user():
    print(
        f"\n============================\n"
        f"1: Create a new ticket\n"
        f"2: See all tickets\n"
        f"3: Display ticket\n"
        f"0: close the menu"
        f"\n============================\n")
    pass


def ticket_menu_for_user():
    print_ticket_menu_user()
    user_input = int(input("Please enter your choice: "))
    while user_input != 0:
        try:
            if user_input == 1:
                create_ticket()

            elif user_input == 2:
                show_all_tickets()

            elif user_input == 3:
                ticket_to_display = input("Please type the name of the ticket you wish to see: ")
                display_specific_ticket(ticket_to_display)

            else:
                print("Non valid option")

            print_ticket_menu_user()
            user_input = int(input("Please enter your choice: "))
        except ValueError as error:
            print(error)
            print("An error has occurred, please try again")
