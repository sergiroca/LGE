from application import db

import datetime
from datetime import date
import time

from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField
from wtforms.validators import InputRequired, Email, Length


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    user_role = db.Column(db.String(80))
    is_active = db.Column(db.Boolean)

# ##### STEAKHOLDERS
class Provider(db.Model):
    __tablename__ = 'provider'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    keyword = db.Column(db.String(90), nullable=False)
    # 0 = NP, 1 = Fresco tipo 1, 2 = Fresco tipo 2
    group = db.Column(db.Integer, nullable=False)



