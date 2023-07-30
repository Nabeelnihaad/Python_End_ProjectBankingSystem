class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} units. Current balance: {self.balance}")
        else:
            print("Insufficient balance!")

# Creating a BankAccount instance
account = BankAccount("Nabeel1", "Nabeel2023")

# Logging in
def account_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if account.login(username, password):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Deposit funds
def deposit_funds():
    amount = float(input("Enter the amount to deposit: "))
    account.deposit(amount)

# Withdraw funds
def withdraw_funds():
    amount = float(input("Enter the amount to withdraw: "))
    account.withdraw(amount)

# Main program loop
def main():
    while True:
        print("\nWelcome to NPK Bank")
        print("1. Account Login")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            account_login()
        elif choice == 2:
            if account_login():
                deposit_funds()
        elif choice == 3:
            if account_login():
                withdraw_funds()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


main()
