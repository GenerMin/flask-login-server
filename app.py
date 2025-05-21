from flask import Flask
from routes.login import login_bp  # Blueprint import

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(login_bp, url_prefix="")  # 슬래시 없이 루트로 등록

if __name__ == "__main__":
    app.run(debug=True)

application = app  # Render gunicorn용