from login_auto import auto_login

kite = auto_login()

if kite:
    print("馃搱 Bot is now ready to trade.")
else:
    print("鉂� Exiting due to failed login.")
