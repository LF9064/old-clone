import requests
import os
import hashlib

def generate_device_key():
    device_info = os.uname()
    raw_string = device_info.machine + device_info.nodename + device_info.release
    hashed = hashlib.sha256(raw_string.encode()).hexdigest()
    return hashed[:16]

device_key = generate_device_key()

def is_approved(key):
    url = "https://raw.githubusercontent.com/LF9064/old-clone/main/approved_keys.txt"
    try:
        response = requests.get(url)
        approved_keys = response.text.splitlines()
        return key.strip() in approved_keys
    except:
        return False

def send_key_via_whatsapp(key):
    phone_number = "8801966737564"
    message = f"Hello developer, my device key is: {key}\nPlease approve it so I can use your tool."
    message = requests.utils.quote(message)
    whatsapp_link = f"https://wa.me/{phone_number}?text={message}"
    print("\n🔗 Please send this message to the developer on WhatsApp:")
    print(f"{whatsapp_link}")

if not is_approved(device_key):
    print(f"\n⛔️ Your device is not approved yet.")
    print(f"🔑 Device Key: {device_key}")
    send_key_via_whatsapp(device_key)
    exit()

print("✅ Your device is approved. Running LF tool...")
print("👉 LF tool is now running securely.")
