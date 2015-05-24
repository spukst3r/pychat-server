from twisted.internet import protocol

from protocol import ChatServerProtocol
from utils import getCommands


class ChatServerFactory(protocol.ServerFactory):
    protocol = ChatServerProtocol

    def __init__(self):
        self.users = {}
        self.commands = getCommands('utils/commands')

    def addUser(self, user):
        if user.name in self.users:
            pass
        else:
            pass
