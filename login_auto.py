
from kiteconnect import KiteConnect
import os
import time
import webbrowser

def auto_login():
    api_key = "n0blt8u5o0o0muzk"
    api_secret = "3xcvr258l619a552cp4lju8q676iizel"

    kite = KiteConnect(api_key=api_key)

    print("🔗 Open login URL in browser...")
    url = kite.login_url()
    webbrowser.open(url)

    request_token = input("Paste request token from URL here: ")
    data = kite.generate_session(request_token, api_secret=api_secret)
    kite.set_access_token(data["access_token"])

    print("✅ Login successful. Access token set.")
    return kite
