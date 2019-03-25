from ecs import Entity, World
from ai_robot import Transform, Vector3


class Robot(Entity):
    def __init__(self, world: World, pos: Vector3 = Vector3.zero()):
        super(Robot, self).__init__(world)

        self.transform = Transform(pos)
