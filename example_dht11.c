/*
 *	Simple test program to test the wiringPi functions
 *	DHT11 test
 */

#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define MAXTIMINGS	85
int dht11_dat[5] = { 0, 0, 0, 0, 0 };

/*
* These variables hold the strings of data; If reading fails, 
* previous successful reading will be held
*/
char temperature[100];
char humidity[100];

/*
* This function will read the data stream from the dht11 data wire.
* The data wire sends bits that the raspberry pi can track. 
* The length of the high-voltage-level signal decides whether the bit is “0” or “1”.
* You can read more about this here:
*     http://www.uugear.com/portfolio/dht11-humidity-temperature-sensor-module/
*/
void read_dht11_dat(int dht_pin_number)
{
  const int DHTPIN = dht_pin_number;
	uint8_t laststate	= HIGH;
	uint8_t counter		= 0;
	uint8_t j		= 0, i;
	float	f; /* fahrenheit */

	dht11_dat[0] = dht11_dat[1] = dht11_dat[2] = dht11_dat[3] = dht11_dat[4] = 0;

	/* pull pin down for 18 milliseconds */
	pinMode( DHTPIN, OUTPUT );
	digitalWrite( DHTPIN, LOW );
	delay( 18 );
	/* then pull it up for 40 microseconds */
	digitalWrite( DHTPIN, HIGH );
	delayMicroseconds( 40 );
	/* prepare to read the pin */
	pinMode( DHTPIN, INPUT );

	/* detect change and read data */
	for ( i = 0; i < MAXTIMINGS; i++ )
	{
		counter = 0;
		while ( digitalRead( DHTPIN ) == laststate )
		{
			counter++;
			delayMicroseconds( 1 );
			if ( counter == 255 )
			{
				break;
			}
		}
		laststate = digitalRead( DHTPIN );

		if ( counter == 255 )
			break;

		/* ignore first 3 transitions */
		if ( (i >= 4) && (i % 2 == 0) )
		{
			/* shove each bit into the storage bytes */
			dht11_dat[j / 8] <<= 1;
			if ( counter > 16 )
				dht11_dat[j / 8] |= 1;
			j++;
		}
	}

	/*
	 * check we read 40 bits (8bit x 5 ) + verify checksum in the last byte
	 * print it out if data is good
	 */
	if ( (j >= 40) &&
	     (dht11_dat[4] == ( (dht11_dat[0] + dht11_dat[1] + dht11_dat[2] + dht11_dat[3]) & 0xFF) ) )
	{
		f = dht11_dat[2] * 9. / 5. + 32;
		sprintf(humidity, "Humidity = %d.%d %% ", dht11_dat[0], dht11_dat[1]);
    sprintf(temperature, "Temperature = %d.%d *C (%.1f *F)\n", dht11_dat[2], dht11_dat[3], f );
	}
}

/*
* The main function will check if wiringPi has been properly setup, and
* print the sensors
*/
int main( void )
{
	printf( "Raspberry Pi wiringPi DHT11 Temperature test program\n" );

  /*
  * If wiringpi is not functioning properly, exit
  */
	if ( wiringPiSetup() == -1 )
		exit( 1 );

  /*
  * Infinite loop, calls the read_dht11 function every second and prints string vars
  */
	while ( 1 )
	{
    /*
    * Read the data stream from gpio pin 7
    */
		read_dht11_dat(7);
    /*
    * If the data strings are greater than 0 (i.e. data was sent sucessfully) then we can print
    * the data and delay for a second
    */
    if ( (strlen(temperature) > 0) && (strlen(humidity) > 0) ) {
      printf("%s%s", humidity, temperature);
		  delay( 1000 ); /* wait 1sec to refresh */
    }
	}

	return(0);
}
