import atexit

from ecs import System
from socket_server import SocketServer
from ai_robot import JoystickMessage, SendMessageEvent


class ServerSystem(System):
    def __init__(self):
        super(ServerSystem, self).__init__()

        self.server = SocketServer()
        self.server.on_received += self.on_received
        self.server.start_server()

        atexit.register(self.exit)

    def process(self, world, components):
        self.event_system.receive(SendMessageEvent).subscribe(
            on_next=lambda evt: self.server.send_message(evt.message)
        )

    def exit(self):
        self.server.on_received -= self.on_received
        self.server.close()

    def on_received(self, sender, message: str = None):
        try:
            packed_message = message.to_packed_message()
            if packed_message == JoystickMessage:
                self.event_system.publish(packed_message.unpack(JoystickMessage))

            print(str.format("Get Message: {1}, From: {0}", packed_message.sender, packed_message.message))
        except Exception as e:
            print(e)
