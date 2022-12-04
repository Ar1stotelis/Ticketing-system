import Tickets.py


def print_ticket_menu():

    
    print(
        f"\n============================\n"
        f"1: Create a new ticket\n"
        f"2: See all tickets\n"
        f"3: Display ticket\n"
        f"4: Show all tickets of one employee\n"
        f"5: Modify ticket\n"
        f"6: Delete ticket\n"
        f"0: close the menu"
        f"\n============================\n")


def ticket_menu():
    print_ticket_menu()
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

            else:
                print("Non valid option")

            print_ticket_menu()
            user_input = int(input("Please enter your choice: "))
        except ValueError as error:
            print(error)
            print("An error has occurred, please try again")


if __name__ == "__main__":
    ticket_menu()
