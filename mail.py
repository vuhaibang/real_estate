import smtplib
from keymail import username, password
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64 
import os


#Content email
msg = MIMEMultipart()
msg['From'] = username # your email
msg['To'] = 'Mr Jone' 
msg['Subject'] = 'data'
msg.attach(MIMEText('''Dear Mr Jone
	Data for Mr Jone'''))
attach = 'C:/Users/User/Documents/file chạy/Danso2017.xlsx'
if attach:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username, password) # login 
toaddr = 'arthur15194@gmail.com' # your gmail
server.sendmail(username, toaddr, msg.as_string())
server.close()