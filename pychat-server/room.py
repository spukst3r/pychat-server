import re


class ChatRoom(object):
    def __init__(self, roomName):
        if not re.match(r'^[a-zA-Z0-9]*$', roomName):
            raise Exception("Invalid room name: {}, please use alphanumeric"
                            "characters only".format(roomName))

        self.name = roomName
        self.users = {}

    def removeUser(self, userName):
        self.users.pop(userName)

    def addUser(self, user):
        self.users[user.name] = user

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


def roomFactory(func):
    rooms = {}

    def wrapper(roomName):
        if roomName not in rooms:
            rooms[roomName] = func(roomName)

        return rooms[roomName]

    return wrapper


@roomFactory
def getRoom(roomName):
    return ChatRoom(roomName)
