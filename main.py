from login_auto import auto_login
from trade_engine import run_smc_strategy
import time

# Run login once
try:
    kite = auto_login()
except Exception as e:
    print(f"❌ Login failed: {e}")
    exit(1)

# Start trading loop
print("📈 Starting Smart Money Concept (SMC) Trading")
run_smc_strategy(kite)

# Keep service alive so Render doesn't rerun
while True:
    time.sleep(300)  # Sleep 5 mins
