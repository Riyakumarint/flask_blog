from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/riya_blogs'
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    msg = db.Column(db.String(1200), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    phone_no = db.Column(db.String(12), nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if(request.method=='POST'):
        '''Add entry to database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('msg')
        entry = Contacts(name=name, phone_no=phone, msg=msg, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        db.create_all()
        Contacts.query.all()

    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')


app.run(debug=True)
