import os

class BaseConfig(object):
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        db = os.environ.get("DATABASE_URI")

        if db is None:
            raise ValueError("Missing env DATABASE_URI")
        
        return db
    
    @property
    def JWT_SECRET_KEY(self):
        secret_key = os.environ.get("JWT_SECRET")

        return secret_key or "super-secret"


class DevelopementConfig(BaseConfig):
    DEBUG=True


class ProductionConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    pass


env = os.environ.get("FLASK_ENV")

if env == "development":
    app_config = DevelopementConfig()
elif env == "testing":
    app_config = TestConfig()
else:
    app_config = ProductionConfig()
