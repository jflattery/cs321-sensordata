import time
import datetime
import dht11
import max31865
import lsm9ds1

while True:
    start_time = time.time()
    externalReading = max31865.get()

    internalTemp1, internalHumidity = dht11.get()

    lsm9ds1_readings = lsm9ds1.get()
    accel_x, accel_y, accel_z = lsm9ds1_readings.get('acceleration')
    mag_x, mag_y, mag_z = lsm9ds1_readings.get('magnetometer')
    gyro_x, gyro_y, gyro_z = lsm9ds1_readings.get('gyroscope')
    internalTemp2 = lsm9ds1_readings.get('temperature')
    myRandom = lsm9ds1_readings.get('myRandom')

    print(datetime.datetime.now())
    print("External Temp: {0:0.3f}C".format(externalReading))
    print("Internal Temp: {:.3f}C  Humidity: {}% ".format(internalTemp1, internalHumidity))
    print(
        "Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
            accel_x, accel_y, accel_z
        )
    )
    print(
        "Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(mag_x, mag_y, mag_z)
    )
    print(
        "Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
            gyro_x, gyro_y, gyro_z
        )
    )
    print("Internal Temp 2: {0:0.3f}C".format(internalTemp2))
    print("------------------------------------------------")

    elapsed = time.time() - start_time
    time.sleep(1.0 - elapsed)
