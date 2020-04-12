import json     # Libary provides methods to convert dict to and from json
import datetime # Used for timestamp
import random # I just used this to generate mock data

# Dictionary that will hold all sensor data. Converted to json later
# The array portion holds new readings

sensor_dict = { "sensor_data": [] }

# Measurements are taken every second during the duration of 'airtime'.
# For the sake of demonstration, this will add mock readings 4 times
for x in range(0,4):

    # Sensors will input  readings into these variables
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    altitude = random.randint(0, 39500)
    roll = random.uniform(-180, 180)
    pitch = random.uniform(-90, 90)
    yaw = random.uniform(-180, 180)
    ext_temp = random.uniform(-40, 80)
    ext_humidity = random.uniform(0, 1)
    int_temp = random.uniform(-40, 80)
    accelerometer = [ # array of x, y, z
        random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)
    ]
    magnetometer = [ # array of x, y, z
        random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)
    ]
    gyroscope = [ # array of x, y, z
        random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)
    ]

    # Append data to the array
    sensor_dict["sensor_data"].append({
        "timestamp": datetime.datetime.now().__str__(),
        "latitude": latitude,
        "longitude": longitude,
        "altitude": altitude,
        "roll": roll,
        "pitch": pitch,
        "yaw": yaw,
        "external": {
            "sensor-specs": "\"DHT11 or DHT22\"",
            "dht11-specs":
                {
                "humidity-range": "\"20-80%\"",
                "humidity-accuracy": "\"5%\"",
                "temperature-range": "\"0-50°C\"",
                "temperature-accuracy": "\"±2°C\""
                },
            "dht22-specs":
                {
                "humidity-range": "\"0-100%\"",
                "humidity-accuracy": "\"2-5%\"",
                "temperature-range": "\"-40 to 80°C\"",
                "temperature-accuracy": "\"±0.5°C\""
                },
            "temperature": ext_temp,
            "humidity": ext_humidity
        },
        "internal": {
            "sensor-specs": "LSM9DS1, DHT11, or DHT22",
            "temperature": int_temp
        },
        "accelerometer": {
            "sensor-specs": "\"LSM9DS1\"",
            "def-specs": "\"A 3-tuple of X, Y, Z axis accelerometer values in meters/second squared.\"",
            "range-specs": "\"±2/±4/±8/±16 g\"",
            "x": accelerometer[0],
            "y": accelerometer[1],
            "z": accelerometer[2]
        },
        "magnetometer": {
            "sensor-specs": "\"LSM9DS1\"",
            "def-specs": "\"A 3-tuple of X, Y, Z axis magnetometer values in gauss.\"",
            "range-specs": "\"±4/±8/±12/±16 gauss\"",
            "x": magnetometer[0],
            "y": magnetometer[1],
            "z": magnetometer[2]
        },
        "gyroscope": {
            "sensor-specs": "\"LSM9DS1\"",
            "def-specs": "\"A 3-tuple of X, Y, Z axis gyroscope values in degrees/second.\"",
            "range-specs": "\"±245/±500/±2000 dps\"",
            "x": gyroscope[0],
            "y": gyroscope[1],
            "z": gyroscope[2]
        }
    })

## This would convert dictinary into json string
# string =json.dumps()

## This would create json file
with open('generate.json', 'w') as json_file:
    json.dump(sensor_dict, json_file,  indent = 4)
