import requests
from flask import Flask
from flask import render_template

@app.route('/')
def home():
   return render_template('index.html')
