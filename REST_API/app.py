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

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return 'User Deleted!'

# PUT (Update) user by ID
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE users SET username=%s, email=%s, password=%s WHERE id=%s", 
                   (username, email, password, id))
    mysql.connection.commit()
    cursor.close()
    return 'User Updated!


 

if __name__ == '__main__':
    app.run(debug=True)
 
