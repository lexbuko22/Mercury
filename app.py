'''
Description: Initial web deployment of Mercury Webpage
Date: April 5th, 2025
Author: Lex
Purpose: Personal project to develop software web development skills using Flask and Render to
         build a backend, frontend, and deploy a webpage

'''

# This is the main Flask router for the Mercury application

from flask import Flask, render_template
import os

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

# Ensure Flask binds to 0.0.0.0 and uses the port provided by Render
if __name__ == "__main__":
    # Get the port from the environment variable provided by Render, default to 5000 if not set
    port = int(os.environ.get("PORT", 5001))
    # Run the app on 0.0.0.0 with the dynamically assigned port
    app.run(host="0.0.0.0", port=port)