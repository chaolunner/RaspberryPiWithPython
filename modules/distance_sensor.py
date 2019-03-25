from gpiozero import DistanceSensor
from signal import pause

ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5, max_distance=2)


def in_range():
    print("In Range : " + ultrasonic.distance.__str__())


def out_of_range():
    print("Out of Range : " + ultrasonic.distance.__str__())


ultrasonic.when_in_range = in_range
ultrasonic.when_out_of_range = out_of_range

pause()
