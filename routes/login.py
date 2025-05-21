from flask import Blueprint, request, jsonify
from ..services.auth_service import verify_user

# 이 파일은 login 관련 기능을 모은 블루프린트다!
login_bp = Blueprint('login', __name__)

# POST 요청으로 /login 들어오면 이 함수 실행됨
@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('id')
    user_pw = data.get('pw')

    print(f"Received ID: {user_id}, PW: {user_pw}")

    if verify_user(user_id, user_pw):
        return jsonify(status='success', message='Login Success')
    else:
        return jsonify(status='fail', message='Login Failed')