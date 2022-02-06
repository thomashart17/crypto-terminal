# Crypto Terminal: Price Checker
# Author: Thomas Hart

import json
from locale import currency
import price_scraper

def get_prices(ipt):
    frmt = "s"
    with open("settings.json", "r") as f:
        settings = json.load(f)
        currency = settings["currency"]
    for i in range(1, len(ipt)):
        if ipt[i][0] == "-":
            if ipt[i][1] in ("n", "s"):
                frmt = ipt[i][1]
            else:
                print(f"Invalid tag: \"{ipt[i][1]}\"")
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

def is_valid_symbol(symbol):
    with open("data.json", "r") as f:
        data = json.load(f)
        if symbol.upper() in data["symbols"]: 
            return True
    return False

def symbol_to_url(symbol):
    with open("data.json", "r") as f:
        data = json.load(f)
        return data["symbols"][symbol.upper()]

def is_valid_crypto(crypto):
    with open("data.json", "r") as f:
        data = json.load(f)
        if crypto.lower() in data["cryptos"]: 
            return True
    return False

def name_to_url(name):
    with open("data.json", "r") as f:
        data = json.load(f)
        return data["cryptos"][name.lower()]

def url_to_symbol(url):
    with open("data.json", "r") as f:
        data = json.load(f)
        return data["urls"][url]