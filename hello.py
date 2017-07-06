#encoding: utf-8
from flask import Flask
from flask import render_template
from flask import request
import  user

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('login.html')


@app.route('/login/',methods=['post','get'])
def login():
    username = request.form.get('username','')
    password = request.form.get('password','')
    if user.va_login(username,password):
        return "success"
    else:
        return render_template('login.html',username=username,error='username or password is error')
    print username
    print password
    return ''
if __name__ == '__main__':
    app.run(host='127.0.0.1')