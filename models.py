'''
#models.py
Defines the table for the database
'''
from enum import Enum
from app import db


class Messages(db.Model):
    '''
    Table definition for messages
    '''
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120))

    def __init__(self, a):
        self.message = a

    def __repr__(self):
        return "<message: %s>" % self.message


class AuthUser2(db.Model):
    '''
    Table definition for auth users
    '''
    id = db.Column(db.Integer, primary_key=True)
    auth_type = db.Column(db.String(120))
    name = db.Column(db.String(120))

    def __init__(self, name, auth_type):
        assert isinstance(auth_type) is AuthUserType
        self.name = name
        self.auth_type = auth_type.value  # sending enum value and not object

    def __repr__(self):
        return "<User name: {}\ntype: {}".format(self.name, self.auth_type)


class AuthUserType(Enum):
    '''
    Defines the correct enum values for auth
    '''
    LINKEDIN = "linkedin"
    GOOGLE = "google"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    TWITTER = "twitter"
    GITHUB = "github"
    PASSWORD = "password"
