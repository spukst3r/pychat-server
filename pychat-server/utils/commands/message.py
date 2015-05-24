from utils import Command
from utils.commands.join_room import joinedRoomRequired
from utils.commands.login import loginRequired


class MessageCommand(Command):
    names = ('MESSAGE',)
    default = True

    @loginRequired
    @joinedRoomRequired
    def _run(self, *args):
        try:
            message = args[0]
        except IndexError:
            raise Exception("Missing required parameter")

        def send(user):
            self.sendMessage({
                'to': user,
                'from': self.user,
                'body': message,
                'type': 'message',
            })

        map(send, self.user.room.users.values())

        return "OK"


def mapping():
    return (MessageCommand.names, MessageCommand)
