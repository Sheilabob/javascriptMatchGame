from banking_pkg import account
from colorama import init, Fore, Style
init(autoreset=True)

# Functions


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Task 2 - register user


print("          === Automated Teller Machine ===          ")
while True:
    name = input("Enter name to register: ")
    if len(name) > 10:
        print(Fore.RED + Style.BRIGHT + "The maximum length is 10 characters.")
        continue
    elif len(name) == 0:
        print(Fore.RED + Style.BRIGHT + "You must enter a name.")
        continue
    else:
        break

while True:
    pin = input("Enter PIN: ")
    if len(pin) > 4 or len(pin) < 4:
        print(Fore.RED + Style.BRIGHT + "PIN must contain 4 numbers")
        continue
    else:
        break

balance = 0

print(Fore.GREEN + Style.BRIGHT +
      f"{name} has been registered with a starting balance of ${str(balance)}")

# Task 3 - log in and menu
# part a - login

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter Name:\t")
    pin_to_validate = input("Enter PIN:\t")
    if name_to_validate == name and pin_to_validate == pin:
        print(Fore.GREEN + Style.BRIGHT + "Login successful!")
        print()
        break
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid Credentials")
        print()
        continue

# part b - menu
while True:
    atm_menu(name)
    option = input("Choose an option:\t")
    # Task 5 - using banking functions
    if option == "1":
        print()
        account.show_balance(balance)
    elif option == "2":
        print()
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        print()
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        print()
        account.logout(name)
        break
