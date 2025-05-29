from login_auto import auto_login
from trade_engine import run_trade_bot

login_attempted = False
kite = None

if not login_attempted:
    kite = auto_login()
    login_attempted = True

if kite:
    print("✅ Bot is now ready to trade.")
    run_trade_bot(kite)
else:
    print("❌ Exiting due to failed login.")
