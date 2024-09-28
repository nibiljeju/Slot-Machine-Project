

import random

MIN_BET =1 
MAX_BET = 100
MAX_LINES = 3

ROWS= 3
COLS =3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}
    
def check_winnings(columns, lines, bet, values):
    winnings =0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = columns[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines +1)

    return winnings, winning_lines
            





def get_slot_machine(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column= []
        current_symbols = all_symbols
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
        
    return columns



def print_slotmachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


        
        
    



#function to collect users initial deposit amount as input
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break

            else:
                print("Please enter an amount greater than 0")

        else:
            print("Please enter a number.")   #handles not greater than 0 and gets them to try again


    return amount




def number_lines():
    while True:
        lines = input("How many lines would you like to bet on (1-" + str(MAX_LINES)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break

            else:
                print("Please enter a valid number of lines")

        else:
            print("Please enter a number.")   #handles not greater than 0 and gets them to try again


    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break

            else:
                print("amount must be between ${MIN_BET} - ${MAX_BET}.")

        else:
            print("Please enter a number.")   #handles not greater than 0 and gets them to try again


    return amount

def spin(balance):
    lines = number_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet* lines

        if total_bet > balance:
            print(f' You do not have enough to bet that amount, your current balance is: ${balance}')
        else:
            break
    
    print(f' You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')

    slots= get_slot_machine(ROWS, COLS, symbol_count)
    print_slotmachine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f' You won ${winnings}.')
    print(f' You won on lines:', *winning_lines)
    return winnings -total_bet






def main():
    balance =  deposit()
    while True:
        print(f' Current balance is ${balance}')
        answer = input ("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print (f" You left with ${balance}")
    

   



main()





          
       
