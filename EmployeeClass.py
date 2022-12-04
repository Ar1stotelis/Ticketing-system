# Needs a ticket member variable and the appropriate methods

# Employ class
class Employ:
    name = "EmployName"
    identifier = "EmployIdentifier"
    phone_number = "EmployPhoneNumber"
    email = "EmployEmail"
    number_of_tickets = 0

    def __init__(self, name, identifier, phone_number, email, number_of_tickets):
        self.name = name
        self.identifier = identifier
        self.phone_number = phone_number
        self.email = email
        self.number_of_tickets = number_of_tickets

    # Setters -----

    def set_name(self, name_input):
        self.name = name_input

    def set_identifier(self, identifier_input):
        self.identifier = identifier_input

    def set_phone_number(self, phone_number_input):
        self.phone_number = phone_number_input

    def set_email(self, email_input):
        self.email = email_input

    def set_number_of_tickets(self, number_of_tickets_input):
        self.number_of_tickets = number_of_tickets_input

    # Getters -----

    def get_name(self):
        return self.name

    def get_identifier(self):
        return self.identifier

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email

    def get_number_of_tickets(self):
        return self.number_of_tickets

    def to_string(self):
        return f"Name : {self.name}\nIdentifier : {self.identifier}\nPhone number : {self.phoneNumber}\nEmail : {self.email}\nNumber of Tickets : {self.numberOfTickets}\n"


# class EmployInterface
class EmployInterface:
    employ = Employ("EmployName", "EmployIdentifier", "EmployPhoneNumber", "EmployEmail", 0)

    def set_name(self, name_input):
        self.employ.set_name(name_input)

    def set_identifier(self, identifier_input):
        self.employ.set_identifier(identifier_input)

    def set_phone_number(self, phone_number_input):
        self.employ.set_phone_number((phone_number_input))

    def set_email(self, email_input):
        self.employ.set_email(email_input)

    def set_number_of_tickets(self, number_of_tickets_input):
        self.employ.set_number_of_tickets(number_of_tickets_input)

    # Getters -----

    def get_name(self):
        return self.employ.get_name()

    def get_identifier(self):
        return self.employ.get_identifier()

    def get_phone_number(self):
        return self.employ.get_phone_number()

    def get_email(self):
        return self.employ.get_email()

    def get_number_of_tickets(self):
        return self.employ.get_number_of_tickets()

    def to_string(self):
        return self.employ.to_string()
