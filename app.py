from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__, template_folder='templates')

app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

mysql = MySQL(app)

@app.route('/')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from user_table")
    #fetching all records from database
    data=cursor.fetchall()
    data_names = []
    data_lastnames = []
    data_roles = []
    data_keys = ["Name", "LastName", "Role"]
    print
    print(data)
    print
    print("Total number of rows in table: ", cursor.rowcount)
    for row in data:
        data_names.append(row[0])
        print("Name = ", row[0], )
        data_lastnames.append(row[1])
        print("LastName = ", row[1])
        data_roles.append(row[2])
        print("Role  = ", row[2], "\n")
    print (data_names)
    print (data_lastnames)
    print (data_roles)

    return render_template('index.html', data_names=data_names, data_lastnames=data_lastnames, data_roles=data_roles)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/fillup', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Create a new line in user_table via the Fill Up Form"

    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        role = request.form['role']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO user_table VALUES(%s,%s,%s)''',(name,lastname,role))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

app.run(host='0.0.0.0', port=5050)
