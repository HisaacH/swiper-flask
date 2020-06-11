from commen import db


class Users(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(20), primary_key=True, nullable=False)
    phone = db.Column(db.Integer(20),)
    nickname = db.Column(db.String(20), nullable=False, index=True)
    passwork = db.Column(db.String(128), nullable=False)
    birthday = db.Column(db.Date, default='2020-01-01')
    gender = db.Column(db.Enum('male', 'female', 'unknown', name='Gender'), default='unknown')
    avatar = db.Column(db.String(128), default='https://www.baidu.com')
    city = db.Column(db.String(20), default='上海')


class Profile(db.model):
    __tablename__ = 'profile'
    dating_gender = db.Column(db.Enum('male', 'female', 'unknown', name='Dating Gender'))
    dating_city = db.Column(db.String(20), default='上海')
    min_distance = db.Column(db.Integer(), default=1, name='Min Distance')
    max_distance = db.Column(db.Integer(), default=10, name='Max Distance')
    min_dating_age = db.Column(db.Integer(), default=18, name='Min Dating Age')
    max_dating_age = db.Column(db.Integer(), default=30, name='Max Dating Age')
    vibration = db.Column(db.Boolean(), default=False)
