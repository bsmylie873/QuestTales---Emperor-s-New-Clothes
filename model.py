from datetime import datetime
from server import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    username = db.Column(db.String(64), index=True, unique=True)
    alert = db.Column(db.String(1), default='0', nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    event = db.Column(db.Integer, db.ForeignKey('eventtype.et_id'), nullable=False)
    timestamp = db.Column(db.DateTime(128), index=True, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Event {}>'.format(self.event)


class EventType(db.Model):
    et_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    type = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return '<EventType {}>'.format(self.type)

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
