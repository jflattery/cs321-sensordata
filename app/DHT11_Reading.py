#!/usr/bin/python
import sys

# this library requires installing adafruit library to pi! Can be found
#                       https://github.com/adafruit/Adafruit_Python_DHT.git
import Adafruit_DHT 

# time libary
import time

start = time.time()
while True:

    humidity, temperature = Adafruit_DHT.read(11, 4)
    if (humidity is not None and temperature is not None):
        end = time.time()
        print "{}".format(end - start)
        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
        saveH = humidity
        saveT = temperature
    elif (saveH is not None and saveT is not None):
        end = time.time()
        print "{}".format(end - start)
        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(saveT, saveH)
    else:
        continue
    start = time.time()
    
    # Sleep for at least 1 second to gaurantee, DHT11 has at least 1 second before being read again
    time.sleep(1)
