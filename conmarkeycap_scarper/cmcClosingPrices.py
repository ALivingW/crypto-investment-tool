import json
from threading import Thread
from actual_stuff import find_closing_price
from update_data import update_data

num = -1
old_file = []

with open('coin_names.txt', 'r') as file:
    lines = file.readlines()
    # This will return [BTC, ETH, DOGE] assuming the file has these symbols each on a new line


for symbol in lines:
    num += 1
    symbol = symbol.rstrip()
    file = open(f'{symbol}.txt', 'r')
    file_contents = file.read()
    file.close()
    old_file.append(file_contents)
    update_data(symbol)


def ask_update():
    update_choice = input('Would You Like To Update The Closing Price Data? ')
    if update_choice.lower() == 'yes':
        pass
    elif update_choice.lower() == 'no':
        global num
        global old_file

        with open('coin_names.txt', 'r') as file:
            lines = file.readlines()
            list(lines)
            lines.reverse()
        num += 1
        for symbol in lines:
            num -= 1
            symbol = symbol.rstrip()
            file = open(f'{symbol}.txt', 'w')
            file.write(old_file[num])
            file.close()


ask_update = Thread(target=ask_update)
ask_update.start()
ask_update.join(timeout=180)

def ask_new_coins():
    new_coins = ''
    symbols = []
    while new_coins != 'QUIT':
        new_coins = input('''
    Enter a new coin that you want to see the closing price of, if you don\'t want to add any coins, enter 'QUIT' : ''')
        if new_coins != 'QUIT':
            symbols.append(new_coins)
            with open('coin_names.txt', 'a') as file:
                for symbol in symbols:
                    file.write('\n' + symbol)


ask_coins = Thread(target=ask_new_coins)
ask_coins.start()
ask_coins.join(timeout=180)


with open('coin_names.txt', 'r') as file:
    lines = file.readlines()

for symbol in lines:
    symbol = symbol.rstrip()  # Remove any extra whitespace/newline characters
    try:
        with open(f'{symbol}.txt', 'r') as file:
            file_contents = json.load(file)
            closing_prices = file_contents[f'{symbol}_data']
            for entry in closing_prices:
                print(f'\n{symbol} Data-')
                for key, value in entry.items():
                    print(f'{key} : {value}')

    except FileNotFoundError:
        closing_price = find_closing_price(symbol)
        creation = {
            f'{symbol}_data': [
                {
                    'Today': f'{closing_price}',
                    'Yesterday': '',
                    '3 days ago': '',
                    '4 days ago': '',
                    '5 days ago': '',
                    '6 days ago': '',
                    '7 days ago': ''
                },
            ]
        }
        with open(f"{symbol}.txt", "w") as file:
            json.dump(creation, file)
