#!/usr/bin/env python3
"""
Mouse coordinate finder - helps you find the exact coordinates to click
Run this to see your current mouse position in real-time
Press ESC to exit
"""
from pynput.mouse import Listener
from pynput.keyboard import Key, Listener as KeyListener

def on_move(x, y):
    """Print current mouse position"""
    print(f"\rMouse position: ({x}, {y})", end="", flush=True)

def on_press(key):
    """Stop on ESC press"""
    try:
        if key == Key.esc:
            print("\n\nExited. Use the coordinates shown above in autoclicker.py")
            return False
    except AttributeError:
        pass

if __name__ == "__main__":
    print("Move your mouse to find coordinates. Press ESC to exit.\n")
    with Listener(on_move=on_move) as listener:
        while listener.is_alive():
            try:
                key_listener = KeyListener(on_press=on_press)
                key_listener.start()
                key_listener.join()
                break
            except:
                break
