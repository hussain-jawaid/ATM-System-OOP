class BankAccounts:
    accounts = {}

    def __init__(self, username, pin, balance):
        self.display_name = username
        self.username = username.lower()
        self.pin = pin
        self.balance = balance

        if self.username not in BankAccounts.accounts:
            BankAccounts.accounts[self.username] = self
        else:
            print(f"The username '{self.display_name}' is already taken!")


class ATM(BankAccounts):
    def __init__(self):
        self.show_menu()

    def show_menu(self):
        while True:
            try:
                choice = int(input("\nWelcome! How would you like to proceed?\n"
                                   "1. Create a new account\n"
                                   "2. Deposit funds\n"
                                   "3. Withdraw funds\n"
                                   "4. Transfer funds\n"
                                   "5. Check balance\n"
                                   "6. Exit\n"
                                   "Enter your choice: "))
                options = {
                    1: self.create_account,
                    2: self.deposit,
                    3: self.withdraw,
                    4: self.transfer_money,
                    5: self.check_balance,
                    6: self.exit_atm
                }
                if choice in options:
                    options[choice]()
                else:
                    print("Invalid option. Please choose between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @classmethod
    def create_account(cls):
        while True:
            username = input("Enter a username: ").strip()
            if username.lower() not in cls.accounts:
                while True:
                    pin = input("Create a 4-digit PIN: ").strip()
                    if pin.isdigit() and len(pin) == 4:
                        try:
                            initial_deposit = int(input("Enter the initial deposit amount: "))
                            if initial_deposit >= 0:
                                BankAccounts(username, pin, initial_deposit)
                                print("Your account has been created successfully.")
                                return
                            else:
                                print("Initial deposit must be non-negative.")
                        except ValueError:
                            print("Please enter a valid amount.")
                    else:
                        print("Please enter a valid 4-digit PIN.")
            else:
                print(f"The username '{username}' is already taken!")

    @classmethod
    def deposit(cls):
        user = cls.authenticate_user()
        if user:
            try:
                amount = int(input("Enter the amount to deposit: "))
                if amount > 0:
                    user.balance += amount
                    print(f"${amount} has been deposited into {user.display_name}'s account.")
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid amount.")

    @classmethod
    def withdraw(cls):
        user = cls.authenticate_user()
        if user:
            try:
                amount = int(input("Enter the amount to withdraw: "))
                if 0 < amount <= user.balance:
                    user.balance -= amount
                    print(f"${amount} has been withdrawn from {user.display_name}'s account.")
                else:
                    print("Insufficient balance or invalid amount.")
            except ValueError:
                print("Invalid amount.")

    @classmethod
    def check_balance(cls):
        user = cls.authenticate_user()
        if user:
            print(f"{user.display_name}, your current balance is ${user.balance}.")

    @classmethod
    def transfer_money(cls):
        sender = cls.authenticate_user()
        if not sender:
            return

        try:
            amount = int(input("Enter the amount to transfer: "))
            if amount <= 0 or amount > sender.balance:
                print("Insufficient balance or invalid amount.")
                return
        except ValueError:
            print("Invalid amount.")
            return

        recipient_username = input("Enter the recipient's username: ").lower()
        if recipient_username == sender.username:
            print("You cannot transfer funds to yourself.")
            return

        recipient = cls.accounts.get(recipient_username)
        if recipient:
            sender.balance -= amount
            recipient.balance += amount
            print(f"${amount} has been transferred to '{recipient.display_name}'.")
        else:
            print("Recipient username not found.")

    @classmethod
    def authenticate_user(cls):
        username = input("\nEnter your username: ").lower()
        user = cls.accounts.get(username)
        if not user:
            print("Username not found.")
            return None
        pin = input("Enter your PIN: ").strip()
        if pin == user.pin:
            return user
        else:
            print("Incorrect PIN.")
            return None

    def exit_atm(self):
        print("Thank you for using our ATM. Goodbye!")
        exit()

# Start ATM session
if __name__ == "__main__":
    ATM()
