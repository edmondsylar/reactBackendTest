from flask import Flask, request
from db import dbModal
from flask_cors import CORS, cross_origin


user = dbModal()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the fear of God is the beginning of wisedom'
cors = CORS(app, resources={r"/": {'origin': '*'}})


@app.route('/')
@cross_origin()
def default():
    defaultCheck = user.GenderCheck()
    return (defaultCheck)


@app.route('/search', methods=['POST', 'GET'])
def search():
    name = request.json['name']
    req = user.search(name)

    return (req)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')