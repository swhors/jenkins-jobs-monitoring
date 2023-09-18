import os
import sqlite3
from config import Config
from flask_sqlalchemy import SQLAlchemy

mon_db = SQLAlchemy()


def init(flask_app):
    global mon_db
    base_path = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_path, Config.Db.db_file)
    print(f'db_path = {db_path}')
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    flask_app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    mon_db.init_app(flask_app)
    mon_db.app = flask_app
    mon_db.create_all()


def fint():
    global db_conn
    db_conn = None
