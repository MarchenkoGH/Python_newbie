ef common_dict():
    return {coin: code for coin, code in zip(coin, code)}


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
print(common_dict())
