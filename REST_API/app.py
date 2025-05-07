from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask import request

 
app = Flask(__name__)
 
# Ρυθμίσεις MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cmp210'
 
mysql = MySQL(app)
 
@app.route('/')
def home():
    return "✅ Flask + MySQL είναι έτοιμο!"
 
@app.route('/users', methods=['GET'])
def get_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, username, email,password FROM users")
    rows = cursor.fetchall()
    cursor.close()
 
    users = []
    for row in rows:
        users.append({
            "id": row[0],
            "username": row[1],
            "email": row[2],
            "pass": row[3]
        })
 
    return jsonify(users)
 
@app.route('/add',methods=['POST'])
def add_users():
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES ('petros', 'petros.doe@example.com', 'passpass')")
    mysql.connection.commit()
    cursor.close()
 
    return 'User Added!'
 
@app.route('/add_custom_users',methods=['POST'])
def query_example():
    # if key doesn't exist, returns None
    username = request.args.get('username')

    # if key doesn't exist, returns a 400, bad request error
    password = request.args.get('password')

    # if key doesn't exist, returns None
    email = request.args.get('email')


    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES  (%s, %s, %s)", (username,email,password))
    mysql.connection.commit()
    cursor.close()

    return 'User Added!'

@app.route('/delete_custom_users',methods=['DELETE'])
def query_example():
    # if key doesn't exist, returns None
    username = request.args.get('username')

    # if key doesn't exist, returns a 400, bad request error
    password = request.args.get('password')

    # if key doesn't exist, returns None
    email = request.args.get('email')


    cursor = mysql.connection.cursor()
    cursor.execute("REMOVE INTO users (username, email, password) VALUES  (%s, %s, %s)", (username,email,password))
    mysql.connection.commit()
    cursor.close()

    return 'User Removed!'

@app.route('/UPDATE_custom_users',methods=['UPDATE'])
def query_example():
    # if key doesn't exist, returns None
    username = request.args.get('username')

    # if key doesn't exist, returns a 400, bad request error
    password = request.args.get('password')

    # if key doesn't exist, returns None
    email = request.args.get('email')


    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE INTO users (username, email, password) VALUES  (%s, %s, %s)", (username,email,password))
    mysql.connection.commit()
    cursor.close()

    return 'User UPDATED!'


 

if __name__ == '__main__':
    app.run(debug=True)
 
