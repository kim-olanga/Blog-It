import os

class Config:
    '''
    General configuration parent class
    '''
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_API_URI =''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kimberly:kim12345@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://'
    DEBUG = True


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
