# class for the manager
class Heisenberg:
    name = 'MangerName'
    surname = 'ManagerSurname'

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # +++SETTERS+++

    def set_name(self, new_name):
        self.name = new_name

    def set_surname(self, new_surname):
        self.surname = new_surname

    # +++GETTERS+++
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


# class for heisenberg {HeisenbergInterface}
class Manager:
    Manager = Manager("EmployName", "ManagerSurname")

    def set_name(self, name_input):
        self.employ.set_name(name_input)

    def set_surname(self, surname_input):
        self.Manager.set_surname(surname_input)

    def get_name(self):
        return self.Manager.get_name()

    def get_surname(self):
        return self.Manager.surname()
