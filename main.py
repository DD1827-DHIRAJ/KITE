from login_auto import auto_login
from trade_engine import run_trade_bot

kite = auto_login()

if kite:
    print("✅ Bot is now ready to trade.")
    run_trade_bot(kite)
else:
    print("❌ Login failed or token expired. Exiting.")
