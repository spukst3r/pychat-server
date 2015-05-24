import re
from utils import Command


class LoginCommand(Command):
    names = ('LOGIN',)

    @staticmethod
    def validateNick(login):
        r = re.compile(r'^[0-9a-zA-Z]{3,16}$')

        return r.match(login) is not None

    def _run(self, *args):
        if self.user.name:
            raise Exception("User already logged in with name {}"
                            .format(self.user.name))

        try:
            nick = args[0]
            if not nick:
                raise IndexError()
        except IndexError:
            raise Exception("Missing required parameter")

        if not LoginCommand.validateNick(nick):
            raise Exception("Invalid nickname")

        self.user.name = nick

        return "Username set to {}".format(self.user.name)


def mapping():
    return (LoginCommand.names, LoginCommand)
