import threading

class lock(object):
	def __init__(self,src):
		self.event = threading.Event()
		self.s = src
		self.event.set()

	def __enter__(self):
		self.event.wait()
		self.event.clear()
		
	def __exit__(self,a,b,c):
		self.event.set()
	
	def __str__(self):
		return "Secured "+str(self.src)
