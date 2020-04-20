# Reference: https://github.com/adafruit/Adafruit_CircuitPython_MAX31865
# Additional Reference: https://learn.adafruit.com/adafruit-max31865-rtd-pt100-amplifier?view=all
import board
import busio
import adafruit_max31865

# SPI connection:
from digitalio import DigitalInOut, Direction

# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = DigitalInOut(board.D16)  # Chip select of the MAX31865 board.


def get():
    sensor = adafruit_max31865.MAX31865(spi, cs, wires=3)
    return sensor.temperature
