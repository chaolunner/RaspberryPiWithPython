import atexit

from ecs import System
from serial_handler import SerialHandler
from ai_robot import JoystickMessage, SendMessageEvent


class SerialSystem(System):
    def __init__(self):
        super(SerialSystem, self).__init__()

        self.serial_handler = SerialHandler()
        self.serial_handler.on_data_received += self.on_data_received
        self.serial_handler.open()

        atexit.register(self.exit)

    def process(self, world, components):
        self.event_system.receive(SendMessageEvent).subscribe(
            on_next=lambda evt: self.serial_handler.write(evt.message)
        )

    def exit(self):
        self.serial_handler.on_data_received -= self.on_data_received

    def on_data_received(self, sender, message: str = None):
        packed_message = message.to_packed_message()
        if packed_message == JoystickMessage:
            self.event_system.publish(packed_message.unpack(JoystickMessage))

        print(str.format("Get Message: {1}, From: {0}", packed_message.sender, packed_message.message))
