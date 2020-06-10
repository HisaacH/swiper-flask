from commen import db


class Users(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(20), primary_key=True, nullable=False)
    nickname = db.Column(db.String(20), nullable=False, index=True)
    passwork = db.Column(db.String(128), nullable=False)
    birthday = db.Column(db.Date, default='2020-01-01')
    gender = db.Column(db.Enum('male', 'female', 'unknown'), default='unknown')
    avatar = db.Column(db.String(128), default='https://www.baidu.com')
    city = db.Column(db.String(20), default='上海')
