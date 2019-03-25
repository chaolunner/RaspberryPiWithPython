from gpiozero import Robot
from time import sleep

robot = Robot((4, 14), (17, 27))

robot.forward()
sleep(5)
robot.backward()
sleep(5)
robot.right()
sleep(5)
robot.left()
sleep(5)
