import os
import ccxt

api_key = os.getenv("API_KEY")w7NhaaVholURZ5I69hmMJznOHJKxQpNIKsIc8Yb0uIVtZLDcQan5m9Rm4TbhwMg
api_secret = os.getenv("API_SECRET")YmIzU0bsUo8bPF9lpz3WulMMqePGAn7U3IPSz7UawN92tX2fsKsePYiiUIQE8iz7

exchange = ccxt.binance({
    "apiKey": api_key,
    "secret": api_secret,
    "enableRateLimit": True
})

print("Bot conectat la Binance!")
# binancebot
bot traiding automat
