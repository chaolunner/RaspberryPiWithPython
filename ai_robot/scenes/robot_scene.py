import inject

from ai_robot import Robot, MovementSystem, SerialSystem, ServerSystem
from message_broker import MessageBroker
from scene import Scene
from ecs import World


class RobotScene(Scene):
    def __init__(self):
        super(RobotScene, self).__init__()
        # create world
        self.world = World()
        # create entities
        self.robot = Robot(self.world)
        # create systems
        self.movement_system = MovementSystem()
        self.serial_system = SerialSystem()
        self.server_system = ServerSystem()
        # add systems to world
        self.world.add_system(self.movement_system)
        self.world.add_system(self.serial_system)
        self.world.add_system(self.server_system)
        # enable systems
        self.world.process()

        while True:
            pass

    def bindings(self):
        inject.clear_and_configure(lambda binder:
                                   binder.bind(MessageBroker, MessageBroker())
                                   )


if __name__ == '__main__':
    robot = RobotScene()
