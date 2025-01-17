import pygetwindow as gw

def list_window_positions():
    """List the positions and dimensions of all open windows."""
    windows = gw.getAllWindows()
    print("\nWindow Positions and Dimensions:")
    for window in windows:
        if window.title.strip():  # Exclude windows with empty titles
            print(f"Title: {window.title}")
            print(f"  - Position: ({window.left}, {window.top})")
            print(f"  - Size: {window.width}x{window.height}\n")

# Example usage
list_window_positions()
