from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/LOGIN-REACTAPP")
db = mongodb_client.db  # Use the 'db' attribute to access the database

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Store the login data in MongoDB
    users_collection = db.users  # Access the 'users' collection in the 'LOGIN-REACTAPP' database
    user = {
        'username': username,
        'password': password
    }
    users_collection.insert_one(user)

    return jsonify({'message': 'Login data stored in MongoDB'}), 201

if __name__ == '__main__':
    app.run(debug=True)
