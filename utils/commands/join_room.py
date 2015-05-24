from utils import Command, loginRequired


class JoinRoomCommand(Command):
    names = ('JOIN ROOM', 'JOIN')

    @loginRequired
    def _run(self, *args):
        try:
            roomName = args[0]
        except IndexError:
            raise Exception("Missing required parameter")

        self.user.joinRoom(roomName)

        return "Joined room {}".format(self.user.room.name)


def mapping():
    return (JoinRoomCommand.names, JoinRoomCommand)
