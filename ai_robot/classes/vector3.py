from json_utility import JsonUtility


@JsonUtility.register
class Vector3:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    @staticmethod
    def zero():
        return Vector3(0, 0, 0)

    @staticmethod
    def one():
        return Vector3(1, 1, 1)
