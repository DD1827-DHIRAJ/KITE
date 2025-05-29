from login_auto import auto_login

try:
    kite = auto_login()
    print("📈 Bot is now ready to trade.")
except Exception as e:
    print("🛑 Login failed or already logged in. Skipping re-login.")
    exit()

if kite:
    print("馃搱 Bot is now ready to trade.")
else:
    print("鉂� Exiting due to failed login.")
