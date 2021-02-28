from flask import Flask, render_template, redirect, url_for, request, session, g, abort
from datetime import datetime
import json
import googlemaps
import time
import math

now = datetime.now()
today = datetime.today()
current_time = now.strftime("%H:%M:%S")
print(current_time)
current_date = today.strftime("%B %d, %Y")

app = Flask(__name__, static_folder=r'C:\Users\Sarjan Shah\Documents\Projects\Python\lancerhack\\static')


schedule = {}
totalnum = None
@app.route('/')
def index():
    return render_template('index.html', date = current_date)
@app.route('/map')
def maps():
    return render_template('maps.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/howitworks')
def howitworks():
    return render_template('howitworks.html')
@app.route('/log')
def log():
    return render_template('log.html')

if current_time == '12:00:00':  
    for i in range(10):
        showPosition()
        time.sleep(5)    

