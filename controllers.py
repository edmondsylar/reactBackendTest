from flask import jsonify
from db import dbModal

class route_definitions:
    def __init__(self):
        self.names = []

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