# MENU main programm

While
True:

print(' =================================')
print('       CHOOSE AN OPTION \n')
print('(type the first number of your choice')
print(' =====================================')

try:
    choice = input(' 1. CREATE A TICKET \n 2. STATUS OF THE TICKET \n ')
    choice = int(choice)
except:
    print(' \n \n error, give me a numeric input please. \n')

break

While
True:

match choice:
    case "1":
    # call the selected function

    case "2":
        # embedded condition in order to identify if the user has opened a ticket before
        while True:
            print(' ===================================')
            print('       STATUS OF YOUR TICKET \n')
            print('(type the first number of your choice')
            print('=====================================')

            try:
                choice = input(' 1. MODIFY TICKET \n 2. DELETE TICKET \n ')
                choice = int(choice)
            except:
                print(' \n \n error, give me a numeric input please. \n')

            break

        # menu to choose if the user wants to modify the ticket or delete it