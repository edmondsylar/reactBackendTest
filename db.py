import pymysql
from flask import jsonify
import uuid;

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

        return (jsonify(genders))

    def search(self, name):
        results = []

        sql = "select name,prifileType, profileUuid from t_profiles where name like '%{}%'".format(name)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        for n, t, y in data:
            res = {
                'name':n,
                'type':t,
                'id':y
            }
            results.append(res)

        return (jsonify(results))
    def regBss(self, bssname, regno, bsstype, regcountry, regdate):
        # table name t_business
        Genid = uuid.uuid4()
        success = "Business Created"
        error = "Encontered errors while creating business"

        BssCreatesql = "insert into t_business(businessUuid, businessName, businessTypeUuid, registrationNumber, registrationCountryid, registrationDate) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(Genid, bssname, bsstype, regno, regcountry, regdate)
        self.cur.execute(BssCreatesql)
        
        return(jsonify({success: Genid}))


    def countries(self):
        counts = []

        countrySql = "select (id, name) from t_country"
        self.cur.execute(countrySql)
        countryz = self.cur.fetchall()

        for i, c in countryz:
            country = {
                'code':i,
                'name': c
            }
            counts.append(country)

        return (jsonify(counts))

