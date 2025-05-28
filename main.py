
from login_auto import auto_login
from trade_engine import run_smc_strategy

# Run login once
try:
    kite = auto_login()
except Exception as e:
    print(f"❌ Login failed: {e}")
    exit(1)

# If login succeeds, start trading
try:
    print("📈 Starting Smart Money Concept (SMC) Trading")
    run_smc_strategy(kite)
except Exception as e:
    print(f"❌ Trading logic failed: {e}")
    
