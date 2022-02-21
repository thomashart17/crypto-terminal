# Crpyto Terminal: Price Scraper
# Author: Thomas Hart

import bs4
import requests

# Scrapes price of given cryptocurrency from Coin Gecko
def get_price(crypto, currency):
    url = f"https://www.coingecko.com/en/coins/{crypto.lower()}/{currency.lower()}"
    site = requests.get(url)
    soup = bs4.BeautifulSoup(site.text, "html.parser")
    price = soup.find("span", class_="no-wrap")
    return bs4.BeautifulSoup.get_text(price)