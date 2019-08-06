import os
from app import app
from flask import render_template, request, redirect, session, url_for
from flask_pymongo import PyMongo
app.secret_key = b'.\xe2l\xb1\x0cg\xa8:\x0e(N\x1c\xd4\x8fPZ'

# name of database
app.config['MONGO_DBNAME'] = 'database' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:4wxbgw55@cluster0-reiqc.mongodb.net/database?retryWrites=true&w=majority' 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')
@app.route('/login', methods=["POST"])

def login():
    users = mongo.db.users
    #use the username to find account, then verify password
    existing_user = users.find_one({'username':request.form['username']})
    if existing_user:
        #verify password
        if existing_user['password'] == request.form['password']:
            session['username'] = request.form['username']
            return render_template('/index.html')
        else:
            return "Invalid password"
        return "Invalid username"
    else:
        return "Enter a valid username/password"

# CONNECT TO DB, ADD DATA
@app.route('/submission', methods=["GET","POST"])
def submission():
    if request.method =="POST":
        submission = mongo.db.submissions
        submission.insert({'Problem':request.form['Problem']})
        return redirect('/')
    

@app.route('/articles')

def articles():
    return render_template("/articles.html")
    
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method =="POST":
        # take in the info they gave us, check if username is taken, if username is available put into a database of users
        users=mongo.db.users
        existing_user = users.find_one({'username':request.form['username']})
        if existing_user is None:
            users.insert({"username":request.form['username'],'password':request.form["password"]})
            return redirect('/')
        else:
            return "That username is taken."
            
    else:
        return render_template('signup.html')
@app.route('/logout') 
def logout():
    session.clear()
    return redirect('/')
    
    
@app.route('/bipolar')
def bipolar():
    return render_template("/bipolar.html")

@app.route('/features')
def features():
    return render_template("/featurepage.html")
    
@app.route('/ocd')
def ocd():
    return render_template('ocd.html')