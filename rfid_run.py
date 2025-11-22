import serial
import base64
import pyautogui
import time

# Open the serial port (update COM port if needed)
ser = serial.Serial("COM6", 9600, timeout=50)  

print("🔄 Waiting for RFID data...")

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()
    print(f"🔍 Debug: Received line → {line}")

    if line.startswith("Block 4:"):  # Match expected RFID output
        raw_data = line.split(": ", 1)[1].strip()  # Extract "hari:9876"

        try:
            # If data is base64-encoded, decode it (uncomment if needed)
            # raw_data = base64.b64decode(raw_data).decode("utf-8")

            username, password = raw_data.split(":", 1)
            print(f"✅ Decoded Username: {username}")
            print(f"✅ Decoded Password: {password}")

            print("⏳ Autofilling in 5 seconds... Switch to login form!")
            time.sleep(3)  

            pyautogui.write(username)
            pyautogui.press("tab")  # Move to password field
            pyautogui.write(password)
            pyautogui.press("enter")  # Press Enter to log in

            print("✅ Autofilled login details!")

        except Exception as e:
            print(f"❌ Error processing data: {e}")
