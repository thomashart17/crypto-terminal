# Crypto Terminal: Price Checker
# Author: Thomas Hart

import console
import json
import pycoingecko

# Gets cryptocurrency prices based on input parameters
#  - Compares to list of valid currencies in "data.json" file
#  - Option to use -s or -n tag to input symbols or names
#  - Option to use -t tag to check top currencies
def get_prices(ipt):
    coin_gecko = pycoingecko.CoinGeckoAPI()
    frmt = "s"
    with open(f"{console.Console.PATH}/data/settings.json", "r") as f:
        settings = json.load(f)
        currency = settings["currency"]
    top_status = False
    for i in range(1, len(ipt)):
        if ipt[i][0] == "-":
            if ipt[i][1:] in ("n", "s"):
                frmt = ipt[i][1]
            elif ipt[i][1:] == "t":
                top_status = True
            else:
                print(f"Invalid tag: \"{ipt[i][1:]}\"")
        elif top_status:
            if i < len(ipt):
                try:
                    remaining = int(ipt[i])
                    if remaining < 1:
                        print("Minimum value of 1 required for \"price -t\"")
                    size = len(str(ipt[i])) + 1
                    rank = 1
                    while remaining > 0:
                        if remaining <= 250:
                            coins = coin_gecko.get_coins_markets(currency, per_page=ipt[i])
                        else:
                            coins = coin_gecko.get_coins_markets(currency, per_page=250)
                        for coin in coins:
                            symbol = coin["symbol"].upper()
                            price = coin["current_price"]
                            rank_str = str(rank) + "."
                            print((f"{rank_str:<{size}} 1 {symbol} = {price} {currency.upper()}"))
                            rank += 1
                        remaining -= 250
                except ValueError:
                    print(f"Invalid argument \"{ipt[i]}\" for \"price -t\"")
            top_status = False
        else:
            if frmt == "n":
                if is_valid_name(ipt[i]):
                    url = name_to_url(ipt[i])
                    price = coin_gecko.get_price(url, currency)[url][currency]
                    print(f"1 {name_to_symbol(ipt[i]).upper()} = {price} {currency.upper()}")
                else:
                    print(f"Could not find \"{ipt[i]}\".")
                    print("Run \"update\" to get an updated list of cryptos.")
            elif frmt == "s":
                if is_valid_symbol(ipt[i]):
                    url = symbol_to_url(ipt[i])
                    price = coin_gecko.get_price(url, currency)[url][currency]
                    print(f"1 {ipt[i].upper()} = {price} {currency.upper()}")
                else:
                    print(f"Could not find \"{ipt[i]}\".")
                    print("Run \"update\" to get an updated list of cryptos.") 

# Compares input symbol to list of valid symbols
def is_valid_symbol(symbol):
    with open(f"{console.Console.PATH}/data/data.json", "r") as f:
        data = json.load(f)
        if symbol.lower() in data["symbols"]: 
            return True
    return False

# Converts symbol to corresponding URL value for Coin Gecko
def symbol_to_url(symbol):
    with open(f"{console.Console.PATH}/data/data.json", "r") as f:
        data = json.load(f)
        return data["symbols"][symbol]

# Checks if input name is valid
def is_valid_name(name):
    with open(f"{console.Console.PATH}/data/data.json", "r") as f:
        data = json.load(f)
        if name.lower() in data["names"]: 
            return True
    return False

# Converts name to corresponding URL for Coin Gecko
def name_to_url(name):
    with open(f"{console.Console.PATH}/data/data.json", "r") as f:
        data = json.load(f)
        return data["names"][name.lower()]

# Converts name into corresponding symbol
def name_to_symbol(name):
    with open(f"{console.Console.PATH}/data/data.json", "r") as f:
        data = json.load(f)
        return data["urls"][data["names"][name.lower()]]

# Takes given rank and finds the corresponding URL
def rank_to_url(rank):
    with open(f"{console.Console.PATH}/data/data.json", "r") as f:
        data = json.load(f)
        return data["ranks"][rank]