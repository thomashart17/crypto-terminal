# Crypto Terminal: Crypto Scraper
# Author: Thomas Hart

import console
import json
import pycoingecko

# Calls the Coin Gecko API to get a list of the top cryptocurrencies by market cap
def get_coins(page):
    coin_gecko = pycoingecko.CoinGeckoAPI()
    coins = coin_gecko.get_coins_markets("usd", page=page, per_page=250)
    return coins

# Updates "data.json" file with new list of symbols and names
def update_json():
    data = {"symbols": {}, "names": {}, "urls": {}}
    for i in range(1, 5):
        coins = get_coins(i)
        print(f"Updating: {round(i/4*100)}%")
        for coin in coins:
            if coin["market_cap_rank"] == None:
                break
            if coin["symbol"].replace("$", "") not in data["symbols"] and coin["name"].lower() not in data["names"]:
                data["symbols"][coin["symbol"].replace("$", "")] = coin["id"]
                data["names"][coin["name"].lower()] = coin["id"]
                data["urls"][coin["id"]] = coin["symbol"].replace("$", "")
        else:
            continue
        break
    with open(f"{console.Console.PATH}/data/data.json", "w") as f:
        json.dump(data, f, indent=4)