from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Index page'

@app.route('/bikes')
def bikes():
    return 'Welcome to Bikes page'

@app.route('/cars')
def cars():
    return 'Welcome to Cars page'

if __name__ == '__main__':
    app.debug = True
    app.run()