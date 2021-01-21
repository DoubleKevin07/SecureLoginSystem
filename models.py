import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# This is the model for the MVC component. Specifically, it's the account model.
class Account(db.Model):

    # The accoutn table name.
    __tablename__ = "accounts"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)

    # Password hash.
    pw_hash = db.Column(db.String, nullable=False)
    salt = db.Column(db.LargeBinary, nullable=False)

    def __init__(self,name,pw,slt):
        self.username = name
        self.pw_hash = pw
        self.salt = slt

    def get_user(name):
        return Account.query.filter_by(username=name).first() # returns first user matching "username"

    def get_user_by_id(id):
        return Account.query.filter_by(id=id).first() # returns first user matching "username"