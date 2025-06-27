from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    if not users:
        return jsonify({"message": "No users found"}), 200
    else:
        return jsonify(users), 200
    
@app.route('/users/<user_id>', methods = ['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id:user}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
    
@app.route('/users', methods = ['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    name = data.get('name')

    if not user_id or not name:
        return jsonify({'error':'ID and name are required'}), 400
    
    users[user_id] = name
    return jsonify({'message': 'User added'}), 201

@app.route('/users/<user_id>', methods = ['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')

    if user_id not in users:
        return jsonify({'error':'User not found'}), 404
    
    users[user_id] = name
    return jsonify({'message': 'User updated'}), 200

@app.route('/users/<user_id>', methods = ['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'error':'User not found'}), 404
    
if __name__ == '__main__':
    app.run(debug = True)