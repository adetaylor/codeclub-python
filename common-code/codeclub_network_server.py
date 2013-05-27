import sys
import Pyro4
import threading

class CodeClubNetworkServer:
	def __init__(self):
		sys.excepthook=Pyro4.util.excepthook
		self.daemon = Pyro4.Daemon(host=Pyro4.socketutil.getInterfaceAddress("www.google.com"))

	def make_local_object_available_on_network(self, label, local_object):
		ns = Pyro4.locateNS()
		uri = self.daemon.register(local_object)
		ns.register(label, uri)

	def handle_requests_forever(self):
		self.daemon.requestLoop()
