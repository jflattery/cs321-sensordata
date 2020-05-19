import random
import serial

gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)

def get():
  line = gps.readline()
  data = line.decode().split(",")
  if data[0] == "$GPRMC":
    if data[2] == "A": #V = Navigation receiver warning, A = Data valid
      TalkerID = data[0]
      utcTime = data[1]
      lat_str = data[3] + " " + data[4]
      long_str = data[5] + " " + data[6]
      spd = data[7]
      cog= data[8]
      altitude = float('-inf')
  elif data[0] == "$GPGGA":
    TalkerID = data[0]
    utcTime = data[1]
    lat_str = data[2] + " " + data[3]
    long_str = data[4] + " " + data[5]
    quality = data[6]
    numSatellites = data[7]
    altitude = data[9] + " " + data[10]
    geoidSeparation =  data[11] + " " + data[12]

  sensor_readings = {
    'latitude': lat_str,
    'longitude': long_str,
    'altitude': altitude,
    'gpsTime': utcTime,
  }
  
  return sensor_readings
