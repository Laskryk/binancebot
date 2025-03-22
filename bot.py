import ccxt

# Introdu manual cheile API aici
api_key = "CHEIA_TA_API"w7NhaaVholURZ5I69hmMJznOHJKxQpNIKsIc8Yb0uIVtZLDcQan5m9Rm4TbhwMg
api_secret = "SECRETUL_TĂU_API"YmIzU0bsUo8bPF9lpz3WulMMqePGAn7U3IPSz7UawN92tX2fsKsePYiiUIQE8iz7

# Conectează-te la Binance
exchange = ccxt.binance({
    "apiKey": api_key,
    "secret": api_secret,
    "enableRateLimit": True
})

# Verifică soldul contului
balance = exchange.fetch_balance()
print("Bot conectat la Binance!")
print("Soldul disponibil:", balance["total"])

