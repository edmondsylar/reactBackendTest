import pymysql
from flask import jsonify
import uuid;

connection = {
    'user':'devops',
    'host':'localhost',
    'database':'astutePoduction',
    'password':'password'
}

genders = []

class dbModal:
    def __init__(self):
        self.conn = pymysql.connect(**connection)
        self.cur = self.conn.cursor()
        self.DbStatus()

    def DbStatus(self):
        msg = "Databse connection active"
        return (msg)

    def GenderCheck(self):
        sql = "select status, gender from a_gender"
        self.cur.execute(sql)
        data = self.cur.fetchall()

        for a, b in data:
            obj = {
                'Id':uuid.uuid4(),
                'status':a,
                'Title':b,
                'Completed':False
            }
            genders.append(obj)

        return (json(genders))

    def search(self, name):
        results = []

        sql = "select name,prifileType from t_profiles where name like '%{}%'".format(name)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        for n, t in data:
            res = {
                'name':n,
                'type':t
            }
            results.append(res)

        return (jsonify(results))