import datetime

class ATM:
    def __init__(self):
        # Account Holder Details
        self.name = "Arun Gautam"
        self.account_number = "123456789"
        self.bank_name = "State Bank of India"
        self.dob = "01-01-2000"
        
        self.balance = 5000.0
        self.pin = 1234
        self.transaction_history = [] # Transaction file record

    def add_transaction(self, type, amount):
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        entry = f"{dt_string} | {type}: {amount} | Balance: {self.balance}"
        self.transaction_history.append(entry)

    def show_details(self):
        print("\n--- Account Holder Details ---")
        print(f"Name: {self.name}")
        print(f"Account No: {self.account_number}")
        print(f"Bank: {self.bank_name}")
        print(f"DOB: {self.dob}")

    def check_balance(self):
        print(f"\nAvailable Balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            print(f"Successfully deposited ₹{amount}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.add_transaction("Withdraw", amount)
            print(f"Successfully withdrawn ₹{amount}")
        else:
            print("Insufficient balance or invalid amount!")

    def mini_statement(self):
        print("\n--- Mini Statement (Last 3 Transactions) ---")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            # Last 3 transactions dikhane ke liye slice [-3:]
            for record in self.transaction_history[-3:]:
                print(record)

# --- Program Execution ---
atm_system = ATM()

print(f"Welcome to {atm_system.bank_name}")
entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == atm_system.pin:
    while True:
        print("\n1. Show Account Details")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Mini Statement")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            atm_system.show_details()
        elif choice == '2':
            atm_system.check_balance()
        elif choice == '3':
            amt = float(input("Enter deposit amount: "))
            atm_system.deposit(amt)
        elif choice == '4':
            amt = float(input("Enter withdrawal amount: "))
            atm_system.withdraw(amt)
        elif choice == '5':
            atm_system.mini_statement()
        elif choice == '6':
            print("Thank you for using our ATM. Have a nice day!")
            break
        else:
            print("Invalid choice, try again.")
else:
    print("Incorrect PIN! Access Denied.")