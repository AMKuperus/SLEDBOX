import time
import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Amount of LED's on strip
LEDS = 32

SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(LEDS, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)

def rainbow_cycle(pixels, wait=0.001):
    for i in range(256):
        for j in range(pixels.count()):
            pixels.set_pixel(j, wheel(((i * 256 // pixels.count()) + j) % 256))
        pixels.show()
        if wait > 0:
            time.sleep(wait)

if __name__ == "__main__":
    pixels.clear()
    pixels.show()
    rainbow_cycle(pixels, wait=0.01)
