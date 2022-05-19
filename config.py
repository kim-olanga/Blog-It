import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLAlchemy engine='sqlite:///:memory:'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kimberly:kim12345@localhost/tester'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='kimzyy123456'
    FLASK_APP="app:create_app(config_name)"
    FLASK_APP="manage.py"


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kimberly:kim12345@localhost/tester'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kimberly:kim12345@localhost/tester'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}