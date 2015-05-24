from utils import Command
from utils.commands.join_room import joinedRoomRequired
from utils.commands.login import loginRequired

from dateutil import parser as dateparser


class HistoryCommand(Command):
    names = ('HISTORY',)

    @loginRequired
    @joinedRoomRequired
    def _run(self, *args):
        room = self.user.room
        fromDate = None
        toDate = None
        timestamp = {}
        doc = {'room': room.name}

        try:
            args = args[0].split(' ')
            fromDate = args[0]
            toDate = args[1]
        except IndexError:
            pass

        if fromDate:
            timestamp['$gte'] = dateparser.parse(fromDate)

        if toDate:
            timestamp['$lte'] = dateparser.parse(toDate)

        if timestamp:
            doc.update({
                'utctimestamp': timestamp
            })

        collection = self.db.messages

        return collection.find(doc).addCallback(self.processResults)

    def processResults(self, results):
        map(lambda doc: self.sendMessage({
            'from': self.user,
            'to': self.user,
            'type': "history",
            'body': HistoryCommand.formatDoc(doc),
        }), results)

    @staticmethod
    def formatDoc(doc):
        del doc['_id']

        return doc


def mapping():
    return (HistoryCommand.names, HistoryCommand)
