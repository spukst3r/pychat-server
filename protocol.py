import json
from twisted.protocols import basic

from user import ChatUser


class ChatServerProtocol(basic.LineReceiver):
    def connectionMade(self):
        self.user = ChatUser(None, self.transport)

    def lineReceived(self, line):
        Command, args = self.getCommand(line)

        command = Command(self.user)
        d = command.run(args)

        def success(reply):
            self.transport.write(reply + '\n\r')

            map(self.sendMessage, command.messageQueue)

        def fail(f):
            self.transport.write(f.getErrorMessage() + '\n\r')

        d.addCallback(success)
        d.addErrback(fail)

    def sendMessage(self, msg):
        print "sendMessage({})".format(msg)
        msg['to'].transport.write(json.dumps({
            'from': msg['from'].name,
            'type': msg['type'],
            'body': msg['body'],
        }))

    def getCommand(self, line):
        default = None

        for names, Command in self.factory.commands.items():
            for name in names:
                if line.startswith(name):
                    return Command, line.replace(name, '').lstrip()

            if Command.default:
                default = Command

        return default, line
