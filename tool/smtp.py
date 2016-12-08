import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from email import encoders
from email.mime.application import MIMEApplication 

user = 'hongyihui@clickplus.cn'
pwd = 'Jdyun1234'
def da(to,subject,content,attfile):
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = "hongyihui@clickplus.cn"
	msg['To'] = to
	#basename = os.path.basename(attfile)
	#fp = open(attfile, 'rb')
	#att = MIMEText(fp.read(), 'base64', 'utf-8')
	#att["Content-Type"] = 'application/octet-stream'
	#att.add_header('Content-Disposition', 'attachment',filename=('gbk', '', basename))
	#encoders.encode_base64(att)
	#msg.attach(att)
	part = MIMEText(content)
	msg.attach(part)
	part = MIMEApplication(open(attfile,'rb').read())
	part.add_header('Content-Disposition', 'attachment', filename=attfile)
	msg.attach(part)  
	#s = smtplib.SMTP('mxn.mxhichina.com')
	s = smtplib.SMTP('smtp.mxhichina.com')
	s.login(user, pwd)
	s.sendmail(user, to, msg.as_string())
	s.close()


if __name__=="__main__":
	to =  sys.argv[1]
	subject = sys.argv[2]
	content = MIMEText(sys.argv[3], 'plain', 'utf-8')
	attfile = sys.argv[4]
	da(to,subject,content,attfile)
