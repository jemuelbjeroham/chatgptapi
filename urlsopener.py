import os
import time
import pygetwindow as gw

def open_urls_in_chrome(urls):
    """Open each URL in Chrome in a new window."""
    for url in urls:
        os.system(f'start chrome --new-window {url}')
        time.sleep(2)  # Wait for the window to open

def move_window(title, x, y, width, height):
    """Find and move a window based on its title."""
    windows = [w for w in gw.getAllTitles() if title.lower() in w.lower()]
    if windows:
        window = gw.getWindowsWithTitle(windows[0])[0]
        window.moveTo(x, y)
        window.resizeTo(width, height)

def main():
    # List of URLs to open
    urls = [
        "https://example.com",
        "https://github.com",
        "https://stackoverflow.com"
    ]

    print("Opening URLs in Chrome...")
    open_urls_in_chrome(urls)

    # Wait for all windows to load
    time.sleep(5)

    print("Resizing and moving Chrome windows...")
    # Move and resize windows based on their titles
    move_window("example", 0, 0, 800, 600)         # Top-left
    move_window("github", 800, 0, 800, 600)        # Top-right
    move_window("stackoverflow", 0, 600, 1600, 480)  # Bottom

    print("All set, Mr. Stark!")

if __name__ == "__main__":
    main()
