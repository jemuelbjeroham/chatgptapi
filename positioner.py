import os
import time
import pygetwindow as gw

def open_shortcuts(shortcuts):
    """Open the specified .lnk files."""
    for shortcut in shortcuts:
        os.startfile(shortcut)
        time.sleep(2)  # Wait for each window to open

def move_window(title, x, y, width, height):
    """Find and move a window based on its title."""
    windows = [w for w in gw.getAllTitles() if title.lower() in w.lower()]
    if windows:
        window = gw.getWindowsWithTitle(windows[0])[0]
        window.moveTo(x, y)
        window.resizeTo(width, height)

def main():
    # List of .lnk files to open
    shortcuts = [
        r"C:\Users\Jemuel\Desktop\WebApp1.lnk",
        r"C:\Users\Jemuel\Desktop\WebApp2.lnk"
    ]

    print("Opening Chrome shortcuts...")
    open_shortcuts(shortcuts)

    # Wait for the windows to load
    time.sleep(5)

    print("Resizing and moving Chrome windows...")
    # Move and resize windows based on their titles
    move_window("WebApp1", 0, 0, 800, 600)  # Top-left
    move_window("WebApp2", 800, 0, 800, 600)  # Top-right

    print("All set, Mr. Stark!")

if __name__ == "__main__":
    main()
