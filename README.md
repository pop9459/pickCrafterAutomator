# Autoclicker Program

A simple Python autoclicker with hotkey toggle support.

## Features

- **Customizable click location** - Set any X/Y coordinates
- **Hotkey toggle** - Enable/disable with a single key press (default: Caps Lock)
- **Adjustable click speed** - Control the interval between clicks
- **Coordinate finder helper** - Utility to find mouse coordinates easily

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Step 1: Find your click coordinates
```bash
python find_coordinates.py
```
Move your mouse to the location you want to click, note the coordinates, then press ESC.

### Step 2: Configure autoclicker.py
Open `autoclicker.py` and update the configuration section:

```python
CLICK_X = 500        # Your X coordinate
CLICK_Y = 500        # Your Y coordinate
CLICK_INTERVAL = 0.1 # Time between clicks (seconds)
TOGGLE_KEY = Key.caps_lock  # Key to toggle on/off
```

### Step 3: Run the autoclicker
```bash
python autoclicker.py
```

The program will start and wait for you to press the toggle key.

## Usage

- **Press Caps Lock** (or your configured toggle key) to enable/disable clicking
- **Press ESC** to stop the program
- Check the console for real-time feedback

## Configuration Options

### Toggle Keys

You can change `TOGGLE_KEY` to any:
- `Key.caps_lock` - Caps Lock key
- `Key.scroll_lock` - Scroll Lock key
- `Key.num_lock` - Num Lock key
- `Key.f1` through `Key.f20` - Function keys
- `'a'`, `'b'`, etc. - Individual letter keys

### Click Interval

- `0.05` - Very fast (20 clicks/sec)
- `0.1` - Fast (10 clicks/sec) - **Default**
- `0.25` - Medium (4 clicks/sec)
- `0.5` - Slow (2 clicks/sec)
- `1.0` - Very slow (1 click/sec)

## Example Configuration

```python
# For a game button at position (1920, 1080), hitting 2x per second
CLICK_X = 1920
CLICK_Y = 1080
CLICK_INTERVAL = 0.5
TOGGLE_KEY = Key.scroll_lock
```

## Safety Tips

- Always have ESC key easily accessible to stop the program
- Test with a slow `CLICK_INTERVAL` first
- Make sure the click location doesn't interfere with window focus

## Troubleshooting

**Permission denied error?**
- On Linux, you may need to run with appropriate permissions
- Try: `sudo python autoclicker.py`

**Keys not detecting?**
- Some systems require elevated privileges for keyboard listening
- Try running with `sudo`

**Mouse clicks not working?**
- Verify the coordinates are on your screen resolution
- Try the `find_coordinates.py` helper to confirm positions
