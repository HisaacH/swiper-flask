from flask import Flask
from user import user_bp
from commen import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eraser:root@localhost/swiper'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

app.register_blueprint(user_bp, url_prefix='/user')


@app.route('/')
def home():
    return '<h1>你是来拉屎的嘛!</h1>'


if __name__ == '__main__':
    app.run()
