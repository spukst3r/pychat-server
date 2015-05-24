from utils import Command, loginRequired, joinedRoomRequired


class LeaveRoomCommand(Command):
    names = ('LEAVE ROOM', 'LEAVE', 'LEFT ROOM', 'LEFT')

    @loginRequired
    @joinedRoomRequired
    def _run(self, *args):
        self.user.leaveRoom()

        return "OK"


def mapping():
    return (LeaveRoomCommand.names, LeaveRoomCommand)
