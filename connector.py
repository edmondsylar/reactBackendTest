import pymysql 

connection = {
    'user':'devops',
    # 'user':'root',
    'host':'localhost',
    'database':'astuteProduction',
    # 'database':'astuteproduction',
    # 'password':None
    'password':'password',
    'autocommit': True 
}

class dbModal:
	def __init__(self):
		try:
			self.conn = pymysql(**connection)
			self.cur = self.conn.cursor()
			self.status()
		except Exception as e:
			print (e)
			return (e)

	def status(self):
		msg = "Connection established"
		print (msg)
		return (msg)
