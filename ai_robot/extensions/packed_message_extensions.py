from forbiddenfruit import curse
from json_utility import JsonUtility
from ai_robot import PackedMessage, RawMessage, SendMessageEvent


def pack(self):
    message = JsonUtility.to_json(self)
    return JsonUtility.to_json(PackedMessage(message, type(self).__name__))


def to_event(self):
    return SendMessageEvent(self.pack())


def to_packed_message(self: str):
    return JsonUtility.from_json(self)


def unpack(self, type: type, sender: str = None):
    if sender is not None and self.sender is not sender:
        return None
    if self == type:
        return JsonUtility.from_json(self.message)
    return None


curse(RawMessage, "pack", pack)
curse(RawMessage, "to_event", to_event)
curse(str, "to_packed_message", to_packed_message)
curse(PackedMessage, "unpack", unpack)
