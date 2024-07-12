from . import config

class Config:
    SECRET_KEY = 'jdkfaljfa29824dsfjalsj8242'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+config.MYSQL_USER_ID \
        + ":" + config.MYSQL_PASSWORD +"@" +config.MYSQL_HOST + \
        "/" + config.MYSQL_DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_POOL_SIZE = 5
    # SQLALCHEMY_MAX_OVERFLOW = 10
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     "isolation_level": "READ COMMITTED"
    # }    
