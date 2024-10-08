import RPi.GPIO as GPIO
from time import sleep

# GPIO 포트 설정
MOTOR_PIN_SIG = 12
MOTOR_PIN_5V = 6
MOTOR_PIN_GND = 5

# 서보의 주기
SERVO_MAX_DUTY = 12.5
SERVO_MIN_DUTY = 2.5
# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN_SIG, GPIO.OUT)
GPIO.setup(MOTOR_PIN_5V, GPIO.OUT)
GPIO.setup(MOTOR_PIN_GND, GPIO.OUT)

# 소프트웨어 PWM 설정 (주기 50Hz)
servo = GPIO.PWM(MOTOR_PIN_SIG, 50)
servo.start(0)  # PWM 신호 시작

# 초기 상태로 설정
GPIO.output(MOTOR_PIN_5V, GPIO.HIGH)  # 5V 전원 공급
GPIO.output(MOTOR_PIN_GND, GPIO.LOW)  # GND


def setServoPos(degree):
  if degree > 180:
    degree = 180

# 각도(degree)를 duty로 변경한다.
  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)

# print("Degree: {} to {}(Duty)".format(degree, duty))

  servo.ChangeDutyCycle(duty)
  sleep(0.5)

def toggle():
  setServoPos(90)
  sleep(1)
  setServoPos(0)
  sleep(1)
  
  servo.ChangeDutyCycle(0)

def clean():
  servo.stop()
  GPIO.cleanup() 

