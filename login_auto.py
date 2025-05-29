
import os
from kiteconnect import KiteConnect

def auto_login():
    kite = KiteConnect(api_key=os.getenv('KITE_API_KEY'))
    data = kite.generate_session(
        request_token=os.getenv('KITE_REQUEST_TOKEN'),
        api_secret=os.getenv('KITE_API_SECRET')
    )
    kite.set_access_token(data['access_token'])
    return kite
