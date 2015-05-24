from room import getRoom


class ChatUser(object):
    def __init__(self, name, transport):
        self.name = name
        self.transport = transport
        self.room = None

    def joinRoom(self, roomName):
        room = getRoom(roomName)

        if self.room:
            self.leaveRoom()

        room.addUser(self)
        self.room = room

    def leaveRoom(self):
        if not self.room:
            raise Exception("No room to leave")

        self.room.removeUser(self.name)
        self.room = None
