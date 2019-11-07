import alpaca_trade_api as tradeapi
KEY_ID = "PKQ02SBCWG6K7QCZ9NHG"
KEY_SECRET = "JJtbRCUQw0LfhsFwuxtedyZVsz8cabhotAPVNWXe"
api = tradeapi.REST(KEY_ID, KEY_SECRET, api_version='v2') # or use ENV Vars shown below
account = api.get_account()
api.list_positions()

tradeapi.REST