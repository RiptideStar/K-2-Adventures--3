from flask import Flask, render_template, flash, request, redirect,make_response
from flask_sqlalchemy import SQLAlchemy
import app_query
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///number.db'
db = SQLAlchemy(app)

class Number(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)

@app.route('/increment-kimberly', methods=['POST'])
def increment_kim():
    number = app_query.update_thoughts("kimberly")
    return json.dumps({"number": number[0]})

@app.route('/increment-kyle', methods=['POST'])
def increment_kyle():
    number = app_query.update_thoughts("kyle")
    return json.dumps({"number": number[0]})


@app.route('/')
def home():
    (_, number, kim_thought_last) = app_query.get_last_thought()
    color_of_output = "red"
    if kim_thought_last == 1: #green: #56ff50
        color_of_output = "#56ff50"
    else: #blue: #2190ec
        color_of_output = "#2190ec"
    return render_template("home.html", num=number, col=color_of_output)
