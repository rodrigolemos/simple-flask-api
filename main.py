from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        'id': 1,
        'first-name': 'Rodrigo',
        'last-name': 'Lemos',
        'age': 28
    },
    {
        'id': 2,
        'first-name': 'John',
        'last-name': 'Doe',
        'age': 30
    },
    {
        'id': 3,
        'first-name': 'Other',
        'last-name': 'User',
        'age': 32
    },
    {
        'id': 4,
        'first-name': 'New',
        'last-name': 'User',
        'age': 37
    }
]


@app.route('/', methods=['GET'])
def home():
    return "Simple Flask API. Request to /users", 200


@app.route('/users', methods=['GET'])
def list_all():
    return jsonify(users), 200


@app.route('/users/<string:first_name>', methods=['GET'])
def find_by_first_name(first_name):
    filtered_users = [user for user in users if user['first-name'] == first_name]
    return jsonify(filtered_users), 200


@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    users.append(user)
    return jsonify(user), 201


@app.route('/users/<int:p_id>', methods=['PUT'])
def update_user(p_id):
    for user in users:
        if user['id'] == p_id:
            user['first-name'] = request.get_json().get('first-name')
            user['last-name'] = request.get_json().get('last-name')
            user['age'] = request.get_json().get('age')

            return jsonify(user), 200

    return jsonify({'error': 'User not found'}), 404


@app.route('/users/<int:p_id>', methods=['DELETE'])
def delete_user(p_id):
    for user in users:
        if user['id'] == p_id:
            users.remove(user)

    return jsonify(users), 204


if __name__ == '__main__':
    app.run(debug=True)
