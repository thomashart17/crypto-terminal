# Crypto Terminal: Console
# Author: Thomas Hart
# Created: February 2nd, 2022
# Modified: February 2nd, 2022

import crypto_scraper
import json
import price_checker
import price_scraper

class Console():

    def __init__(self):
        self.dir = "~"
        with open("settings.json", "r") as f:
            self.settings = json.load(f)
        self.currency = self.settings["currency"]

    def start(self):
        print(f"crypto-terminal:{self.dir}$ ", end = '')
        self.get_input()
    
    def get_input(self):
        ipt = input().strip().lower().split()
        if len(ipt) == 0:
            self.start()
        # elif ipt[0] == "cd":
        #     if len(ipt) == 1:
        #         self.change_dir("")
        #     else:
        #         self.change_dir(ipt[1])
        elif ipt[0] == "currency":
            if len(ipt) == 1:
                print(f"Current Currency: {self.currency}")
                self.start()
            else:
                self.change_currency(ipt[1])
        elif ipt[0] == "exit":
            exit()
        elif ipt[0] == "help":
            self.help()
        elif ipt[0] == "price":
            if price_checker.is_valid_symbol(ipt[1]):
                self.get_price(price_checker.symbol_to_url(ipt[1]))
            elif price_checker.is_valid_crypto(ipt[1]):
                self.get_price(price_checker.name_to_url(ipt[1]))
            else:
                print(f"Could not find \"{ipt[1]}\".")
                print("Run \"update\" to get an updated list of cryptos.")
                self.start()
        elif ipt[0] == "update":
            self.update()
        else:
            self.error(ipt[0])
    
    def change_currency(self, new_currency):
        self.currency = new_currency.upper()
        self.settings["currency"] = self.currency
        self.update_settings()
        self.start()
    
    # def change_dir(self, new_dir):

    #     if new_dir == "~" or new_dir == "" or new_dir == "~/":
    #         self.dir = "~"
    #     else:
    #         self.dir += new_dir
    #     self.start()

    def error(self, err):
        print(f"\"{err}\" is not a recognized command.")
        print("For a list of available commands, use \"help\".")
        self.start()
    
    def get_price(self, crypto):
        price = price_scraper.get_price(crypto, self.currency)
        print(f"Current Price: {price}")
        self.start()

    def help(self):
        with open ("help.txt") as f:
            for line in f:
                print(line, end = '')
            print()
        self.start()
    
    def update(self):
        crypto_scraper.update_json()
        self.start()
    
    def update_settings(self):
        with open("settings.json", "w") as f:
            json.dump(self.settings, f)