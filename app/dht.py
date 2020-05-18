# Reference: https://github.com/adafruit/Adafruit_CircuitPython_DHT/
# Additional Reference: https://learn.adafruit.com/dht/dht-circuitpython-code
import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT11(board.D17)

# def get():
#    temperature_c = dhtDevice.temperature
#    humidity = dhtDevice.humidity
#    return temperature_c, humidity

def get(sensor):
    if sensor == 11:
        try:
          dht_device = adafruit_dht.dht11(board.D17)
        except:
          return float('nan')
    elif sensor == 22:
        try:
          dht_device = adafruit_dht.dht22(board.D4)
        except:
          return float('nan')
    else:
        return float('-inf')

    try:
        temperature_c = dht_device.temperature
    except:
        temperature_c = float('-inf')
    try:
        humidity = dht_device.humidity
    except:
        humidity = float('-inf')

    return temperature_c, humidity
