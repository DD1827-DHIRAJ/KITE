from kiteconnect import KiteConnect
import os

def auto_login():
    try:
        api_key = os.getenv("KITE_API_KEY")
        api_secret = os.getenv("KITE_API_SECRET")
        request_token = os.getenv("KITE_REQUEST_TOKEN")

        kite = KiteConnect(api_key=api_key)
        print("🔐 Starting Auto Login")
        data = kite.generate_session(request_token, api_secret=api_secret)
        kite.set_access_token(data["access_token"])
        print("✅ Login successful. Access token set.")
        return kite
    except Exception as e:
        print("❌ Login failed:", str(e))
        return None