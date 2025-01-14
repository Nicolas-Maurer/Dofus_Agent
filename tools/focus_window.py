import pygetwindow as gw
import sys
import time

def focus_window(window_name):
    """Focus on the window with the given name."""
    try:
        windows = gw.getWindowsWithTitle(window_name)
        if not windows:
            print(f"Window '{window_name}' not found.")
            return
        window = windows[0]
        window.activate()
        time.sleep(0.5)
        print(f"Window '{window_name}' activated.")
    except Exception as e:
        print(f"Error activating window: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python focus_window.py <window_name>")
    else:
        focus_window(sys.argv[1])
