import serial
import capture_func
from time import sleep

def active(command):
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    sleep(2)
    command = ""
    ser.write((command + '\n').encode()) 
    ser.close()

def passive():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    sleep(2)
    command = "passive"
    ser.write((command + '\n').encode()) 
    ser.close()

def toggle(command):
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    sleep(2)
    command = "toggle"
    ser.write((command + '\n').encode()) 
    ser.close()
    capture_func.capture()
