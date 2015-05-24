from room import getRoom


class ChatUser(object):
    def __init__(self, name, transport):
        self.name = name
        self.transport = transport
        self.room = None

    def joinRoom(self, roomName):
        room = getRoom(roomName)

        if self.name in room.users:
            raise Exception("User with such nickname is already present in "
                            "the requested room")

        if self.room:
            self.leaveRoom()

        room.addUser(self)
        self.room = room

    def leaveRoom(self):
        if not self.room:
            raise Exception("No room to leave")

        self.room.removeUser(self.name)
        self.room = None

    def tearDown(self):
        if self.room:
            self.leaveRoom()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
