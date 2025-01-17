import os
import time
import pygetwindow as gw

def open_urls_in_chrome(urls):
    """Open each URL in Chrome in a new window."""
    for url in urls:
        os.system(f'start chrome --new-window {url}')
        time.sleep(2)  # Wait for the window to open

def list_window_titles():
    """List all currently open window titles."""
    print("\nAvailable window titles:")
    for title in gw.getAllTitles():
        if title.strip():  # Exclude empty titles
            print(f"- {title}")

def move_window(title_keyword, x, y, width, height):
    """Find and move a window based on a keyword in its title."""
    windows = [w for w in gw.getAllTitles() if title_keyword.lower() in w.lower()]
    if windows:
        window = gw.getWindowsWithTitle(windows[0])[0]
        print(f"Moving window: {window.title}")
        window.moveTo(x, y)
        window.resizeTo(width, height)
    else:
        print(f"No window found with title containing '{title_keyword}'.")

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

    # List all current window titles
    list_window_titles()

    print("\nResizing and moving Chrome windows...")
    # Move and resize windows based on their titles
    move_window("example", 0, 0, 800, 600)         # Top-left
    move_window("github", 800, 0, 800, 600)        # Top-right
    move_window("stackoverflow", 0, 600, 1600, 480)  # Bottom

    print("All set, Mr. Stark!")

if __name__ == "__main__":
    main()
