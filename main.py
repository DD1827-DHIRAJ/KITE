import time
from login_auto import auto_login
from trade_engine import run_smc_strategy
import traceback

def main():
    print("🚀 Starting Auto Trader")
    try:
        kite = auto_login()
        print("✅ Login successful. Access token set.")
        run_smc_strategy(kite)
    except Exception as e:
        print("❌ Error during login or strategy:")
        traceback.print_exc()

    while True:
        print("❤️ System heartbeat active")
        time.sleep(60)

if __name__ == "__main__":
    main()
