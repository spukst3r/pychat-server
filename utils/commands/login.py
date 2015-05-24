from utils import Command


class LoginCommand(Command):
    names = ('LOGIN',)

    def _run(self, *args):
        if self.user.name:
            raise Exception("User already logged in with name {}"
                            .format(self.user.name))

        try:
            nick = args[0]
        except IndexError:
            raise Exception("Missing required parameter")

        self.user.name = nick

        return "Username set to {}".format(self.user.name)


def mapping():
    return (LoginCommand.names, LoginCommand)
