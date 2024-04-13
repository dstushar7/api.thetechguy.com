# app/config.py

import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql+pymysql://root:toor@localhost/thetechg_resumedb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT settings
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or '9WpbkXH3z13VBNm4QFAsyX62J5R7CKxELoLr8DvaUgt0'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jI7hVvPmcV8IWsWxzw4yI1KZAXfHEXhVkLkkXgQ4VU7B6lqT'
