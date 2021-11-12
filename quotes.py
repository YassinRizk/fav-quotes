from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:saso0105@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://rksapnicgnzsml:90c79b90e73dfa65dfc7b646ef6077c4fbd0abca4f5993986378020c61deb001@ec2-52-209-246-87.eu-west-1.compute.amazonaws.com:5432/d58tri9ahsnqqj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)


class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote  = db.Column(db.String(2000))

@app.route('/')

def index():
    result = Favquotes.query.all()
    return render_template('index.html',result =result )

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata =Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
