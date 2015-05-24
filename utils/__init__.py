import pkgutil
import sys
import datetime

from twisted.internet import defer
from twisted.python import log


class Command(object):
    names = ()
    default = False

    def __init__(self, user, db):
        self.user = user
        self.messageQueue = []
        self.db = db

    @defer.inlineCallbacks
    def run(self, *args):
        result = yield self._run(*args)

        defer.returnValue(result)

    def sendMessage(self, msg):
        collection = self.db.messages
        msg.update({
            'utctimestamp': datetime.datetime.utcnow(),
            'room': self.user.room,
        })

        self.messageQueue.append(msg)

        doc = dict(map(lambda (k, v): (k, str(v)), msg.items()))

        if msg['type'] != 'history':
            return collection.insert(doc, safe=True)

    def _run(self, *args):
        raise NotImplementedError()


def getCommands(directory):
    def registerCommand(args):
        importer, package_name, _ = args

        if package_name not in sys.modules:
            module = (importer
                      .find_module(package_name)
                      .load_module(package_name))

            if callable(getattr(module, 'mapping', None)):
                mapping = module.mapping()

                log.msg("Registering commands {}".format(mapping[1]))

                return mapping

    return dict(filter(None, map(registerCommand,
                                 pkgutil.walk_packages([directory]))))
