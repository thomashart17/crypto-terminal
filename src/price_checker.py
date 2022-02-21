# Crypto Terminal: Price Checker
# Author: Thomas Hart

import console
import json
import price_scraper

# Gets cryptocurrency prices based on input parameters
#  - Compares to list of valid currencies in "data.json" file
#  - Option to use -s or -n tag to input symbols or names
#  - Option to use -t tag to check top currencies
def get_prices(ipt):
    frmt = "s"
    with open(f"{console.Console.PATH}data/settings.json", "r") as f:
        settings = json.load(f)
        currency = settings["currency"]
    top_status = False
    for i in range(1, len(ipt)):
        if ipt[i][0] == "-":
            if ipt[i][1] in ("n", "s"):
                frmt = ipt[i][1]
            elif ipt[i][1] == "t":
                top_status = True
                continue
            else:
                print(f"Invalid tag: \"{ipt[i][1]}\"")
        elif top_status:
            if i < len(ipt):
                for j in range(1, int(ipt[i]) + 1):
                    print(f"{j}. 1 {url_to_symbol(rank_to_url(str(j)))} = {price_scraper.get_price(rank_to_url(str(j)), currency)}")
            top_status = False
        else:
            if frmt == "n":
                if is_valid_crypto(ipt[i]):
                    print(f"1 {url_to_symbol(name_to_url(ipt[i].lower())).upper()} = {price_scraper.get_price(name_to_url(ipt[i]), currency)}")
                else:
                    print(f"Could not find \"{ipt[i]}\".")
                    print("Run \"update\" to get an updated list of cryptos.")
            elif frmt == "s":
                if is_valid_symbol(ipt[i]):
                    print(f"1 {ipt[i].upper()} = {price_scraper.get_price(symbol_to_url(ipt[i]), currency)}")
                else:
                    print(f"Could not find \"{ipt[i]}\".")
                    print("Run \"update\" to get an updated list of cryptos.") 

# Compares input symbol to list of valid symbols
def is_valid_symbol(symbol):
    with open(f"{console.Console.PATH}data/data.json", "r") as f:
        data = json.load(f)
        if symbol.upper() in data["symbols"]: 
            return True
    return False

# Converts symbol to corresponding URL value for Coin Gecko
def symbol_to_url(symbol):
    with open(f"{console.Console.PATH}data/data.json", "r") as f:
        data = json.load(f)
        return data["symbols"][symbol.upper()]

# Checks if input name is valid
def is_valid_crypto(crypto):
    with open(f"{console.Console.PATH}data/data.json", "r") as f:
        data = json.load(f)
        if crypto.lower() in data["cryptos"]: 
            return True
    return False

# Converts name to corresponding URL for Coin Gecko
def name_to_url(name):
    with open(f"{console.Console.PATH}data/data.json", "r") as f:
        data = json.load(f)
        return data["cryptos"][name.lower()]

# Converts URL from Coin Gecko into corresponding symbol
def url_to_symbol(url):
    with open(f"{console.Console.PATH}data/data.json", "r") as f:
        data = json.load(f)
        return data["urls"][url]

# Takes given rank and finds the corresponding URL
def rank_to_url(rank):
    with open(f"{console.Console.PATH}data/data.json", "r") as f:
        data = json.load(f)
        return data["ranks"][rank]