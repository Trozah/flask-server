import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('./index.html')

@app.route('/about.html')
def about():
    return render_template('./about.html')


@app.route('/blog/2020/dogs')
def blog2():
    return 'this is my dog'
