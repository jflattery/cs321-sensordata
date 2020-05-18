# Reference: https://github.com/adafruit/Adafruit_CircuitPython_DHT/
# Additional Reference: https://learn.adafruit.com/dht/dht-circuitpython-code
import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dht11Device = adafruit_dht.DHT11(board.D17)
dht22Device = adafruit_dht.DHT22(board.D4)

def get(sensor):
    if sensor == 11:
        temperature_c = dht11Device.temperature
        humidity = dht11Device.humidity
    elif sensor == 22:
        temperature_c = dht22Device.temperature
        humidity = dht22Device.humidity
    else:
        print("Invalid Sensor number provided")
        return float('-inf')

    return temperature_c, humidity
