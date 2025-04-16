class ATM:
    def __init__(self, balance):
        self.__balance = balance
        self.__pin = 0

    def create_pin(self):
        pin_flag = True
        while pin_flag:
            try:
                pin = int(input("Create your PIN (must be a four-digit number): "))
                if pin > 0 and len(str(pin)) == 4 and pin != self.__pin:
                    self.__pin = pin
                    print("Your PIN has been created.")
                    pin_flag = False
                else:
                    print("Please enter a four-digit PIN (must be different from previous)!")
            except ValueError:
                print("Please enter a four-digit PIN (letters not allowed)!")

    def deposit(self):
        deposit_flag = True
        while deposit_flag:
            try:
                pin = int(input("Enter your PIN: "))
                if pin > 0 and pin == self.__pin:
                    print(f"Balance: ${self.__balance}")
                    amount = float(input("Enter the amount to deposit: "))
                    if amount > 0:
                        self.__balance += amount
                        print(f"${amount} has been deposited into your account.")
                        deposit_flag = False
                    else:
                        print("Amount must be positive!")
                else:
                    print("You entered an incorrect PIN. Please try again.")
            except ValueError:
                print("Please enter a four-digit PIN (letters not allowed)!")

    def withdraw(self):
        withdraw_flag = True
        while withdraw_flag:
            try:
                pin = int(input("Enter your PIN: "))
                if pin > 0 and pin == self.__pin:
                    print(f"\nBalance: ${self.__balance}.")
                    amount = float(input("Enter the amount to withdraw: "))
                    if amount <= self.__balance and amount > 0:
                        self.__balance -= amount
                        print(f"${amount} has been withdrawn from your account.")
                        withdraw_flag = False
                    else:
                        print("Amount must be positive and not exceed your current balance!")
                else:
                    print("You entered an incorrect PIN. Please try again.")
            except ValueError:
                print("Please enter a four-digit PIN (letters not allowed)!")

    def check_balance(self):
        balance_flag = True
        while balance_flag:
            try:
                pin = int(input("Enter your PIN: "))
                if pin == self.__pin:
                    print(f"Your current balance is ${self.__balance}.")
                    balance_flag = False
                else:
                    print("You entered an incorrect PIN. Please try again.")
            except ValueError:
                print("Please enter a four-digit PIN (letters not allowed)!")

    def menu(self):
        flag = True
        while flag:
            print("\nHello, how would you like to proceed?")
            print("1. Enter 1 to create a PIN\n"
                  "2. Enter 2 to deposit\n"
                  "3. Enter 3 to withdraw\n"
                  "4. Enter 4 to check balance\n"
                  "5. Enter 5 to exit\n")
            try:
                option = int(input("Choose an option: "))
                if option == 1:
                    self.create_pin()
                elif option == 2:
                    self.deposit()
                elif option == 3:
                    self.withdraw()
                elif option == 4:
                    self.check_balance()
                elif option == 5:
                    flag = False
                else:
                    print("Invalid option. Please choose a number between 1 and 5.")
            except ValueError:
                print("Please choose a valid option!")

if __name__ == '__main__':
    hbl = ATM(1000)
    hbl.menu()
    
