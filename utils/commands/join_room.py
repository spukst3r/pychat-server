from utils import Command
from utils.commands.login import loginRequired


class JoinRoomCommand(Command):
    names = ('JOIN ROOM', 'JOIN')

    @loginRequired
    def _run(self, *args):
        try:
            roomName = args[0]
        except IndexError:
            raise Exception("Missing required parameter")

        self.user.joinRoom(roomName)

        map(lambda user: self.sendMessage({
            'from': self.user,
            'to': user,
            'type': "userJoined",
            'body': "User {} has joined the room".format(self.user.name),
        }), self.user.room.users.values())

        return "Joined room {}".format(self.user.room.name)


def joinedRoomRequired(func):
    def wrapper(self, *args, **kwargs):
        if not self.user.room:
            raise Exception("Join a room first")

        return func(self, *args, **kwargs)

    return wrapper


def mapping():
    return (JoinRoomCommand.names, JoinRoomCommand)
