#!/usr/bin/python3

import time
import socket
import threading
import sys
class scan_tool(threading.Thread):  
    def __init__(self,ip,max_port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.max_port = max_port
                
    def run(self):
        self.check_iplist_portlist()
   
    def check_ip_port(self,ipaddress,port):
        if int(self.get_conn_time(ipaddress, port)) != 1:
   #         print('ip is:',ipaddress,"port is:",port)
            return str(ipaddress) + ":" + str(port)
        else:
            return 0
        
    def check_iplist_portlist(self):
        port_list = []
        #for i in range(self.max_port):
        str0 = self.check_ip_port(self.ip,self.max_port)
        if str0:
            port_list.append(str0)
      #  for p in port_list:
     #       print(p)
                          
    def get_conn_time(self,ipaddress, port):   
        try:
            socket.setdefaulttimeout(20)
            s=socket.socket()
            start=time.time()
            s.connect((ipaddress, port))
            end=time.time()
            s.close()
        except:
            #print ('Connect %s:%d timeout' %(ipaddress,port))
            end='error'
            s.close()
            return '1'
        
        try:
            socket.setdefaulttimeout(20)
            s=socket.socket()
            start=time.time()
            s.connect((ipaddress, port))
            end=time.time()
            s.close()
        except:
            end='error'
            s.close()
            return '1'
            
        if end!='error':
            connect_time=end-start
            print ('found ip %s :%d 连接时间:%s ms' %(ipaddress,port,str(int(connect_time*1000))))
            connect_time=int(connect_time*1000)
            return connect_time
        else:
            return '1'
        
def main(ip,port1,port2):
#    st = scan_tool('23.252.160.225',500)
#    st.start()
#    st0 = scan_tool('127.0.0.1',500) 
#    st0.start()
	for i in range(int(port1),int(port2)):
		scan_tool(ip,i).start()
#	for i in range(1000,2000):
#		scan_tool(ip,i).start()

    
if __name__ == '__main__':
    #main(sys.argv[1],sys.argv[2],sys.argv[3])       
	for i in range(66):    
		try:
			main(sys.argv[1],i*1000,(i+1)*1000)       
		except:
			pass

