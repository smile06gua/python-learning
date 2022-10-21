from flask import Flask,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Check this amazing web.</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>早安，{}</h1>'.format(name)

@app.route('/tosmileig/')
def myig():
    return redirect("https://www.instagram.com/smilegoofy_orb/")

@app.route('/checkbabysig/')
def babysig():
    return redirect("https://www.instagram.com/sjxi_0302/")

if __name__ == '__main__':
    app.run('0.0.0.0')
