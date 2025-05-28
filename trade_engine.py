
import datetime

def start_trading(kite):
    now = datetime.datetime.now()
    if now.hour == 14 and now.minute >= 30:
        print("⚡ Running Zero-to-Hero Expiry Strategy")
        # SMC expiry trade logic goes here
        # kite.place_order(...)
    else:
        print("🚀 Running Normal Smart Money Concept Trade Logic")
        # Your POI, Fractal, ITH/STH logic here
        # kite.place_order(...)
