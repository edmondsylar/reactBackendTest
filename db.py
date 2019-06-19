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
    'host':'localhost',
    'database':'astuteProduction',
    'password':'password',

    # This is a constant for all connections
    'autocommit': True,

    # 'user':'root',
    # # 'host':'192.168.8.2',
    # 'database':'astuteproduction',
    # 'password':None,

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


    def login(self, email, password):
        password_init = hashlib.md5(password.encode())
        passw = password_init.hexdigest()

        sql_login = "SELECT username, userUuid FROM t_users WHERE username='{}' AND password='{}'".format(email, passw)
        self.cur.execute(sql_login)
        results = self.cur.fetchall()

        if(len(results) != 0):
            for username, userid in results:
                user = {
                    'username':username,
                    'id': userid
                }
                return (jsonify(user))

        else:
            status_code = '500'
            return (status_code)

    def business_fetch(self, userid):

        businesses = []

        sql_business_search = "SELECT `businessUuid` FROM `a_user_roles` WHERE assignedTo='{}'".format(userid)

        self.cur.execute(sql_business_search)
        business_results = self.cur.fetchall()

        if (len(business_results) == 0):
            for each in business_results:
                for one in each:
                    businesses.append(one)
            
            return(jsonify(businesses))
        else:
            status_code = '500'
            return (status_code)
        
