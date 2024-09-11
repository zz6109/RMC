# RPI Programing

![Screenshot-4](https://github.com/user-attachments/assets/492bb45f-4fa7-4aba-83c7-4e38d8e41dfb)

## Implementation of an air conditioner power toggle system using the Telegram bot library
<hr/>

## To run the "pip install" command, it can only be done in a "venv" environment.

## Before writing the code, the necessary preparations...

## USB_camera, Servo_moter, dht11, arduino_uno, rpi3b+(I used the 3B+ version, but you can use a higher one. However, I cannot take responsibility for any issues that arise from using a different version.), The implemented SQL server

## The required action is to connect the RPi and Arduino Uno via USB.

![IMG_20240911_110046](https://github.com/user-attachments/assets/e4111ddd-9878-4b31-b885-3053c9c46d5c)

<hr/>
These codes work in the same network environment, but accessing from external IPs to external IPs requires a VPN server protocol.
So, I plan to set up a VPN server using SoftEther VPN additionally.
<hr/>

### ✅ 1. Automatically run Telegram Bot after booting

### ✅ 2. Upload temperature and humidity value to sql server (real time-1 minute cycle)

### ✅ 3. Operate the servo motor at a certain temperature (25 degrees Celsius) or higher

### 4. After the servomotor operation, take a picture of the controller with the USB camera and check whether the controller is turned on or not, then operate the thermomotor again

### 5. If it is confirmed that it is turned on, send it to the Telegram

### 6. Add manual on/off (toggle) function

### 7. To be added after implementing the VPN server...
