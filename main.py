from login_auto import auto_login
from trade_engine import run_trade_bot

if __name__ == "__main__":
    kite = auto_login()
    if kite:
        print("✅ Bot is now ready to trade.")
        run_trade_bot(kite)
    else:
        print("❌ Exiting due to failed login.")