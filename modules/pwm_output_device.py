from gpiozero import PWMOutputDevice
from time import sleep

a = PWMOutputDevice(4)

for i in range(1, 11):
    speed = i / 10
    print(speed)
    a.value = speed
    sleep(0.5)
