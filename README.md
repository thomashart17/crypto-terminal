# Crypto Terminal
## Description
Crypto Terminal is command line application that allows users to get data about a variety of cryptocurrencies. It makes use of the Coin Gecko API to get data about the top 1000 cryptocurrencies. This includes prices for individual coins by symbol or name as well as prices for top currencies by market cap. To get data for the most profitable mining hardware by currency, the application makes use of the Python mechanize and bs4 libraries. These libraries are used to scrape data from Minerstat based on given currency and electricity costs.
## Dependencies
In order to use this appliation, users will need Python version 3.7 and the following Python libraries installed on their device:
- [bs4](https://pypi.org/project/bs4)
- [mechanize](https://pypi.org/project/mechanize)
- [pycoingecko](https://pypi.org/project/pycoingecko)
## Installation
Clone the repository to your device in your desired directory:

`git clone https://github.com/thomashart17/crypto-terminal`

Add \<YOUR DIRECTORY\>/app to your path variables. The application can now be run using: `crypto-terminal`
## Available commands
The following commands are currently available for use:
- currency: Displays the current currency or updates to a specified currency.
- electricity: Displays the current electricity cost per kWh or updates to a specified cost.
- exit: Exits the application back to the command line.
- help: Displays a list of available commands and their uses.
- miners: Displays a list of all miners available for the input currency as well as their profitability per day.
- price: Displays prices for the input cryptocurrencies.
- update: Updates the list of available currencies to match what is found on Coin Gecko.