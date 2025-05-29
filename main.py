from login_auto import auto_login
from trade_engine import run_trade_bot

# Only login once when service starts
if __name__ == '__main__':
    try:
        print("🔁 Starting Auto Login")
        kite = auto_login()
        
        if kite:
            print("✅ Bot is now ready to trade.")
            run_trade_bot(kite)
        else:
            print("❌ Login failed or token expired. Exiting.")
            
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
