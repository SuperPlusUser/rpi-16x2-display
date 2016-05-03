#16x2 I2C Display on Raspberry Pi

Here I show how to use a 16x2 I2C display on the Raspberry Pi.

###Components
- Raspberry Pi 2
- 16x2 I2C LCD
- Logic Level Shifter

###Pinout
 Raspberry Pi | Level Shifter | I2C Display
--------------|---------------|-------------
 GND (Pin 6)  | GND           | GND
 3V3 (Pin 1)  | LV            | 
 SDA (Pin 3)  | LV1           |
 SCL (Pin 5)  | LV2           |
 5V (Pin2)    | HV 			  | Vcc
              | HV1           | SDA
              | HV2           | SCL

For more information, please visit my blog:
www.deloarts.wordpress.com