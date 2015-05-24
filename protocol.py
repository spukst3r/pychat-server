from twisted.protocols import basic

from user import ChatUser


class ChatServerProtocol(basic.LineReceiver):
    def connectionMade(self):
        self.user = ChatUser(None)

    def lineReceived(self, line):
        Command, args = self.getCommand(line)

        d = Command(self.user).run(args)

        def success(reply):
            self.transport.write(reply + '\n\r')

        def fail(f):
            self.transport.write(f.getErrorMessage() + '\n\r')

        d.addCallback(success)
        d.addErrback(fail)

    def getCommand(self, line):
        default = None

        for names, Command in self.factory.commands.items():
            for name in names:
                if line.startswith(name):
                    return Command, line.replace(name, '').lstrip()

            if Command.default:
                default = Command

        return default, line
