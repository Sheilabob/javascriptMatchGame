from playsound import playsound
from colorama import init, Fore, Style
init(autoreset=True)

# task 4: banking


def show_balance(balance):
    format_balance = "{:.2f}".format(balance)
    print(f"Current balance:\t${format_balance}")
    print()


def deposit(balance):
    deposit = input("Enter amount to deposit:\t$")
    print()
    return (balance + float(deposit))


def withdraw(balance):
    withdraw = input("Enter amount to withdraw:\t$")
    print()
    new_balance = (balance - float(withdraw))
    if new_balance < 0:
        print(Fore.RED + Style.BRIGHT + "Insufficient funds.")
        playsound('insufficientFunds.mp3')
        return balance
    else:
        return new_balance


def logout(name):
    print(f"Goodbye, {name}!")
    print()
