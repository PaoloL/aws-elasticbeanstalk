from flask import Flask
from markupsafe import escape

application = Flask(__name__)

@application.route('/')
def index():
    return 'Welcome to Index page'

@application.route('/bikes')
def bikes():
    return 'Welcome to Bikes page'

@application.route('/cars')
def cars():
    return 'Welcome to Cars page'

@application.route('/bus')
def bus():
    return 'Welcome to Bus page'

if __name__ == '__main__':
    application.debug = True
    application.run(host='0.0.0.0', port=8080)