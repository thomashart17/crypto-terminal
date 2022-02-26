# Crypto Terminal: Miner Checker
# Author: Thomas Hart

import console
import json
import mechanize
import miner_scraper
import urllib

def get_miners(ipt):
    with open(f"{console.Console.PATH}/data/settings.json", "r") as f:
        settings = json.load(f)
        currency = settings["currency"]
        electricity = settings["electricity"]
    for i in range(1, len(ipt)):
        try:
            miner_scraper.scrape_miners(ipt[i], currency, electricity)
        except mechanize._mechanize.FormNotFoundError:
            print(f"Could not find \"{ipt[i]}\".")
        except urllib.error.URLError:
            print("Error: Connection failed")
        except:
            print("An unknown error occurred")