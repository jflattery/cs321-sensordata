# Reference: https://github.com/adafruit/Adafruit_CircuitPython_DHT/
# Additional Reference: https://learn.adafruit.com/dht/dht-circuitpython-code
import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)


def get():
    temperature_c = dhtDevice.temperature
    humidity = dhtDevice.humidity
    return temperature_c, humidity
