# CS321-007: HAB Sensor Data
## Objective: To expose sensor reading data via a realtime JSON formated data stream as well as a historic data file which contains all readings over a period of time.
## Sensors Used:
* Velleman VMA311 (DHT11) [[Microcenter](https://www.microcenter.com/product/613629/velleman-dht11-digital-temperature-humidity-sensor-module-for-arduino)]
  * 3 or 5V power
  * 2.5mA max current use during conversion (while requesting data)
  * Good for 20-80% humidity readings with 5% accuracy
  * Good for 0-50°C temperature readings ±2°C accuracy
  * No more than 1 Hz sampling rate (once every second)
* DHT22 [**¿ _VENDOR_ ?**]
  * 3 or 5V power
  * 2.5mA max current use during conversion (while requesting data)
  * Good for 0-100% humidity readings with 2-5% accuracy
  * Good for -40 to 80°C temperature readings ±0.5°C accuracy
  * No more than 0.5 Hz sampling rate (once every 2 seconds)
* VK-162 G-Mouse GPS [[Amazon](https://www.amazon.com/gp/product/B078Y52FGQ)]
  * Data baud rate: 9600 (default) (optional: 4800, 19200, 38400, 57600, 115200, etc.) 
  * Data refresh rate: 1Hz-10Hz refresh rate (can be set to output data 1-10 times per second). 
  * NMEA-0183 protocol output 
  * C/A code, 1.023MHz stream
  * Receive Band: L1 [1575.42MHz]
  * Tracking Channels: 50
  * Support DGPS [WAAS, EGNOS and MSAS]
  * Positioning performance
    * 2D plane: 5m [average]
    * 2D plane: 3.5m [average], there DGPS auxiliary.
    * Drift: <0.02m / s
    * Timing Accuracy: 1us
    * Reference coordinate system: WGS-84
    * Maximum altitude: 18,000 m
    * Maximum speed: 500m / s
    * Acceleration: <4g
  * Electrical properties:
    * Tracking sensitivity:-160dBm
    * Acquisition sensitivity:-146dBm
    * Cold Start Time: 32s [average]
    * Warm start time: 32s [average]
    * Hot start time: 1s [average]
    * Recapture Time: 0.1s [average]
    * Operating temperature: -30 ℃ to +80 ℃
    * Package size:  49 * 38 * 16mm;
    * Cable length 2m
* Adafruit LSM9DS1 [[Adafruit](https://www.adafruit.com/product/3387)]
  * Accelerometer ranges: ±2/±4/±8/±16 g (no ±6 g range)
  * Magnetometer ranges: ±4/±8/±12/±16 gauss
  * Gyroscope ranges: ±245/±500/±2000 dps
* Adafruit MAX31865 [[Adafruit](https://www.adafruit.com/product/3328)]
  * SPECS
* Adafruit PT100 [[Adafruit](https://www.adafruit.com/product/3290)]
  * SPECS

## Assembly
![Fritzing Diagram](gpio-sensor-diagram.png)
### LSM9Ds1 Pinout
  * Vin - this is the power pin. Chip includes a voltage regulator on board that will take either 3 or 5VDC.
    * RPi 3V3 to sensor VIN
  * 3V3 - this is the 3.3V output from the voltage regulator, you can grab up to 100mA from this if you like
    * Not Used
  * GND - common ground for power and logic
    * RPi GND to sensor GND
  * SCL - this is also the SPI clock pin, it's level shifted so you can use 3-5V logic input
    * RPi SCLK to sensor SCL
  * SDA - this is also the SPI MOSI pin, it's level shifted so you can use 3-5V logic input
    * Pi MOSI to sensor SDA
  * CSAG - this is the Accelerometer+Gyro subchip Chip Select, it's level shifted so you can use 3-5V logic input
    * RPi GPIO5 to sensor CSAG
  * CSM - this is the Magnetometer subchip Select, it's level shifted so you can use 3-5V logic input
    * RPi GPIO6 to sensor CSM
  * SDOAG - this is the Accelerometer+Gyro subchip MISO pin - it's 3V logic out, but can be read properly by 5V logic chips.
    * RPi MISO to sensor SDOAG AND sensor SDOM
  * SDOM - this is the Magnetometer subchip MISO pin - it's 3V logic out, but can be read properly by 5V logic chips.
    * RPi MISO to sensor SDOAG AND sensor SDOM

### MAX31865 Pinout
  * Vin - this is the power pin. Chip includes a voltage regulator on board that will take either 3 or 5VDC.
    * RPi 3V3 to sensor VIN
  * 3Vo - this is the 3.3V output from the voltage regulator, you can grab up to 100mA from this if you like
    * Not Used
  * GND - common ground for power and logic
    * RPi GND to sensor GND
  * SCK - This is the SPI Clock pin, its an input to the chip
    * 
  * SDO - this is the Serial Data Out / Master In Slave Out pin, for data sent from the MAX31865 to your processor
  * SDI - this is the Serial Data In / Master Out Slave In pin, for data sent from your processor to the MAX31865
  * CS - this is the Chip Select pin, drop it low to start an SPI transaction. Its an input to the chip

## Setup
Do an update if you have not already done one today:
```bash
sudo apt update && sudo apt upgrade -y
```
If not already installed install Docker:
```bash 
curl -sSL https://get.docker.com | sh
```
Add your self to the docker group so you don't have to type sudo every time to use it:
```bash
boldsudo usermod -aG docker $USER
```
If not already installed install git:
```bash
sudo apt install git -y
```
Download the repo
```bash
git clone git@github.com:jflattery/cs321-sensordata.git
```
Change your currernt directory to the newly created one
```bash
cd ___
```
If not already enabled, enable SPI:
```bash
raspi-config nonint do_spi 0
```
Spin up a new container and LGTM:
```bash
docker run --privileged -it --rm --name conductor -v "$PWD":/usr/src/myapp -w /usr/src/myapp circuit-python:latest python app/conductor.py
```
## Known Issue(s)
