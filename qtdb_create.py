from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

engine = create_engine('sqlite:///mymusic.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    username = Column(String(64), index=True, unique=True)
    alert = Column(String(1), default='0', nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Events(Base):
    """"""
    __tablename__ = "Event"

    event_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    event = Column(Integer, ForeignKey('eventtype.et_id'), nullable=False)
    timestamp = Column(datetime, index=True, default=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Event {}>'.format(self.event)


class EventType(Base):
    """"""
    __tablename__ = "Eventtype"

    et_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    type = Column(String(140), nullable=False)

    def __repr__(self):
        return '<EventType {}>'.format(self.type)


# create tables
Base.metadata.create_all(engine)
