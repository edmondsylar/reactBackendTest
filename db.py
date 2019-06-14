import pymysql
from flask import jsonify
import uuid
import time
import sys
import hashlib
from emailer import sendCode
verifyMail = sendCode()

connection = {
    'user':'devops',
    # 'user':'root',
    'host':'localhost',
    'database':'astuteProduction',
    # 'database':'astuteproduction',
    # 'password':None,
    'password':'password',
    'autocommit': True 

}

genders = []

class dbModal:
    def __init__(self):

        self.proceed = 'proceed'
        self.exist = 'exist'


        self.conn = pymysql.connect(**connection)
        self.cur = self.conn.cursor()
        self.DbStatus()


    def Checker(self, email):
        sql = "select person_uid from t_users_register where email='{}'".format(email)
        self.cur.execute(sql)
        response = self.cur.fetchall()

        if (len(response) >= 1):
            print (self.exist)
            return (self.exist)
        else:
            print(self.proceed)
            return (self.proceed)



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

        countrySql = "select id, name from t_country"
        self.cur.execute(countrySql)
        countryz = self.cur.fetchall()

        for i, c in countryz:
            country = {
                'code':i,
                'name': c
            }
            counts.append(country)

        return (jsonify(counts))


    def bssTypes(self):
        bsts = []

        regtypes = "select id, name from t_registrationtypes"
        self.cur.execute(regtypes)
        bstypz = self.cur.fetchall()

        for i, c in bstypz:
            business = {
                'id':i,
                'name': c
            }
            bsts.append(business)

        return (jsonify(bsts))

    def register(self, name, email, gender, dob, password):
        status = self.Checker(email)
        personid = uuid.uuid4()
        passw = hashlib.md5(password.encode())

        if (status == 'proceed'):
            print (status)
            # msg = ('/home')
            code = verifyMail.Start(email)
            
            sql = "insert into t_users_register(person_uid, names, gender, email, date_of_birth, password) VALUES ('{}', '{}','{}','{}','{}','{}')".format(personid, name, gender, email, dob, passw.hexdigest())
            self.cur.execute(sql)

            return(code)

        else:
            msg = 'This user Exists already'
            # print ('This user Exists already')
            return (msg)