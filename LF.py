import requests
import uuid, hashlib
import webbrowser

# 🔐 ডিভাইস থেকে ইউনিক key তৈরি
def generate_device_key():
    device_id = str(uuid.getnode())
    hashed = hashlib.sha256(device_id.encode()).hexdigest()
    return hashed[:16]

device_key = generate_device_key()

# ✅ GitHub-এর approved_keys.txt ফাইল চেক
def is_approved(key):
    url = "https://raw.githubusercontent.com/LF9064/old-clone/main/approved_keys.txt"
    try:
        response = requests.get(url)
        approved_keys = response.text.splitlines()
        return key.strip() in approved_keys
    except:
        return False

# 📤 ইউজারের key WhatsApp-এ পাঠানো
def send_key_via_whatsapp(key):
    phone_number = "8801966737564"  # 🔁 তোমার WhatsApp নম্বর
    message = f"Hello developer, my device key is: {key}\nPlease approve it so I can use your tool."
    message = requests.utils.quote(message)
    whatsapp_link = f"https://wa.me/{phone_number}?text={message}"
    print("\n📩 Opening WhatsApp to send your key to the developer...")
    webbrowser.open(whatsapp_link)

# 🔐 Approval Check
if not is_approved(device_key):
    print(f"\n⛔️ Your device is not approved yet.")
    print(f"🔑 Device Key: {device_key}")
    send_key_via_whatsapp(device_key)
    exit()

# ✅ Approved হলে চলবে
print("✅ Your device is approved. Running LF tool...")

# 🔽🔽🔽 LF Tool-এর মূল কোড এখানে 🔽🔽🔽
print("👉 LF tool is now running securely.")
