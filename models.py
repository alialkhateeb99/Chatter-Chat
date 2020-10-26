# models.py
import flask_sqlalchemy
from app import db
from enum import Enum


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120))

    def __init__(self, a):
        self.message = a

    def __repr__(self):
        return "<message: %s>" % self.message


class AuthUser2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auth_type = db.Column(db.String(120))
    name = db.Column(db.String(120))

    def __init__(self, name, auth_type):
        assert type(auth_type) is AuthUserType
        self.name = name
        self.auth_type = auth_type.value  # sending enum value and not object

    def __repr__(self):
        return "<User name: {}\ntype: {}".format(self.name, self.auth_type)


class AuthUserType(Enum):
    LINKEDIN = "linkedin"
    GOOGLE = "google"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    TWITTER = "twitter"
    GITHUB = "github"
    PASSWORD = "password"
