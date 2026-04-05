#!/usr/bin/env python3
"""
Simple Python Autoclicker with hotkey toggle
"""
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key

# ==================== CONFIGURATION ====================
# Click location (x, y) - change these to your desired coordinates

CLICK_POS_DEFAULT = (1500, 800)
CLICK_POS_BUY = (1800, 600)
CLICK_POS_REFIL = (1650, 350)
CLICK_POS_CLAIM = (1800, 100)

# Click interval (milliseconds) - time between each click
CLICK_INTERVAL = 100

# Toggle key - which key activates/deactivates the autoclicker
# Options: Key.caps_lock, Key.scroll_lock, Key.num_lock, or any letter like 'a'
TOGGLE_KEY = Key.caps_lock

# ==================== END CONFIGURATION ====================

mouse = Controller()
is_clicking = False
next_click_time = 0
next_ability_time = 0

def toggle_clicking():
    """Toggle the autoclicker on/off"""
    global is_clicking
    is_clicking = not is_clicking
    status = "ON" if is_clicking else "OFF"
    print(f"Autoclicker turned {status}")

def on_press(key):
    """Handle key press events"""
    try:
        if key == TOGGLE_KEY:
            toggle_clicking()
    except AttributeError:
        pass

def on_release(key):
    """Handle key release events"""
    # Stop listener if ESC is pressed
    if key == Key.esc:
        print("\nAutoclicker stopped. Press ESC again to exit listener.")
        return False

def clicker_loop():
    """Main clicking loop"""
    global next_click_time, next_ability_time
    
    print(f"Autoclicker initialized!")
    print(f"Click interval: {CLICK_INTERVAL}s")
    print(f"Toggle key: {TOGGLE_KEY}")
    print(f"Press {TOGGLE_KEY} to enable/disable")
    
    # Start keyboard listener
    with Listener(on_press=on_press) as listener:
        try:
            while True:
                if is_clicking:
                    print("Buying...")

                    mouse.position = CLICK_POS_REFIL
                    mouse.click(Button.left, 1)
                    time.sleep(CLICK_INTERVAL / 1000.0)
                    
                    time.sleep(0.25)

                    mouse.position = CLICK_POS_BUY
                    mouse.click(Button.left, 1)
                    time.sleep(CLICK_INTERVAL / 1000.0)
                    mouse.click(Button.left, 1)
                    time.sleep(CLICK_INTERVAL / 1000.0)

                    time.sleep(0.25)

                    mouse.position = CLICK_POS_REFIL
                    mouse.click(Button.left, 1)
                    time.sleep(CLICK_INTERVAL / 1000.0)

                    time.sleep(0.25)

                    mouse.position = CLICK_POS_BUY
                    mouse.click(Button.left, 1)
                    time.sleep(CLICK_INTERVAL / 1000.0)
                    mouse.click(Button.left, 1)
                    time.sleep(CLICK_INTERVAL / 1000.0)

                    time.sleep(0.25)

                    print("Claiming chest...")

                    mouse.position = CLICK_POS_CLAIM
                    mouse.click(Button.left, 1)
                    time.sleep(CLICK_INTERVAL / 1000.0)
                    
                    time.sleep(0.25)

                    print("Opening chest...")

                    mouse.position = CLICK_POS_DEFAULT
                    for _ in range(25):
                        mouse.click(Button.left, 1)
                        time.sleep(CLICK_INTERVAL / 1000.0)

                    time.sleep(1)

                    print("Exiting chest...")

                    mouse.click(Button.left, 1)

                    time.sleep(0.25)

        except KeyboardInterrupt:
            print("\nAutoclicker stopped by user.")

if __name__ == "__main__":
    clicker_loop()
