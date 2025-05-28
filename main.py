from login_auto import auto_login
from trade_engine import run_smc_strategy
import time

print("🚀 main.py started")

# Run login once
try:
    print("🔐 Attempting login...")
    kite = auto_login()
    print("✅ Login successful. Access token set.")
except Exception as e:
    print(f"❌ Login failed: {e}")
    exit(1)

# Start trading logic
try:
    print("📈 Starting Smart Money Concept (SMC) Trading")
    run_smc_strategy(kite)
except Exception as e:
    print(f"❌ Trade logic failed: {e}")

# Keep alive
while True:
    print("⏳ Bot running... (sleeping 5 mins)")
    time.sleep(300)
