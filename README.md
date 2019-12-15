# Dog Feeder

## Overview

The purpose of this project was to find a way to feed my dog on a regular cadence, as well as verify 
that she had been fed.  Major components include: Raspberry Pi (with camera, a Servo Motor and a 
breakfast cereal dispenser.  Various other bits of PVC and wood grafted everything together.

The servo motor was attached to the rotating part of the cereal dispenser in the place of the 
handle that would be normally used by a human to manually dispense food.  The program makes the servo
rotate the dispenser's knob, thus dispensing food for the dog.

The code that handled the servo operation was invoked by a cron job on the Rasbperry Pi, 
which was scheduled 4x a day, so that my dog would be fed equal servings at each meal.

The first iteration of the dog feeder can be seen in action [here](https://youtu.be/5L-E-7JgWd4).  
Below are two still photos of all the components, and the assembled final version.

![all-the-components](images/dog-feeder-1.jpg)

![assembled-final-version](images/dog-feeder-2.jpg)

A process was added to take a picture of the food in the bowl 
immediately after it was delivered, and then email that picture to me, so I could know how 
well she was fed (or not fed).

## Code

The code for this project is located in the [dog-feeder](dog-feeder/) directory.

`crontab.txt` shows the relevant invocation parameters, as well as starting the necessary 
daemons to ensure proper operation of the dog feeder from the Rasbperry Pi.  
As you can see in `crontab.txt`, the process was invoked by a shell script `feedDog.sh`.  
This shell script then invokes the `feed-dog.py` script, which handles all the logic around 
operating the servo, taking a photo after the food has been dispensed, and emailing the result.me

The [dog-feeder/test-scripts](dog-feeder/test-scripts) directory contains "scratch code" 
that was used to test various options for connecting to the servo, or the camera, etc.  
This represents iterative testing that ultimately resulted in the final product described above.

## Servo Power Circuit
The Pi's on-board power supply was insufficient to drive the servo.  An external suppy was needed 
directly from the transformer (Y cable adaptor), bypassing the Pi board's power circuts. 
A Darlinging transistor controlled by the Pi was added to allow the servo power to be cut when not in use, 
to prevent the motor from burning out.

Supplies:
* D645MW Digital Super Torque servo from HiTec
* TIP120 transistor
* 10,000 Ohm resistor
* USB Micro power adapter (5V) for a breadboard
* Y-Power Adapter (to power the Raspberry Pi and the Servo separately from the same outlet)
* small breadboard

![circuit diagram](images/dog-feeder-circuit.jpeg)

## History
This repository is a fork of [Kate's](https://github.com/kmfrett)
[home-projects](https://github.com/kmfrett/home-projects) repo at a time when it only contained the 
dog-feeder project.
Kate and I collaborated on the construction and coding of this feeder.