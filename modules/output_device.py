from gpiozero import OutputDevice
from time import sleep

a = OutputDevice(4)
b = OutputDevice(14)

for i in range(1):
    b.off()
    a.on()
    sleep(5)
    a.off()
    b.on()
    sleep(5)
