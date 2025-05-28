from kiteconnect import KiteConnect
import os

def auto_login():
    api_key = os.environ.get('KITE_API_KEY')
    api_secret = os.environ.get('KITE_API_SECRET')
    request_token = os.environ.get('KITE_REQUEST_TOKEN')  # Now taken from environment

    kite = KiteConnect(api_key=api_key)
    data = kite.generate_session(request_token, api_secret=api_secret)
    kite.set_access_token(data["access_token"])
    print("✅ Login successful. Access token set.")
    return kite
