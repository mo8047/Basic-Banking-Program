

def show_balance():
    print(balance)

def deposit():
    global balance
    u_deposit = int(input("How much would you like to deposit: "))
    if u_deposit <= 0:
        print("Please enter a valid amount. ")
        return 0
    else:
        balance += u_deposit
        print(f"You're current balance is: {balance}")
        return balance

def withdraw():
    global balance
    u_withdraw = int(input("How much would you like to withdraw: "))
    if u_withdraw > balance:
        print("Your withdrawal amount exceeds your balance, please try again.")
        return 0
    elif u_withdraw <= balance:
        balance -= u_withdraw
        print(f"You're balance after the withdrawal is {balance}")
        return balance
def main():
    global balance
    balance = 0
    is_running = True

    while is_running:
        print('''Banking Program
                    1. Show Balance: 
                    2. Deposit: 
                    3. Withdraw:
                    4: Exit. ''')
        u_input = input("Enter what program would you like to proceed with: ")
        if u_input == "1":
            show_balance()
        elif u_input == "2":
            deposit()
        elif u_input == "3":
            withdraw()
        else:
            print("Thank you for using our services.")
            exit()

if __name__ == '__main__':
    main()

