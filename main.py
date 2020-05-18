#imports
import Adafruit_DHT
import time
import serial

#sense hat initialization
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

#gps module initialization
gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)

#dht22 intialization
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

#inital values of some data
ex_old_temp = None
ex_old_humid = None
lat_str = " "
long_str = " "

#reading sensors until interuption
while True:
    #external temp/humidity
    ex_humidity, ex_temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    print("=====================================================")
    #output external temp/humidity on success
    #output old values (if they exist) when sensor fails to read at 1Hz
    if ex_humidity is not None and ex_temperature is not None:
        ex_old_temp = ex_temperature
        ex_old_humid = ex_humidity
        print("External Temperature: {0:0.1f}C External Humidity: {1:0.1f}%".format(ex_temperature, ex_humidity))
    elif ex_old_temp is not None and ex_old_humid is not None:
        print("External Temperature: {0:0.1f}C External Humidity: {1:0.1f}%".format(ex_old_temp, ex_old_humid));

    #internal temp/humidity
    in_temperature = sense.get_temperature()
    in_humidity = sense.get_humidity()
    #round the values to one decimal place
    in_temperature = round(in_temperature, 1)
    in_humidity = round(in_humidity, 1)
    #output internal temp/humidity
    print("Internal Temperature: " + str(in_temperature)+ "C " + "Internal Humidity: " + str(in_humidity) + "%")

    #pressure
    pressure = sense.get_pressure()
    #round the value to one decimal place
    pressure = round(pressure, 1)
    #output pressure
    print("Pressure: " + str(pressure) + " millibars")

    #getting orientation of sense hat
    orientation = sense.get_orientation()
    #roll, pitch, yaw
    pitch = orientation["pitch"]
    roll = orientation["roll"]
    yaw = orientation["yaw"]
    #output roll, pitch, yaw
    print("Pitch: {0:0.5f}°  Roll: {1:0.5f}°  Yaw: {2:0.5f}°".format(pitch, roll, yaw))

    #gps module information
    line = gps.readline()
    data = line.decode().split(",")
    #for the correct module,
    if data[0] == "$GPRMC":
        #on success, output longitude and latitude
        #output old values (if they exist) when gps module fails to read at 1Hz
        if data[2] == "A":
            lat_str = data[3] + " " + data[4]
            long_str = data[5] + " " + data[6]
            print("Latitude in DDM: %s" % (lat_str))
            print("Longitude in DDM: %s" % (long_str))
        elif lat_str != " " and long_str != " " :
            print("Latitude in DDM: %s" % (lat_str))
            print("Longitude in DDM: %s" % (long_str))
    elif lat_str != " " and long_str != " " :
            print("Latitude in DDM: %s" % (lat_str))
            print("Longitude in DDM: %s" % (long_str))

    #output at 1Hz increments until there is keyboard interuption
    time.sleep(1);
