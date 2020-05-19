import time
import datetime
import dht
import max31865
import lsm9ds1
import gvk162

while True:
    start_time = time.time()
    try:
      externalReading = max31865.get()
    except Exception: 
      pass
    
    try:
      internalTemp1, internalHumidity = dht.get(11)
    except Exception:
      pass
    
    try:
      lsm9ds1_readings = lsm9ds1.get()
    except Exception:
      pass

    try:
      accel_x, accel_y, accel_z = lsm9ds1_readings.get('acceleration')
    except Exception:
      pass

    try:
      mag_x, mag_y, mag_z = lsm9ds1_readings.get('magnetometer')
    except Exception:
      pass

    try:
      gyro_x, gyro_y, gyro_z = lsm9ds1_readings.get('gyroscope')
    except Exception:
      pass

    try:
      internalTemp2 = lsm9ds1_readings.get('temperature')
    except Exception:
      pass
    
    try:
      myRandom = lsm9ds1_readings.get('myRandom')
    except Exception:
      pass
    
    try:
      gps = gvk162.get()
    except Exception:
      pass

    print("\n------------------------------------------------")
    print(datetime.datetime.now())
    
    try:
      print("External Temp: {0:0.3f}C".format(externalReading))
    except Exception:
      pass
    
    try:
      print("Internal Temp: {:.3f}C  Humidity: {}% ".format(internalTemp1, internalHumidity))
    except Exception:
      pass
    
    try:
      print(
        "Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
            accel_x, accel_y, accel_z
        )
      )
    except Exception:
      pass

    try:
      print(
        "Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(mag_x, mag_y, mag_z)
      )
    except Exception:
      pass
      
    try:
      print(
        "Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
            gyro_x, gyro_y, gyro_z
        )
      )
    except Exception:
      pass

    try:
      print("Internal Temp 2: {0:0.3f}C".format(internalTemp2))
    except Exception:
      pass

    try:
      print("GPS Latitude: %s" % gps['latitude'])
      print("GPS Longitude: %s" % gps['longitude'])
      print("GPS Altitude: %s" % gps['altitude'])
      print("GPS Time: %s" % gps['gpsTime'])
    except Exception:
      pass

    elapsed = time.time() - start_time
    time.sleep(1.0 - elapsed)
