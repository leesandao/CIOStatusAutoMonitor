from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Message, Mailbox, HTMLBody, FileAttachment
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
from exchangelib.items import SEND_ONLY_TO_ALL, SEND_ONLY_TO_CHANGED
import urllib3
import os

#此句用来消除ssl证书错误，exchange使用自签证书需加上
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 输入你的域账号如example\leo
cred = Credentials(r'citrite\raynorl', 'Jordan01')

config = Configuration(server='mail.citrix.com', credentials=cred, auth_type=NTLM)
a = Account(primary_smtp_address='raynor.li@citrix.com', config=config, autodiscover=False, access_type=DELEGATE)

# 此处为用来发送html格式邮件的文件路径
logoname = 'E:\screenshots\screenshot.jpg'
with open(logoname,'rb') as fp:
	logoimg = FileAttachment(name=logoname, content=fp.read())

m = Message(
	account=a,
	#folder=a.sent,
	subject='CIO Login Status Test',
	body = HTMLBody('<html><body><p>Hi Team<br /><img src="cid:screenshot.jpg"><br />B.R.<br />Raynor</p></body></html>'),
	to_recipients=[Mailbox(email_address='tao.sun@citrix.com'),Mailbox(email_address='Staff-TaoToddSunEmployeesOnly@citrite.net')]
		)
		
m.attach(logoimg)
m.send()
