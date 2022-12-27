from flask import Flask, render_template, flash, request, redirect,make_response
from datetime import datetime
import json

app = Flask(__name__)
start_date = datetime(2022, 11, 25, 17, 35)

@app.route('/')
def home():
    return render_template("home.html", start_date=start_date)