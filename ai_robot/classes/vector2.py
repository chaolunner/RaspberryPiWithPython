from json_utility import JsonUtility


@JsonUtility.register
class Vector2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def zero():
        return Vector2(0, 0)

    @staticmethod
    def one():
        return Vector2(1, 1)
