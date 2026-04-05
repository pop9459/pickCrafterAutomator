#!/usr/bin/env python3
"""
Simple Python Autoclicker with hotkey toggle
"""
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key

# ==================== CONFIGURATION ====================
# Click location (x, y) - change these to your desired coordinates
# Split layout
# ABILITY_1_POS = (160, 1200)
# ABILITY_2_POS = (400, 1200)
# ABILITY_3_POS = (640, 1200)
# ABILITY_4_POS = (880, 1200)
# ABILITY_5_POS = (1120, 1200)
# 
# CLICK_X = 690
# CLICK_Y = 780

# Fullscreen layout
ABILITY_1_POS = (1125, 650)
ABILITY_2_POS = (1125, 825)
ABILITY_3_POS = (1125, 1000)
ABILITY_4_POS = (1125, 1175)
ABILITY_5_POS = (1125, 1350)

CLICK_POS_MOB = (2500, 650)
CLICK_POS_EGG = (1885, 750)
CLICK_POS_COLLECT = (1885, 1125)
# CLICK_POS_POTTATO = (1500, 650)

# Click interval (milliseconds) - time between each click
CLICK_INTERVAL = 10

# Ability interval (milliseconds) - time between each ability click
ABILITY_INTERVAL = 10000

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
    print(f"Click location: ({CLICK_POS_MOB[0]}, {CLICK_POS_MOB[1]}) and ({CLICK_POS_EGG[0]}, {CLICK_POS_EGG[1]})")
    print(f"Click interval: {CLICK_INTERVAL}s")
    print(f"Toggle key: {TOGGLE_KEY}")
    print(f"Press {TOGGLE_KEY} to enable/disable")
    
    # Start keyboard listener
    with Listener(on_press=on_press) as listener:
        try:
            while True:
                if is_clicking:
                    if next_click_time <= time.time():
                            mouse.position = CLICK_POS_MOB
                            mouse.click(Button.left, 1)
                            
                            time.sleep(CLICK_INTERVAL / 1000.0)
                            
                            mouse.position = CLICK_POS_EGG
                            mouse.click(Button.left, 1)

                            time.sleep(CLICK_INTERVAL / 1000.0)

                            mouse.position = CLICK_POS_COLLECT
                            mouse.click(Button.left, 1)

                            print(f"Click at ({CLICK_POS_EGG} and {CLICK_POS_MOB})")
                            next_click_time = time.time() + (CLICK_INTERVAL / 1000.0)
                    
                    if next_ability_time <= time.time():
                            # Click abilities in sequence
                            mouse.position = ABILITY_1_POS
                            mouse.click(Button.left, 1)
                            print(f"Clicked Ability 1 at {ABILITY_1_POS}")
                            time.sleep(0.01)  # Short delay between clicks

                            mouse.position = ABILITY_2_POS
                            mouse.click(Button.left, 1)
                            print(f"Clicked Ability 2 at {ABILITY_2_POS}")
                            time.sleep(0.01)

                            mouse.position = ABILITY_3_POS
                            mouse.click(Button.left, 1)
                            print(f"Clicked Ability 3 at {ABILITY_3_POS}")
                            time.sleep(0.01)

                            mouse.position = ABILITY_4_POS
                            mouse.click(Button.left, 1)
                            print(f"Clicked Ability 4 at {ABILITY_4_POS}")
                            time.sleep(0.01)

                            mouse.position = ABILITY_5_POS 
                            mouse.click(Button.left, 1)
                            print(f"Clicked Ability 5 at {ABILITY_5_POS}")
                            time.sleep(0.01)

                            next_ability_time = time.time() + (ABILITY_INTERVAL / 1000.0)

        except KeyboardInterrupt:
            print("\nAutoclicker stopped by user.")

if __name__ == "__main__":
    clicker_loop()
