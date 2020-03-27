from . import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=None)
    create_user_id = db.Column(db.Integer, default=None)
    update_time = db.Column(db.DateTime, default=None)
    update_user_id = db.Column(db.Integer, default=None)

