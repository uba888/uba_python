#!/usr/bin/python
from email.mime.multipart import MIMEMultipart
import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email_with_file(addressee, text, subject, file_list):
    """file email"""

    msg = MIMEMultipart()
    msg.attach(MIMEText(text, _charset='utf-8'))
    msg['Subject'] = 'test'
    msg['From'] = 'hongyihui@clickplus.cn'
    msg['To'] = addressee

    for file_name in file_list:
        ctype, encoding = mimetypes.guess_type(file_name)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        
        attachment = MIMEImage((lambda f: (f.read(), f.close())) \
                (open(file_name, 'rb'))[0], _subtype =subtype)
        attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
        msg.attach(attachment)

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.mxhichina.com', 25) 
        smtp.login('hongyihui@clickplus.cn','Jdyun1234') 
        smtp.sendmail(msg['From'], addressee, msg.as_string())
    except Exception as e:
        print('send_email: %s' % (str(e)))



send_email_with_file('hongyihui@clickplus.cn','test','test',['test.txt'])
