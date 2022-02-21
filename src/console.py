# Crypto Terminal: Console
# Author: Thomas Hart

import crypto_scraper
import json
import miner_scraper
import price_checker
import re

# Main class representing the console that runs the entire terminal
class Console():

    # Update to location of directory before use
    PATH = "C:/Users/Thomas Hart/Documents/crypto-terminal/"

    # Initializes member variables to defaults or values saved in JSON
    def __init__(self):
        self.dir = "~"
        with open(f"{self.PATH}data/settings.json", "r") as f:
            self.settings = json.load(f)
        self.currency = self.settings["currency"]
        self.electricity = self.settings["electricity"]

    # Creates a new terminal line to take in commands
    def start(self):
        print(f"crypto-terminal:{self.dir}$ ", end = '')
        self.get_input()
    
    # Reads inputted command and calls corresponding function
    def get_input(self):
        ipt = re.findall(r"[^\"\s]\S*|\".+?\"", input().strip().lower())
        for i in range(len(ipt)):
            if ipt[i][0] == '"' and ipt[i][-1] == '"':
                ipt[i] = ipt[i][1:-1]
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
        elif ipt[0] == "electricity":
            if len(ipt) == 1:
                print(f"Current Electricity Costs: {self.electricity} {self.currency}/kWh")
                self.start()
            else: 
                self.change_electricity(ipt[1])
        elif ipt[0] == "exit":
            exit()
        elif ipt[0] == "help":
            self.help()
        elif ipt[0] == "miners":
            if len(ipt) <= 1:
                print("No argument specified for \"miners\"")
            else:
                miner_scraper.scrape_miners(ipt[1], self.currency, self.electricity)
            self.start()
        elif ipt[0] == "price":
            if len(ipt) <= 1:
                print("No argument specified for \"price\"")
            else:
                price_checker.get_prices(ipt)
            self.start()
        elif ipt[0] == "update":
            self.update()
        else:
            self.error(ipt[0])
    
    # Changes currency prices will be displayed in and updates settings in JSON
    def change_currency(self, new_currency):
        self.currency = new_currency.upper()
        self.settings["currency"] = self.currency
        self.update_settings()
        self.start()
    
    # Changes directory in which the terminal is operating
    #  - Will be implemented after feature to save output to files
    # def change_dir(self, new_dir):
    #     if new_dir == "~" or new_dir == "" or new_dir == "~/":
    #         self.dir = "~"
    #     else:
    #         self.dir += new_dir
    #     self.start()

    # Changes electricity cost that will be used in profitability calculations and updates setting in JSON
    def change_electricity(self, new_electricity):
        self.electricity = new_electricity
        self.settings["electricity"] = self.electricity
        self.update_settings()
        self.start()

    # Error message for when an invalid command is entered
    def error(self, err):
        print(f"\"{err}\" is not a recognized command.")
        print("For a list of available commands, use \"help\".")
        self.start()

    # Displays list of available commands from "help.txt" file
    def help(self):
        # TODO: Add description for each command in "help.txt"
        with open (f"{self.PATH}data/help.txt") as f:
            for line in f:
                print(line, end = '')
            print()
        self.start()
    
    # Updates list of available cryptocurrencies and corresponding symbols
    # TODO: Allow updates for individual lists of values
    def update(self):
        crypto_scraper.update_json()
        self.start()
    
    # Updates settings.json file with current settings
    def update_settings(self):
        with open(f"{self.PATH}data/settings.json", "w") as f:
            json.dump(self.settings, f, indent=4)