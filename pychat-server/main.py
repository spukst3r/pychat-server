from twisted.application import service, internet
from factory import ChatServerFactory

application = service.Application('pychat-server')
factory = ChatServerFactory()

internet.TCPServer(9090, factory).setServiceParent(
    service.IServiceCollection(application))
