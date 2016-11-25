import time
import sys
begin=time.time()
for i in range(1,10):
	sys.stdout.write('{0}\r'.format((int(time.time()-begin))))
	sys.stdout.flush()
	time.sleep(1)
