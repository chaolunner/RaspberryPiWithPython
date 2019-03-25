from json_utility import JsonUtility
from ai_robot import RawMessage, Vector2


@JsonUtility.register
class JoystickMessage(RawMessage):
    def __init__(self, axis: Vector2 = Vector2.zero(), identifier: int = 0):
        self.identifier = identifier
        self.axis = axis
