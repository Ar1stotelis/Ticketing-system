from Tickets import *

if __name__ == "__main__":
    print("1. Manager")
    print("2. Employee")
    print("3. User")
    entity_input = int(0)
    try:
        entity_input = int(input("Who is using the software : "))
        while 1 > entity_input > 3:
            print("Error")
            print("Choose one of the following")
            entity_input = int(input("Who is using the software : "))

        if entity_input == 1:
            ticket_menu_for_manager()
        elif entity_input == 2:
            ticket_menu_for_employee()
        else:
            ticket_menu_for_user()

    except ValueError as error:
        print("Error")
        print("Invalid input")

