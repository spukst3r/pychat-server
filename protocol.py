import json
from twisted.protocols import basic

from user import ChatUser


class ChatServerProtocol(basic.LineReceiver):
    def connectionMade(self):
        self.user = ChatUser(None, self.transport)

    def connectionLost(self, reason):
        # TODO: notify other users in the room about disconnecting
        self.user.tearDown()

    def lineReceived(self, line):
        Command, args = self.getCommand(line)

        command = Command(self.user, self.factory.db)
        d = command.run(args)

        def success(reply):
            result = {
                'result': reply,
                'type': 'commandResult',
            }

            self.transport.write(json.dumps(result))

            map(self.sendMessage, command.messageQueue)

        def fail(f):
            result = {
                'error': f.getErrorMessage(),
                'type': 'error',
            }

            self.transport.write(json.dumps(result))

        d.addCallback(success)
        d.addErrback(fail)

    def sendMessage(self, msg):
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
