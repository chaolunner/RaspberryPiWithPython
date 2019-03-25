from ecs import Component
from ai_robot import Vector3
from reactive_property import ReactiveProperty


class Transform(Component):
    def __init__(self, pos: Vector3 = Vector3.zero()):
        super(Transform, self).__init__()

        self.position = ReactiveProperty(pos)
