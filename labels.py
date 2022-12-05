import pickle
import os


def add_label(arr):
    label_input = input("Please, enter the name of the new label :")
    arr.append(label_input)


def store_data(arr):
    with open('labels.pkl', 'wb') as f:
        pickle.dump(arr, f)


def load_data():
    with open('labels.pkl', 'rb') as f:
        loaded = pickle.load(f)
        return loaded


def print_menu():
    print(
        f"\n============================\n"
        f"1: see labels\n"
        f"2: add label\n"
        f"3: remove label\n"
        f"0: to exit"
        f"\n============================\n")
    pass


def label_menu(arr):

    print_menu()
    user_input = int(input("Please enter your choice: "))

    while user_input != 0:
        try:
            if user_input == 1:

                print(arr)

            elif user_input == 2:
                add_label(arr)
                store_data(arr)

            elif user_input == 3:
                to_remove = input("Please enter element to remove: ")
                arr.remove(to_remove)
                print("label has been removed")
                store_data(arr)

            else:
                print("Non valid option")

            print_menu()
            store_data(arr)
            user_input = int(input("Please enter your choice: "))

        except ValueError as error:
            print(error)
            print("An error has occurred, please try again")


if __name__ == "__main__":
    if os.path.isfile("labels.pkl"):
        labels = load_data()
        label_menu(labels)
    else:
        labels = ["IT"]
        label_menu(labels)
