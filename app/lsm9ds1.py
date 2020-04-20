# Reference: https://github.com/adafruit/Adafruit_CircuitPython_LSM9DS1/
# Additional Reference: https://learn.adafruit.com/adafruit-lsm9ds1-accelerometer-plus-gyro-plus-magnetometer-9-dof-breakout
import board
import busio
import adafruit_lsm9ds1

# SPI connection:
from digitalio import DigitalInOut, Direction

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
csag = DigitalInOut(board.D5)
csag.direction = Direction.OUTPUT
csag.value = True
csm = DigitalInOut(board.D6)
csm.direction = Direction.OUTPUT
csm.value = True


def get():
    sensor = adafruit_lsm9ds1.LSM9DS1_SPI(spi, csag, csm)

    sensor_readings = {
        'acceleration': sensor.acceleration,
        'magnetometer': sensor.magnetic,
        'gyroscope': sensor.gyro,
        'temperature': sensor.temperature,
    }

    return sensor_readings
