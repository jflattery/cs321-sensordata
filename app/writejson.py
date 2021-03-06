import json     # Libary provides methods to convert dict to and from json
import atexit   # Allows a function to be called upon exit. Used to write json file

# Function that takes sensor readings and appends them to python dict
# assumes dictionary has already been initialized prior to call
#   i.e. this line -> sensor_dict = { "sensor_data": [] }
# also assumes varibales have been previously defined (latitude, longitude, roll/yaw/pitch etc.)
def add_json():
    # Append data to the array
    sensor_dict["sensor_data"].append({
        "timestamp": datetime.datetime.now().__str__(),
        "external": {
            "sensor-specs": "\"DHT11 or DHT22 or MAX31865 w/ PT100\"",
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
            "MAX31865 w/ PT100":
                {
                "temperature-range": "\"-200 to 550°C\"",
                "temperature-accuracy": "\"±0.5°C\""
                }
            "temperature": externalReading
        },
        "internal": {
            "sensor-specs": "LSM9DS1, DHT11, or DHT22",
            "temperature_1": internalTemp1,
            "temperature_2": internalTemp2,
            "humidity": internalHumidity
        },
        "accelerometer": {
            "sensor-specs": "\"LSM9DS1\"",
            "def-specs": "\"A 3-tuple of X, Y, Z axis accelerometer values in meters/second squared.\"",
            "range-specs": "\"±2/±4/±8/±16 g\"",
            "x": accel_x,
            "y": accel_y,
            "z": accel_z
        },
        "magnetometer": {
            "sensor-specs": "\"LSM9DS1\"",
            "def-specs": "\"A 3-tuple of X, Y, Z axis magnetometer values in gauss.\"",
            "range-specs": "\"±4/±8/±12/±16 gauss\"",
            "x": mag_x,
            "y": mag_y,
            "z": mag_z
        },
        "gyroscope": {
            "sensor-specs": "\"LSM9DS1\"",
            "def-specs": "\"A 3-tuple of X, Y, Z axis gyroscope values in degrees/second.\"",
            "range-specs": "\"±245/±500/±2000 dps\"",
            "x": gyro_x,
            "y": gyro_y,
            "z": gyro_z
        },
        "orientation": {
            "sensor-specs": "\"Pi Sense HAT\"",
            "def-specs": "\"A 3-tuple of Roll, Pitch, Yaw via an accelerometer, 3D gyroscope, and magnetometer.\"",
            "range-specs": "\"Uncertainity determined by propogation of error (accel,gyro,magnetometer)\"",
            "roll": roll,
            "yaw": yaw,
            "pitch": pitch
        },
        "gps": {
            "sensor-specs": "\"VK162\"",
            "def-specs": "\A 2-tuple of Latitude, Longitude in degrees"\"",
            "range-specs": "\"±5 m\"",
            "latitude": latitude,
            "longitude": longitude#,
            #"altitude": altitude,   <-omitted
        },
        "barometer": {
            "sensor-specs": "\"Pi Sense Hat\"",
            "def-specs": "\Air pressure in hPa"\"",
            "range-specs": "\"±1 hPa\"",
            "pressure": pressure,
        }
        
    })


# This should execute upon normal termination (including ctrl+c press)
@atexit.register
def write_json():
    # This creates a json file using the data filled dictionary
    with open('sensor.json', 'w') as json_file:
        json.dump(sensor_dict, json_file,  indent = 4)
