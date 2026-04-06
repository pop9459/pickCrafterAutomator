#!/usr/bin/env python3
"""
Mouse coordinate finder and config generator.
Move the mouse and use hotkeys to capture target coordinates.

Hotkeys:
- m: capture mob click position
- e: capture egg click position
- c: capture collect click position
- 1-5: capture ability 1-5 positions
- o: capture default/open chest position
- b: capture buy position
- r: capture refill position
- h: capture claim chest position
- s: save to click_config.json
- ESC: exit
"""
import json
from pathlib import Path

from pynput.mouse import Listener
from pynput.mouse import Controller
from pynput.keyboard import Key, Listener as KeyListener

CONFIG_PATH = Path(__file__).parent / "click_config.json"

TARGET_KEYS = {
    "m": "CLICK_POS_MOB",
    "e": "CLICK_POS_EGG",
    "c": "CLICK_POS_COLLECT",
    "1": "ABILITY_1_POS",
    "2": "ABILITY_2_POS",
    "3": "ABILITY_3_POS",
    "4": "ABILITY_4_POS",
    "5": "ABILITY_5_POS",
    "o": "CLICK_POS_DEFAULT",
    "b": "CLICK_POS_BUY",
    "r": "CLICK_POS_REFIL",
    "h": "CLICK_POS_CLAIM",
}

mouse = Controller()
captured_positions = {}


def save_config():
    """Write captured coordinates to click_config.json"""
    if not captured_positions:
        print("\nNo coordinates captured yet. Nothing to save.")
        return

    config = {
        "positions": captured_positions,
    }

    with CONFIG_PATH.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print(f"\nSaved {len(captured_positions)} positions to: {CONFIG_PATH}")


def capture_position(target_name):
    """Capture current mouse position for a specific target"""
    x, y = mouse.position
    captured_positions[target_name] = [int(x), int(y)]
    print(f"\nCaptured {target_name}: ({int(x)}, {int(y)})")

def on_move(x, y):
    """Print current mouse position"""
    print(f"\rMouse position: ({x}, {y})", end="", flush=True)

def on_press(key):
    """Handle hotkeys for capture/save/exit"""
    try:
        if key == Key.esc:
            print("\n\nExited coordinate finder.")
            return False

        if hasattr(key, "char") and key.char:
            normalized = key.char.lower()

            if normalized in TARGET_KEYS:
                capture_position(TARGET_KEYS[normalized])
                return

            if normalized == "s":
                save_config()
                return
    except AttributeError:
        pass

if __name__ == "__main__":
    print("Move your mouse to find coordinates.\n")
    print("Capture keys:")
    print("  m = CLICK_POS_MOB")
    print("  e = CLICK_POS_EGG")
    print("  c = CLICK_POS_COLLECT")
    print("  1-5 = ABILITY_1_POS ... ABILITY_5_POS")
    print("  o = CLICK_POS_DEFAULT")
    print("  b = CLICK_POS_BUY")
    print("  r = CLICK_POS_REFIL")
    print("  h = CLICK_POS_CLAIM")
    print("  s = save click_config.json")
    print("  ESC = exit\n")

    with Listener(on_move=on_move) as listener:
        while listener.is_alive():
            try:
                key_listener = KeyListener(on_press=on_press)
                key_listener.start()
                key_listener.join()
                break
            except:
                break
