from logging import debug
import flask
import datetime
import mysql.connector
import pymysql
from flask import Flask, redirect, render_template, request, url_for, flash
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, make_response, Response, json, url_for
import os
from flask_mysqldb import MySQL,MySQLdb


app = Flask(__name__, static_url_path='/static')
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='opencvfrom',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

#upload   
app.secret_key = "caircocoders-ednalan"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'opencvfrom'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = './static/uploads'
  
mysql = MySQL(app)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','mp4'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    with conn.cursor () as cur:
        cur.execute("select * from testfrom")
        rows=cur.fetchall()
    return render_template("index.html",datas=rows)

@app.route('/showfrom',  methods=['GET', 'POST'])
def showfrom():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.datetime.now()
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        email = request.form['email']
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['files[]']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            tup = (fname ,lname ,phone , email, f'./static/uploads/{filename}', now)
            cur.execute("INSERT INTO testfrom (fname, lname, phone, email, path_img, date_upload) VALUES (%s , %s, %s, %s , %s, %s)", tup)
            mysql.connection.commit()
            cur.close()
            flash("Upload file successed")
            return redirect("/")
    return render_template("testfrom.html")

@app.route('/admin')
def admin():
    name = "Audy Woranat"
    return render_template("admin.html",myname = name)

@app.route('/about')
def about():
    return render_template("about.html")

'''
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/',methods=["POST","GET"])
def index():
    return render_template('testfrom.html')

cursor = mysql.connection.cursor()
@app.route("/showfrom",methods=["POST","GET"])
def upload():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    if request.method == 'POST':
        files = request.files.getlist('files[]')
        #print(files)
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cur.execute("INSERT INTO images (file_name, uploaded_on) VALUES (%s, %s)",[filename, now])
                mysql.connection.commit()
            print(file)
        cur.close()   
        flash('File(s) successfully uploaded')    
    return redirect('/')'''
 
if __name__ == "__main__":
    app.run(debug=True)

