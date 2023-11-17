from cardHolder import cardHolder

def print_menu():
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit_amount = float(input("How much money would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit_amount)
        print("Thank you for your money. Your new balance is: ", str(cardHolder.get_balance()))
    except ValueError:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdrawal_amount = float(input("How much money would you like to withdraw: "))
        if cardHolder.get_balance() < withdrawal_amount:
            print("Insufficient balance :( ")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdrawal_amount)
            print("You're good to go! Thank you :) ")
    except ValueError:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("", 0, "", "", 0.0)

    list_of_cardHolders = [
        cardHolder("4343434343342", 1234, "John", "Griffth", 150.31),
        cardHolder("734343343342", 9999, "Khem", "Khanal", 150200.31),
        cardHolder("4343433343342", 4343, "Nil", "Panday", 150110.31),
        cardHolder("3343434343342", 4342, "Nirmal", "Khanal", 150010.31),
        cardHolder("5343434343342", 2343, "John", "Pandey", 1520.31)
    ]

    debit_card_num = ""
    while True:
        try:
            debit_card_num = input("Please insert your debit card: ")
            debit_match = [holder for holder in list_of_cardHolders if holder.get_cardNum() == debit_card_num]
            if len(debit_match) > 0:
                current_user = debit_match[0]
                break
            else:
                print("Card number not recognized. Please try again")
        except ValueError:
            print("Card number not recognized. Please try again")

    while True:
        try:
            user_pin = int(input("Please Enter your pin: ").strip())
            if current_user.get_pin() == user_pin:
                break
            else:
                print("Invalid PIN. Please try again.")
        except ValueError:
            print("Invalid PIN. Please try again.")

    print("Welcome, ", current_user.get_firstname(), ":)")
    option = 0
    while True:
        print_menu()
        try:
            option = int(input())
        except ValueError:
            print("Invalid input. Please try again")
        if option == 1:
            deposit(current_user)
        elif option == 2:
            withdraw(current_user)
        elif option == 3:
            check_balance(current_user)
        elif option == 4:
            break
        else:
            option = 0

    print("Thank you. Have a good day")
