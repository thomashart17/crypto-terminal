# Crypto Terminal: Miner Scraper
# Author: Thomas Hart

import bs4
import mechanize

# Scrapes data for miners of given cryptocurrency from Miner Stat
def scrape_miners(crypto, currency, electricity):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [("User-agent", "Chrome")]
    browser.open(f"https://www.minerstat.com/coin/{crypto}/profitability")
    browser.select_form(method="post")
    browser.form["currency"] = [currency]
    browser.form["electricityCosts"] = str(electricity)
    browser.submit()
    soup = bs4.BeautifulSoup(browser.response().read(), "html.parser")
    miners = soup.find_all("div", class_="td flexHardware")
    prices = soup.find_all("div", class_="td rmv1 flexProfit profit_order")
    print(f"\"{crypto.upper()}\" miners:")
    for i in range(len(miners)):
        print(bs4.BeautifulSoup.get_text(miners[i]), bs4.BeautifulSoup.get_text(prices[i]))