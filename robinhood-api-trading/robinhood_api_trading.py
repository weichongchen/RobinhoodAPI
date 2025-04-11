import uuid
from api import CryptoAPITrading
from utils import display


# instantiate the trading client
trading_client = CryptoAPITrading()

# get my account details
account = trading_client.get_account()

# display my account details (without the account number)
print("\n== Account Details: ==\n")
display(account)

# trading_pairs = trading_client.get_trading_pairs()
# print("\n== Trading Pairs: ==\n")
# display(trading_pairs)

# display my holdings
print("\n== Holdings: ==\n")
holdings = trading_client.get_holdings()
for holding in holdings['results']:
    display(holding)

# get the best bid and ask for BTC-USD
print("\n== Best Bid and Ask for DOGE-USD: ==\n")
best_bid_ask = trading_client.get_best_bid_ask('DOGE-USD')
display(best_bid_ask)

# order = trading_client.place_order(
#       str(uuid.uuid4()),
#       "buy",
#       "market",
#       "DOGE-USD",
#       {"asset_quantity": "1"}
# )
# print("\n== Order: ==\n")
# display(order)   

orders = trading_client.get_orders()
print("\n== Orders: ==\n")
for order in orders['results']:
    display(order)

# only display orders from 2020
filtered_orders = list(filter(lambda order: order['created_at'].startswith('2020'), orders['results']))
print("\n== Orders from 2020: ==\n")
display(filtered_orders)
    