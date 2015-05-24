from utils import Command
from utils.commands.join_room import joinedRoomRequired
from utils.commands.login import loginRequired


class LeaveRoomCommand(Command):
    names = ('LEAVE ROOM', 'LEAVE', 'LEFT ROOM', 'LEFT')

    @loginRequired
    @joinedRoomRequired
    def _run(self, *args):
        room = self.user.room

        self.user.leaveRoom()

        map(lambda user: self.sendMessage({
            'from': self.user,
            'to': user,
            'type': "userLeft",
            'body': "User {} has left the room".format(self.user.name)
        }), room.users.values())

        return "OK"


def mapping():
    return (LeaveRoomCommand.names, LeaveRoomCommand)
