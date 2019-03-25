from json_utility import JsonUtility


@JsonUtility.register
class PackedMessage:
    def __init__(self, message: str = None, type: str = None, sender: str = "Python"):
        self.message = message
        self.type = type
        self.sender = sender

    def __eq__(self, other):
        return self.type.__eq__(other.__name__)
