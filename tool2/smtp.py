import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def send(to,subject,contect): 
	msg = MIMEText(contect, 'plain', 'utf-8')
	msg['From'] = formataddr(["监控",'clickplus@163.com'])
	msg['To'] = formataddr([to,to])
	msg['Subject'] = subject
 
	server = smtplib.SMTP("smtp.163.com", 25)
	server.login("clickplus@163.com", "Clickplus1234")
	server.sendmail('clickplus@163.com', [to,], msg.as_string())
	server.quit()
	
#def sendmail():
#    to='hongyihui@clickplus.cn'
#    subject='test'
#    contect='this is a test'
#    send(to,subject,contect)
#if __name__=='__main__':
#    sendmail()
