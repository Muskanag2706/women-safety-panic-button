import json
from datetime import datetime
from .gps import get_location
from .notifiers import send_sms, send_telegram
from .config import CONTACTS_FILE

def load_contacts():
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def panic_alert():
    contacts = load_contacts()
    latitude, longitude = get_location()
    message = f"🚨 Panic Alert! I need help! My location: https://maps.google.com/?q={latitude},{longitude}"

    # Send SMS to all contacts
    for contact in contacts:
        send_sms(contact["phone"], message)

    # Send Telegram alert
    send_telegram(message)

    # Log the alert
    with open("panic_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: Alert sent to {len(contacts)} contacts at {latitude},{longitude}\n")

if __name__ == "__main__":
    panic_alert()
