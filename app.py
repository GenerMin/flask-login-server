from flask import Flask
from routes.login import login_bp  # Blueprint 가져오기

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(login_bp)

# 로컬에서 실행할 때만 작동 (개발용)
if __name__ == "__main__":
    app.run(debug=True)

# Render에서 Gunicorn으로 실행할 때 사용
if __name__ != "__main__":
    application = app