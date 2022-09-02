from flask import Flask,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Check this amazing web.</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>My hug baby~~~ It is hard to forget someone who gave you so much to remember.I know it is hard to forget who hurt you a lot. Just because you loved before.Hey {}, remember one thing, I will always by your side.</h1>'.format(name)

@app.route('/tosmileig/')
def myig():
    return redirect("https://www.instagram.com/smilegoofy_orb/")

@app.route('/checkbabysig/')
def babysig():
    return redirect("https://www.instagram.com/sjxi_0302/")

if __name__ == '__main__':
    app.run('0.0.0.0')
