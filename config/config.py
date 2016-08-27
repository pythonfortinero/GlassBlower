import os
os.getcwd()


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "always you can choose"
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.getcwd() + "/yourdatabase.db"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/yourdatabase"

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
