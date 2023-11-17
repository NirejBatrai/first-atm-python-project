class cardHolder:
    def __init__(self, cardNum, pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def get_cardNum(self):
        return self.cardNum

    def get_pin(self):
        return self.pin

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_balance(self):
        return self.balance

    def set_cardNum(self, new_val):
        self.cardNum = new_val

    def set_pin(self, new_val):
        self.pin = new_val

    def set_firstname(self, new_val):
        self.firstname = new_val

    def set_lastname(self, new_val):
        self.lastname = new_val

    def set_balance(self, new_val):
        self.balance = new_val

    def print_out(self):
        print("Card #:", self.cardNum)
        print("PIN:", self.pin)
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("Balance:", self.balance)
