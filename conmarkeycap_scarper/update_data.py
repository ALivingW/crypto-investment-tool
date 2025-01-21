import json
from actual_stuff import find_closing_price


def update_data(symbol):
    try:
        with open(f'{symbol}.txt', 'r') as file:
            file_contents = json.load(file)

        data = file_contents[f'{symbol}_data'][0]
        data['7 days ago'] = data['6 days ago']
        data['6 days ago'] = data['5 days ago']
        data['5 days ago'] = data['4 days ago']
        data['4 days ago'] = data['3 days ago']
        data['3 days ago'] = data['Yesterday']
        data['Yesterday'] = data['Today']
        data['Today'] = find_closing_price(symbol)

        with open(f'{symbol}.txt', 'w') as file:
            json.dump(file_contents, file)

    except FileNotFoundError:
        print(f"File for {symbol} not found.")
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example call
# update_data('BTC')
