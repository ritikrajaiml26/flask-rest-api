# app.py
# Simple REST API with Flask for User Management

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (dictionary)
users = {
    1: {"name": "Ritik Raj", "email": "ritikrajaiml@gmail.com"},
    2: {"name": "Amit", "email": "amit@example.com"}
}

# GET - Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# GET - Get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST - Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"message": "User added", "user": users[new_id]}), 201

# PUT - Update existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    users[user_id].update(data)
    return jsonify({"message": "User updated", "user": users[user_id]}), 200

# DELETE - Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted_user}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
