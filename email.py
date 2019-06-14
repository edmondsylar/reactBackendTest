import sys
import smtplib, ssl
import random
import string
from genRandom import randomStringDigits

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "servicedesk.transcend@gmail.com"
password = "Alupo.Agatha&Edmond@2019"
# Create a secure SSL context
context = ssl.create_default_context()


class sendCode:
	def __init__(self, email):
		try:
			key = randomStringDigits()

			self.server = smtplib.SMTP(smtp_server, port)
			selfserver.ehlo()
			self.server.starttls(context=context)
			self.server.ehlo()
			self.server.login(sender_email, password)
			mailto = email
			msg = "Verificatio coed is {}".format(key)
			
			self.server.sendmail(sender_email, mailto, msg)

			print (key)
			return (key)

		except Exception as e:
			print (e)
			return (e)
