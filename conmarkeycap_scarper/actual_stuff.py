import requests


def find_closing_price(coin_symbol):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol': f'{coin_symbol}'}  # Replace with the desired cryptocurrency symbol
    headers = {'X-CMC_PRO_API_KEY': '22aa3a0b-7146-4b8d-81ff-92aafbbb5600'}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        closing_price = data['data'][f'{coin_symbol}']['quote']['USD']['price']
        print(f"Closing price of BTC: ${closing_price:.2f}")
        return closing_price
    else:
        print(f'Error fetching data. Status code: {response.status_code}')
