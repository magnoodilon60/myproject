#teste
#algum coteudo novo

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


#criar primeira rota
@app.route('/')
def index():
    return 'index'


#segunda rota
@app.route('/login')
def login():
    return 'login'

#terceira rota
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Jhon Doe'))


