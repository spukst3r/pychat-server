from utils import Command


class MessageCommand(Command):
    names = ('MESSAGE',)
    default = True

    def _run(self, *args):
        if not self.user.name:
            raise Exception("Login required")

        if not self.user.room:
            raise Exception("Join a room first")

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
