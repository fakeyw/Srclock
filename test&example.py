import threading
import time
from datetime import datetime
from SrcLock import lock

sth = []
#basic test
sec_sth = lock(sth)
with sec_sth:
	sec_sth.s.append(1)
	
#threading test
src1 = []
src2 = []
sec_src1 = lock(src1)
sec_src2 = lock(src2)

class worker1(threading.Thread):
	def __init__(self,*args,**kw):
		super(worker1,self).__init__(*args,**kw)
		
	def run(self):
		print('[Worker1] want src1 - %s' % str(datetime.now().timestamp()))
		with sec_src1:
			print('[Worker1] use src1 for 5s - %s' % str(datetime.now().timestamp()))
			time.sleep(5)
			print('[Worker1] release src1 - %s' % str(datetime.now().timestamp()))
			
class worker2(threading.Thread):
	def __init__(self,*args,**kw):
		super(worker2,self).__init__(*args,**kw)
		
	def run(self):
		time.sleep(1.5)
		print('	[Worker2] want src2 - %s' % str(datetime.now().timestamp()))
		with sec_src2:
			print('	[Worker2] use&release src2 - %s' % str(datetime.now().timestamp()))
		
		print('	[Worker2] want src1 - %s' % str(datetime.now().timestamp()))
		with sec_src1:
			print('	[Worker2] use&release src1 - %s' % str(datetime.now().timestamp()))
			
t1 = worker1()
t2 = worker2()
t1.start()
t2.start()

	
	
	