
from login_auto import auto_login
from trade_engine import start_trading

if __name__ == "__main__":
    print("🔐 Starting Auto Login")
    kite = auto_login()

    print("📈 Starting Smart Money Concept (SMC) Trading")
    start_trading(kite)
