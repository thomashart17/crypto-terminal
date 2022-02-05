# Crypto Terminal: Price Checker
# Author: Thomas Hart

import json

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
        return data["cryptos"][name.upper()]