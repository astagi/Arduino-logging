#!/usr/bin/python
import serial, sys, time

if len(sys.argv) != 3:
    print "Usage: logging.py dev baudrate"
    exit(0)

ser = serial.Serial(sys.argv[1], sys.argv[2])
time.sleep(2)
while True:
    print ser.readline()