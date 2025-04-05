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
import os

app = Flask(__name__)

if __name__ == "__main__":
    # Only bind to 0.0.0.0 when running locally
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# Get the port from the environment variable, default to 5000 if not set
# port = int(os.environ.get("PORT", 5000))
# app.run(host="0.0.0.0", port=port)

@app.route('/', methods=['GET'])
def hello():
    return "<h1>Welcome to Mercury</h1>"

@app.route('/login', methods=['GET','POST'])
def login():
    return "<h1>Login Page</h1>"


@app.route("/style")
def home():
    return render_template("index.html")