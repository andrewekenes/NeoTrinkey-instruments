import time
import touchio
import board
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
led = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.2, auto_write=True)

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

while True:
    if touch1.value:

        kbd.send(Keycode.SPACE)                                                                                                                                                         