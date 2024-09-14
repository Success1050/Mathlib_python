import random

symbols= ["🌕", "🍎", "🍌", "🍒", "🚒", "🥣"]

points_for_same_rows= 10
points_for_same_cols= 10
points_for_diagonals= 10


def deposite():
    while True:
        amount= input("Enter the amount you want to deposite?:$")
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("deposite must be greater than 0")
        else:
            print("Enter a valid number")
    return amount

def spin():
    items= [[random.choice(symbols) for _ in range(3)] for _ in range(3)]
    # print(items)
    return items

def display_slots(spin_result):
    for row in spin_result:
        print(f"| {' | '.join(row)} |")


def check_winnings(spin_result, balance, bet):
    for i, row in enumerate(spin_result):
        if row[0] == row[1] == row[2]:
            print(f"you won on Row{i + 1} which is {row}")
            balance += points_for_same_rows * bet
            print(f"${points_for_same_rows * bet} has been added to your balance, current balance is {balance}")
            return True
            
    for cols in range(3):
        if spin_result[0][cols] == spin_result[1][cols] == spin_result[2][cols]:
            print(f"you won on column {cols + 1} which is {[spin_result[0][cols], spin_result[1][cols], spin_result[2][cols]]}")
            balance += points_for_same_cols * bet
            print(f"${points_for_same_rows * bet}, current balance is ${balance}")
            return True

    for i in range(3):
        if spin_result[0][0] == spin_result[1][1] == spin_result[2][2]:
            print(f"you won on diagonal {i + 1} which is {[spin_result[0][0], spin_result[1][1], spin_result[2][2]]}")
            balance += points_for_same_cols * bet
            print(f"${points_for_same_cols * bet} ,current balance is ${balance}")
            return True

        if spin_result[0][2] == spin_result[1][1] == spin_result[2][0]:
            print(f"you won on diagonal {i + 1} which is {[spin_result[2][0], spin_result[1][1], spin_result[0][2]]}")
            balance += points_for_same_cols * bet
            print(f"${points_for_same_cols * bet}, current balance is ${balance}")
            return True


# def want_to_continue(spin_result, balance, bet):
#     while True:
#         if check_winnings(spin_result, balance, bet):
#             statement= input("do you want to continue?yes/no ")
#             if statement.islower() == "no":
#                 break

def get_bets():
    while True:
        bets = input(F"how much would you like to bet? $")
        if bets.isdigit():
            bets= int(bets)
            if bets > 0:
                break
            else:
                print("your betting amount should be more than 0 dollars")
        else:
            print("Please enter a valid amount of bet")
    return bets


def start_slot_machine(balance, bet):
    input("Press Enter to start the slot machine")
    result= spin()
    print(f"current balance {balance}")
    display_slots(result)
    check_winnings(result, balance,bet)
    # while True:
    #     if check_winnings(result, balance,bet):
    #         statement= input("do you want to continue?yes/no ")
    #         if statement.islower() == "no":
    #             break

def main():
    amount = deposite()
    while True:
        bet = get_bets()
        if bet < amount:
            amount -= bet
            start_slot_machine(amount, bet)
            # check_winnings(spin())

        else: 
            print(f"your balance is too low to bet. your current balance is {amount}")
        
main()




