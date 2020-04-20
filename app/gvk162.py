import random


def get():
    sensor_readings = {
        'latitude': random.uniform(-90, 90),
        'longitude': random.uniform(-180, 180),
        'altitude': random.randint(0, 39500),
    }

    return sensor_readings
