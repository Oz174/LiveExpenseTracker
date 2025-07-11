import time
from sheets_reader import get_sheet_data
from utils import generate_alert
from notifier import send_whatsapp_alert

CHECK_INTERVAL = 30  # Act as rate limiter to avoid spam on google sheets api 
ALERT_SENT = False   # State flag

print("🔄 Live Watch Mode started... (press Ctrl+C to stop)")

try:
    while True:
        expenses, current_remaining, target_remaining = get_sheet_data()
        message = generate_alert(current_remaining, target_remaining)

        if message:
            if not ALERT_SENT:
                print("[ALERT]", message)
                send_whatsapp_alert(message)
                ALERT_SENT = True
            else:
                print("⚠️ Alert already sent. Waiting for state to change.")
        else:
            if ALERT_SENT:
                print("✅ Balance back to safe range. Resetting alert flag.")
                ALERT_SENT = False
            else:
                print("✅ All good. Monitoring...")

        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("\n👋 Exiting Live Watch Mode.")
