from dotenv import load_dotenv
load_dotenv()

from os import environ as env

class FlaskAppConfig:
    SECRET_KEY = env.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
