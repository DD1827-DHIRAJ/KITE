import os
import time
from login_auto import auto_login
from trade_engine import run_smc_strategy

print("✅ System heartbeat started")

def main():
    try:
        kite = auto_login()
        print("✅ Login successful. Access token set.")

        print("📈 Starting Smart Money Concept (SMC) Trading")
        run_smc_strategy(kite)

    except Exception as e:
        print(f"❌ Error in main(): {str(e)}")

if __name__ == "__main__":
    main()
    while True:
        print("⏳ Alive...", time.ctime())
        time.sleep(60)
