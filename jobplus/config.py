class BaseConfig(object):
        SECRET_KEY = 'make sure to set a very secret key'

class DevelopmentConfig(BaseConfig):
        DEBUG = True
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'

class ProductionConfig(BaseConfig):
        
        pass

class TestingConfig(BaseConfig):

        pass

configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
}
