import numpy

from ecs import System
from reactive_property import ReactiveProperty
from ai_robot import JoystickMessage, Transform, Vector3
from gpiozero import Robot


class MovementSystem(System):
    def __init__(self):
        super(MovementSystem, self).__init__()

        self.componenttypes = (Transform,)

    def process(self, world, components):
        for transform, in components:
            robot = Robot(left=(12, 16), right=(21, 20))
            position = transform.position  # type: ReactiveProperty
            position.distinct_until_changed().subscribe(
                on_next=lambda pos: {
                    setattr(robot, 'value', (numpy.clip(pos.y + pos.x, -1, 1), numpy.clip(pos.y - pos.x, -1, 1)))
                })
            self.event_system.receive(JoystickMessage).subscribe(
                on_next=lambda evt: setattr(position, 'value', Vector3(evt.axis.x, evt.axis.y, 0)))
