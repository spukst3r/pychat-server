from utils import Command


class JoinRoomCommand(Command):
    names = ('JOIN ROOM',)

    def _run(self, *args):
        if not self.user.name:
            raise Exception("Login required")

        try:
            roomName = args[0]
        except IndexError:
            raise Exception("Missing required parameter")

        self.user.joinRoom(roomName)

        return "Joined room {}".format(self.user.room.name)


def mapping():
    return (JoinRoomCommand.names, JoinRoomCommand)
