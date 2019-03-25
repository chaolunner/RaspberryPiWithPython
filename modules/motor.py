from gpiozero import Motor
from time import sleep

motor = Motor(4, 14)

motor.forward()
while True:
    sleep(5)
    motor.reverse()
