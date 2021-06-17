import pyrebase

from flask import Flask,jsonify
application = Flask(__name__)

@application.route('/')
def index():
    return jsonify({'sucess': '1'})

if __name__ == '__main__':
    application.run(host="0.0.0.0:3000",debug=True)