'''
Description: Initial web deployment of Mercury Webpage
Date: April 5th, 2025
Author: Lex
Purpose: Personal project to develop software webdevelopment skills using Flask and Render to
         build a backend, frontend, and deploy a webpage

'''

# This is the main Flask router for the Mercury application

# test_flask.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "<h1>Welcome to Mercury</h1>"

@app.route('/login', methods=['GET','POST'])
def login():
    return "<h1>Login Page</h1>"


@app.route("/style")
def home():
    return render_template("index.html")