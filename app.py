from flask import Flask,url_for,request,render_template,flash
import pymysql
import pytz
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

connection = pymysql.connect(host="localhost",user="root",password="",db="ToDoList")
IST = pytz.timezone('Asia/Kolkata')


@app.route("/",methods=['GET','POST'])
def home():
    cursor = connection.cursor()
    sql = f"SELECT title,description,created_at from todos"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    print(results)
    return render_template('home.html',results=results)

@app.route("/add",methods=['GET','POST'])
def addTodo():
    if request.method == 'POST':    
        title = request.form.get('title','')
        description = request.form.get('description','')
        created_at = datetime.now(IST)
        cursor = connection.cursor()
        sql = f"INSERT INTO todos (title,description,created_at) VALUES ('{title}','{description}','{created_at}')"
        result =cursor.execute(sql)
        connection.commit()
        cursor.close()
        if(result):
            flash('saved successfully')
        else:
            flash('unable to save')
        return redirect(url_for('home'))  
    return render_template('addTodo.html')

# @app.route("/flash",methods=['GET','POST'])
# def home():
#     print(request.form)
#     return render_template('home.html')

