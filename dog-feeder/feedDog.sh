#!/bin/bash

# Invoke dog feeder python script
/usr/bin/python /home/pi/DogFeeder/feed-dog.py >> /home/pi/DogFeeder/logs/log.txt 2>&1
