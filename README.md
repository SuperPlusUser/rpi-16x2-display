# RPi: 16x2 I2C Display

## 1 Description

In this tutorial I show how to use a 16x2 I2C display on the Raspberry Pi.

For a more detailed description visit my website:

- [English](http://deloarts.com/en/scripts/raspberry/16x2-display)
- [German](http://deloarts.com/de/scripts/raspberry/16x2-display)

### 1.1 Components

- Raspberry Pi 2
- 16x2 I2C LCD
- Logic Level Shifter

### 1.2 Pinout
 Raspberry Pi | Level Shifter | I2C Display
--------------|---------------|-------------
 GND (Pin 6)  | GND           | GND
 3V3 (Pin 1)  | LV            | /
 SDA (Pin 3)  | LV1           | /
 SCL (Pin 5)  | LV2           | /
 5V (Pin2)    | HV 			  | Vcc
 /            | HV1           | SDA
 /            | HV2           | SCL

## 2 License

This project is licensed under the GNU GPLv3 open source license. Thus anybody is allowed to copy and modify the source code, provided all changes are open source too and the author is in knowledge of all done changes. This can happen either via eMail or directly on GitHub, in other words at this repository.

## 3 Disclaimer

I am not responsible for anything in conjunction with this project, including bugs, failure, fire, harm of equipment and harm of persons. Reasonably foreseeable misapplication:

- Bug in the code
- Failure of used parts due to a bug in the code or a wrong wiring diagram, including a wrong design.
- Fire due to a wrong wiring diagram, including a wrong design.
- Harm of equipment, meaning third party parts (cameras, flashes, etc.) due to a bug in the code or a wrong wiring diagram, including a wrong design.
- Harm of persons due to any failure of the system, a wrong wiring diagram or a wrong behaviour.

**It is your own responsibility to use these contents**. Be careful, this project includes lethal electrical voltage. Put yourself in knowledge about the risks before you start with this project.