import sys
import Pyro4
import threading

class CodeClubNetworkClient:
	def __init__(self):
		sys.excepthook=Pyro4.util.excepthook
		self.daemon = Pyro4.Daemon(host=Pyro4.socketutil.getInterfaceAddress("www.google.com"))
		self.t = None

	def connect_to_object_on_network(self, name):
		return Pyro4.Proxy("PYRONAME:"+name)

	def make_local_object_available_on_network(self, local_object):
		uri = self.daemon.register(local_object)
		# Stop and restart daemon thread to make sure latest object registered
		if self.t != None:
			self.daemon.shutdown()
			self.t.join()
		self.t = threading.Thread(target=lambda: self.daemon.requestLoop())
		self.t.daemon = True
		self.t.start()
		return uri

	def handle_network_requests(self):
		socks=daemon.getServerSockets()
		ins,outs,exs=select.select(socks,[],[],2)
		for s in socks:
			if s in ins:
				daemon.handleRequests()
				break
