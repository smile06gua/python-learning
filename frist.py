from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Check this amazing web.</h1>'

def user2('/who/<yourname>):
    return '<h1>Hello {},have s nice day!</h1>'.format(yourname)

@app.route('/user/<name>')
def user(name):
    return '<h1>It is hard to forget someone who gave you so much to remember.I know it is hard to forget who hurt you a lot. Just because you loved before.Hey {}, remember one thing, I will always by your side.</h1>'.format(name)

@app.route('/tosmileig/')
def myig():
    return redirect("https://www.instagram.com/smilegoofy_orb/")

if __name__ == '__main__':
    app.run()
