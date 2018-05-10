#SQLite and Flask
from flask import Flask, request, render_template
import sqlite3
from datetime import datetime, date
#ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import User, Base, Keg
 
#Create a object of Flask(Framework)
app = Flask(__name__)


#Insert data in the table User
def insert_data_User(username, fullname, email, password, nfc_id):
    new_user = User(username=username, fullname=fullname, email=email, password=password, nfc_id=nfc_id)
    session.add(new_user)
    session.commit()
    
#Insert data in the table Keg
def insert_data_Keg(keg_id, keg_flow):
    new_keg = Keg(keg_id=keg_id, keg_flow=keg_flow)
    session.add(new_keg)
    session.commit()   
    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/show_users")
def show_users():
    #Get the data from the data User
    users = session.query(User).all()
    
    return render_template("show_users.html", users=users)

@app.route("/show_kegs")
def show_kegs():
    #Get the data from the table Keg
    kegs = session.query(Keg).all()
    
    return render_template("show_kegs.html", kegs=kegs)

@app.route("/insert_user", methods=['GET', 'POST'])
def insert_user():
    if (request.method == "GET"):
        return render_template("insert_user.html")
    
    elif(request.method == "POST"):
        username = request.form.get('username')
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        nfc_id = request.form.get('nfc_id')
        
        insert_data_User(username, fullname, email, password, nfc_id)

    
        return show_users()
    
@app.route("/insert_keg", methods=['GET', 'POST'])
def insert_keg():
    if (request.method == "GET"):
        return render_template("insert_keg.html")
    
    elif(request.method == "POST"):
        keg_id = request.form.get('keg_id')
        keg_flow = 0.0
        
        insert_data_Keg(keg_id, keg_flow)

    
        return show_kegs()


if __name__ == '__main__':
    path_to_database = "BeerBase.db"    
    engine = create_engine('sqlite:///'+path_to_database) 
    Base.metadata.bind = engine
     
    DBSession = sessionmaker(bind=engine)

    session = DBSession()
    app.run('0.0.0.0', debug=True, port=5000)

