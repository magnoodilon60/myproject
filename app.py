from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def hello_world(username):
    # mostrar o perfil do usuário para aquele usuário
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def porj(post_id):
    # mostra a postagem com o id fornecido, o id é um inteiro
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'O primeiro projeto'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<username>')
def index1(username):
    return render_template(f'{username}')

app.run(port=5000, debug=True)
