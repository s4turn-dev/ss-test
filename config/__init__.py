from dotenv import load_dotenv
load_dotenv()

from os import environ as env

class FlaskAppConfig:
    SERVER_NAME = env.get('APP_URL')
    SECRET_KEY = env.get('APP_SECRET')

    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
