from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('id')
    user_pw = data.get('pw')

    print(f"Received ID: {user_id}, PW: {user_pw}")

    if user_id == 'admin' and user_pw == '1234':
        return jsonify(status='success', message='Login Success')
    else:
        return jsonify(status='fail', message='Login Failed')