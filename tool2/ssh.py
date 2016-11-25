#!/usr/bin/python3
import pexpect
import sys
'''usage： python3 ssh.py user ip passwd cmd
   such as:python3 ssh.py root 192.168.31.131 'df -h'
'''
def ssh_cmd(user,ip, passwd,cmd): 
        ssh = pexpect.spawn('ssh %s@%s "%s"' % (user,ip,cmd)) 
        try: 
                i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
                if i == 0 : 
                        ssh.sendline(passwd) 
                elif i == 1: 
                        ssh.sendline('yes') 
                        ssh.expect('password: ') 
                        ssh.sendline(passwd) 
        except pexpect.EOF: 
                print("EOF")
        except pexpect.exceptions.TIMEOUT as e :
                print(e)
        else:
                r = ssh.read() 
                print(r.decode('utf-8'))
        ssh.close()

if __name__=='__main__':
        ssh_cmd(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
