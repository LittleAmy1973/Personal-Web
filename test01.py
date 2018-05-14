#coding=utf-8
import json,pprint,sys
from flask import Flask, render_template
app = Flask(__name__)
# ...
'''
@app.route('/')
def index():
    return  "<h1>欢迎来到我的世界</h1>"
'''

@app.route('/')
def index():
    return render_template("zihui.html")

@app.route('/pic')
def pic():
    return render_template("pic.html")
@app.route('/book')
def book():
    return render_template("book.html")
@app.route('/movie')
def movie():
    return render_template("movie.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)