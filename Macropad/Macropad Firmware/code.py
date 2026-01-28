# -----------------------
# Imports
# -----------------------

import board
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes


# -----------------------
# Keyboard Setup
# -----------------------

keyboard = KMKKeyboard()

# Enable macros & layers
macros = Macros()
layers = Layers()

keyboard.modules.append(macros)
keyboard.modules.append(layers)

# -----------------------
# Key Pins (4 buttons)
# -----------------------

PINS = [
    board.D3,
    board.D4,
    board.D2,
    board.D1,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # buttons wired to GND
)

# -----------------------
# Macros
# -----------------------

# Screenshot (Win + Shift + S)
SCREENSHOT = KC.MACRO(
    Press(KC.LGUI),
    Press(KC.LSHIFT),
    Tap(KC.S),
    Release(KC.LSHIFT),
    Release(KC.LGUI),
)

# Clipboard macros
COPY  = KC.MACRO(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL))
PASTE = KC.MACRO(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL))
CUT   = KC.MACRO(Press(KC.LCTRL), Tap(KC.X), Release(KC.LCTRL))
UNDO  = KC.MACRO(Press(KC.LCTRL), Tap(KC.Z), Release(KC.LCTRL))

# Save (Ctrl + S)
SAVE = KC.MACRO(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL))


# -----------------------
# Keymap
# -----------------------

keyboard.keymap = [

    # -------- Layer 0 (Default) --------
    [
        KC.TG(1),  # Toggle to Layer 1
        COPY,
        PASTE,
        UNDO,
    ],

    # -------- Layer 1 (Productivity) --------
    [
        KC.TG(2),  # Toggle to Layer 2
        SCREENSHOT,
        SAVE,
        CUT,
    ],

    # -------- Layer 2 (Sim Racing) --------
    [
        KC.TG(0),  # Toggle back to Layer 0
        KC.I,      # Traction Control
        KC.O,      # Pit Limiter
        KC.P,      # DRS
    ],
]

# -----------------------
# RGB Setup (2x SK6812)
# -----------------------

rgb = RGB(
    pixel_pin=board.D10,   # Data pin for SK6812
    num_pixels=2,
    animation_mode=AnimationModes.STATIC,
)

keyboard.extensions.append(rgb)

# -----------------------
# LED 1: Layer Indicator
# -----------------------

def set_layer_color():
    if 2 in keyboard.active_layers:
        rgb.set_hsv(170, 255, 100, index=1)  # Blue → Layer 2
    elif 1 in keyboard.active_layers:
        rgb.set_hsv(85, 255, 100, index=1)   # Green → Layer 1
    else:
        rgb.set_hsv(40, 255, 100, index=1)   # Yellow → Layer 0

    rgb.show()

# -----------------------
# LED 0: Flash on Key Press
# -----------------------

def after_keypress(keyboard, key, pressed, *args):
    if pressed:
        # Flash LED 0 white
        rgb.set_hsv(0, 0, 255, index=0)
        rgb.show()
        time.sleep(0.05)
        rgb.set_hsv(0, 0, 0, index=0)

        # Update layer indicator
        set_layer_color()

keyboard.after_keypress_handler = after_keypress

# Initialize LEDs on boot
set_layer_color()

# -----------------------
# Start KMK
# -----------------------

if __name__ == '__main__':
    keyboard.go()
