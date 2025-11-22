import serial
import base64
import pyautogui
import time
ser = serial.Serial("COM7", 9600, timeout=50)  
print("Waiting for RFID data...")
while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()
    print(f"Debug: Received line: {line}")
    if line.startswith("Block 4:"):  
        raw_data = line.split(": ", 1)[1].strip()
        try:
            username, password = raw_data.split(":", 1)
            print(f"Decoded Username: {username}")
            print(f"Decoded Password: {password}")
            print("Autofilling in 5 seconds... Switch to login form!")
            time.sleep(3)  
            pyautogui.write(username)
            pyautogui.press("tab")  
            pyautogui.write(password)
            pyautogui.press("enter")  
            print("Autofilled login details!")
        except Exception as e:
            print(f"Error processing data: {e}")


