from login_auto import auto_login
from trade_engine import run_trade_bot

# Run once and exit cleanly after 1 login attempt
if __name__ == '__main__':
    print("🚀 Starting Auto Login")
    kite = auto_login()

    if kite:
        print("✅ Bot is now ready to trade.")
        run_trade_bot(kite)
    else:
        print("❌ Login failed. Exiting.")
