import os
import time
import pyautogui
import pygetwindow as gw

def open_application(command):
    os.system(command)
    time.sleep(5)  # Allow time for the application to open

def move_window(title, x, y, width, height):
    windows = [w for w in gw.getAllTitles() if title.lower() in w.lower()]
    if windows:
        window = gw.getWindowsWithTitle(windows[0])[0]
        window.moveTo(x, y)
        window.resizeTo(width, height)

def greet_user():
    from datetime import datetime
    now = datetime.now()
    if now.hour < 12:
        return "Good morning"
    elif now.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def main():
    print("Starting your setup, Mr. Stark...")
    
    # Open applications
    open_application("start chrome")  # Chrome
    open_application("start outlook")  # Outlook
    open_application("start slack")  # Slack
    
    # Move and resize windows
    time.sleep(10)  # Ensure all apps are loaded
    move_window("chrome", 0, 0, 800, 600)  # Top-left
    move_window("outlook", 800, 0, 800, 600)  # Top-right
    move_window("slack", 0, 600, 1600, 480)  # Bottom
    
    # Open PowerShell
    open_application("start powershell")
    print(f"{greet_user()}, Mr. Stark! Everything is set up.")

if __name__ == "__main__":
    main()
