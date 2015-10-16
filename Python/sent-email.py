#-*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

read_score = open('D:\\UVA\\Python\\score.txt', 'r')
read_address =open('D:\\UVA\\Python\\address.txt', 'r')

smtp_server = 'ccms.nkfust.edu.tw'
me = 'u0324814@nkfust.edu.tw'

while True:
	recipient=read_address.readline().rstrip('\n')
	score=read_score.readline().rstrip('\n')
	if recipient=='':
		break
	print(score,recipient)
	msg = MIMEMultipart() 

	msg['Subject'] = 'testing' #標題
	msg['From'] = me  
	msg['To'] = recipient
	msg.attach(MIMEText(score)) #內文

	s = smtplib.SMTP('ccms.nkfust.edu.tw', 25)
	s.login('leorean', 'password')
	s.sendmail(me, recipient, msg.as_string())
	s.quit()




