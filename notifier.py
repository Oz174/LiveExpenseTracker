import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def send_whatsapp_alert(message):
    sid = os.getenv("TWILIO_SID")
    auth = os.getenv("TWILIO_AUTH")
    from_whatsapp = os.getenv("TWILIO_FROM")
    to_whatsapp = os.getenv("TWILIO_TO")

    client = Client(sid, auth)

    try:
        msg = client.messages.create(
            body=message,
            from_=from_whatsapp,
            to=to_whatsapp
        )
        print(f"✅ Message sent: SID {msg.sid}")
    except Exception as e:
        print(f"❌ Failed to send message: {e}")
