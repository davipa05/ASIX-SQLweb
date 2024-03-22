import sqlite3
from flask import Flask, render_template,url_for,redirect,request
import sqlite3
import hashlib
import uuid
from createdb import cipher_suite



app = Flask(__name__)

@app.route("/")
def home():
    conn=sqlite3.connect("store.db")
    cur=conn.cursor()
    SQL=f'SELECT * FROM products'
    prod=cur.execute(SQL).fetchall()
    return render_template("home.html",products=prod)

@app.route("/login",methods=['GET', 'POST'])
def login():
    logged=False 
    if request.method == "POST":
        conn=sqlite3.connect("store.db")
        
        cur=conn.cursor()
        username=request.form.get('username')
        password=request.form.get('password')
        # " OR "1"="1
        # " OR "1"="1"; DROP TABLE users;
        SQL=f'SELECT rowid,username, password FROM users WHERE username="{username}" AND password="{password}"'
        print(SQL)
        try:
            res=cur.execute(SQL).fetchone()
        except Exception as e:
            return render_template("login.html",errors=e)
        if res:
           print("USER", res[0])
           logged=True
        else:
            return render_template("login.html",errors="Ha habido alguna clase de error")
    if logged:
       return redirect('user/'+str(res[0]))
    else:
        return render_template("login.html")
    
@app.route("/register",methods=['GET','POST'])
def register():
    registered=False
    if request.method == "POST":
        conn=sqlite3.connect("store.db")
        cur=conn.cursor()
        print(request.form)

        SQL='INSERT INTO users VALUES ('
        SQL += '"'+str[uuid.uuid4()]+'",'
        for field in list(request.form):

            campo = field
            valor=request.form[field]

            if campo=="password":
                valor=hashlib.sha256(bytes(valor,'utf-8')).hexdigest()

            elif campo=="adress":
                valor = cipher_suite.encrypt(bytes(valor,'utf-8')).hexdigest()

            SQL+=f'"{valor}",'
            
        SQL=SQL.rstrip(', ')
        SQL+=',"'+2+'"'
        SQL+=')'
        print("create user",SQL)
        try:
            cur.execute(SQL)
            conn.commit()
            newuserid=cur.lastrowid
            registered=True
        except Exception as e:
            return render_template("register.html",errors=e)

    if registered:
        return redirect('user/'+str(newuserid))
    else:
        return render_template("register.html")

@app.route("/user/<int:userid>")
def user(userid):
    # get user data
    conn=sqlite3.connect("store.db")
    cur=conn.cursor()
    SQL=f'SELECT username, adress FROM users WHERE rowid='+str(userid)
    userdata=cur.execute(SQL).fetchone()

    #get products
    SQL=f'SELECT name,price,image FROM purchases INNER JOIN products ON purchases.product_id=products.rowid WHERE purchases.username_id={userid}'
    prod=cur.execute(SQL).fetchall()
    print("products",prod)
    return render_template("user.html", userdata={"username":userdata[0],"adress":userdata[1],"products":prod})

if __name__ == "__main__":
  app.run(debug=False,host="0.0.0.0")