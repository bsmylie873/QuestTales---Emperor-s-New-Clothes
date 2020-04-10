import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'server.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
