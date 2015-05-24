from room import getRoom


class ChatUser(object):
    def __init__(self, name):
        self.name = name
        self.rooms = {}
        self.room = None

    def joinRoom(self, roomName):
        room = getRoom(roomName)

        if self.room:
            self.leaveRoom()

        room.addUser(self)
        self.rooms[roomName] = room
        self.room = room

    def leaveRoom(self):
        if not self.room:
            raise Exception("No room to leave")

        self.room.removeUser(self.name)
        self.rooms.pop(self.room.name)

        self.room = None
